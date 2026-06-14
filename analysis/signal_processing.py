from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import signal


@dataclass
class ReleaseAnalysis:
    """Agrupa los resultados y señales calculados para una liberación libre."""
    release_number: int
    start_time: float
    end_time: float
    score: float
    time: np.ndarray
    raw: np.ndarray
    filtered: np.ndarray
    peak_indices: np.ndarray
    period_s: float
    frequency_peaks_hz: float
    frequency_fft_hz: float
    logarithmic_decrement: float
    damping_ratio: float
    rdt_time: np.ndarray
    rdt_signal: np.ndarray


def load_accelerometer(csv_path, axis="z"):
    """Lee un CSV del sensor y lo interpola sobre una malla temporal uniforme."""
    frame = pd.read_csv(csv_path)
    required = {"seconds_elapsed", axis}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns in {csv_path}: {sorted(missing)}")

    frame = frame[["seconds_elapsed", axis]].dropna().copy()
    frame.columns = ["time", "acceleration"]
    frame = frame.sort_values("time").drop_duplicates("time")
    original_time = frame["time"].to_numpy(dtype=float)
    original_acceleration = frame["acceleration"].to_numpy(dtype=float)

    dt = np.diff(original_time)
    valid_dt = dt[np.isfinite(dt) & (dt > 0)]
    median_dt = float(np.median(valid_dt))
    sample_rate = 1.0 / median_dt

    # Los registros del celular contienen muestras omitidas ocasionalmente.
    # Los filtros digitales y la FFT suponen un muestreo uniforme, por lo que
    # primero se interpola la señal sin alterar la escala temporal original.
    time = np.arange(original_time[0], original_time[-1] + median_dt * 0.5, median_dt)
    acceleration = np.interp(time, original_time, original_acceleration)
    resampled = pd.DataFrame({"time": time, "acceleration": acceleration})
    return resampled, time, acceleration, sample_rate


def bandpass_filter(values, sample_rate, lowcut, highcut, order):
    """Elimina la deriva y el ruido exterior a la banda de vibración definida."""
    nyquist = 0.5 * sample_rate
    highcut = min(highcut, nyquist * 0.90)
    if lowcut >= highcut:
        raise ValueError(
            f"Invalid passband {lowcut}-{highcut} Hz for sample rate {sample_rate:.2f} Hz"
        )
    sos = signal.butter(
        order,
        [lowcut / nyquist, highcut / nyquist],
        btype="bandpass",
        output="sos",
    )
    centered = signal.detrend(values, type="linear")
    return signal.sosfiltfilt(sos, centered)


def detect_release_starts(
    time,
    filtered,
    sample_rate,
    count=3,
    minimum_separation_seconds=12.0,
):
    """Localiza el inicio de los eventos de vibración fuertes y separados."""
    envelope = np.abs(signal.hilbert(filtered))
    smooth_samples = max(3, int(round(sample_rate * 0.35)))
    smooth = np.convolve(
        envelope, np.ones(smooth_samples) / smooth_samples, mode="same"
    )
    prominence = max(np.std(smooth) * 0.8, np.ptp(smooth) * 0.08)
    peaks, properties = signal.find_peaks(
        smooth,
        distance=max(1, int(sample_rate * minimum_separation_seconds)),
        prominence=prominence,
    )
    if len(peaks) < count:
        peaks, properties = signal.find_peaks(
            smooth,
            distance=max(1, int(sample_rate * minimum_separation_seconds * 0.70)),
            prominence=max(np.std(smooth) * 0.4, np.ptp(smooth) * 0.04),
        )
    if len(peaks) < count:
        raise ValueError(f"Only {len(peaks)} release candidates were detected")

    prominence_values = properties["prominences"]
    selected = peaks[np.argsort(prominence_values)[-count:]]
    starts = []
    lookback = max(1, int(sample_rate * 1.0))
    threshold = np.median(smooth) + 2.5 * np.median(np.abs(smooth - np.median(smooth)))
    for peak in np.sort(selected):
        left = max(0, peak - lookback)
        candidates = np.flatnonzero(smooth[left : peak + 1] <= threshold)
        start = left + candidates[-1] if len(candidates) else left
        starts.append(start)
    return np.asarray(starts, dtype=int), smooth


def positive_peaks(time, filtered, sample_rate, minimum_separation_seconds):
    """Obtiene los índices de picos positivos físicamente separados."""
    prominence = max(np.std(filtered) * 0.12, np.ptp(filtered) * 0.015)
    indices, _ = signal.find_peaks(
        filtered,
        distance=max(1, int(sample_rate * minimum_separation_seconds)),
        prominence=prominence,
    )
    return indices


def period_from_peaks(time, peak_indices):
    """Estima periodo y frecuencia con la mediana del intervalo entre picos."""
    if len(peak_indices) < 4:
        return np.nan, np.nan
    differences = np.diff(time[peak_indices])
    period = float(np.median(differences))
    return period, 1.0 / period


def logarithmic_decrement(filtered, peak_indices):
    """Estima decremento y amortiguamiento usando varias separaciones de picos."""
    amplitudes = filtered[peak_indices]
    amplitudes = amplitudes[np.isfinite(amplitudes) & (amplitudes > 0)]
    if len(amplitudes) < 4:
        return np.nan, np.nan

    deltas = []
    max_gap = min(8, len(amplitudes) - 1)
    for gap in range(2, max_gap + 1):
        ratios = amplitudes[:-gap] / amplitudes[gap:]
        valid = ratios[np.isfinite(ratios) & (ratios > 1)]
        if len(valid):
            deltas.extend(np.log(valid) / gap)
    if not deltas:
        return np.nan, np.nan
    delta = float(np.median(deltas))
    zeta = float(delta / np.sqrt(4.0 * np.pi**2 + delta**2))
    return delta, zeta


def dominant_fft_frequency(values, sample_rate, lowcut, highcut):
    """Obtiene la frecuencia FFT dominante dentro de la banda analizada."""
    centered = signal.detrend(values, type="linear")
    window = signal.windows.hann(len(centered), sym=False)
    spectrum = np.abs(np.fft.rfft(centered * window))
    frequencies = np.fft.rfftfreq(len(centered), d=1.0 / sample_rate)
    valid = (frequencies >= lowcut) & (frequencies <= highcut)
    if not np.any(valid):
        return np.nan, frequencies, spectrum
    valid_indices = np.flatnonzero(valid)
    index = valid_indices[np.argmax(spectrum[valid])]
    return float(frequencies[index]), frequencies, spectrum


def random_decrement(
    filtered,
    sample_rate,
    window_seconds,
    max_segments,
):
    """Promedia segmentos activados para obtener una respuesta coherente."""
    length = max(8, int(round(window_seconds * sample_rate)))
    centered = filtered - np.mean(filtered)
    threshold = 0.25 * np.std(centered)
    crossings = np.flatnonzero(
        (centered[:-1] < threshold) & (centered[1:] >= threshold)
    ) + 1
    crossings = crossings[crossings + length <= len(centered)]
    if len(crossings) == 0:
        return np.arange(length) / sample_rate, np.full(length, np.nan)

    segments = np.asarray([centered[i : i + length] for i in crossings[:max_segments]])
    return np.arange(length) / sample_rate, np.mean(segments, axis=0)


def release_score(filtered, peak_indices, period_s, damping_ratio):
    """Puntúa una liberación por cantidad, regularidad, decaimiento y validez."""
    if len(peak_indices) < 4 or not np.isfinite(period_s):
        return -np.inf
    peak_times = peak_indices
    intervals = np.diff(peak_times)
    interval_cv = np.std(intervals) / np.mean(intervals) if np.mean(intervals) else 1.0
    amplitudes = np.abs(filtered[peak_indices])
    decay_fraction = np.mean(np.diff(amplitudes) < 0) if len(amplitudes) > 1 else 0.0
    damping_ok = 1.0 if np.isfinite(damping_ratio) and 0 < damping_ratio < 0.25 else 0.0
    return float(len(peak_indices) + 8.0 * decay_fraction + 4.0 * damping_ok - 12.0 * interval_cv)


def analyze_release(
    release_number,
    time,
    raw,
    filtered,
    sample_rate,
    lowcut,
    highcut,
    peak_min_separation_seconds,
    rdt_window_seconds,
    rdt_max_segments,
):
    """Ejecuta todos los cálculos requeridos para una liberación segmentada."""
    peaks = positive_peaks(
        time, filtered, sample_rate, peak_min_separation_seconds
    )
    period_s, frequency_peaks_hz = period_from_peaks(time, peaks)
    delta, damping_ratio = logarithmic_decrement(filtered, peaks)
    frequency_fft_hz, _, _ = dominant_fft_frequency(
        filtered, sample_rate, lowcut, highcut
    )
    rdt_time, rdt_signal = random_decrement(
        filtered, sample_rate, rdt_window_seconds, rdt_max_segments
    )
    score = release_score(filtered, peaks, period_s, damping_ratio)
    return ReleaseAnalysis(
        release_number=release_number,
        start_time=float(time[0]),
        end_time=float(time[-1]),
        score=score,
        time=time,
        raw=raw,
        filtered=filtered,
        peak_indices=peaks,
        period_s=period_s,
        frequency_peaks_hz=frequency_peaks_hz,
        frequency_fft_hz=frequency_fft_hz,
        logarithmic_decrement=delta,
        damping_ratio=damping_ratio,
        rdt_time=rdt_time,
        rdt_signal=rdt_signal,
    )
