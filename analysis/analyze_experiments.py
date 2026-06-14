from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analysis import config
from analysis.modeling import (
    calibrate_thickness,
    cantilever_model,
    theoretical_acceleration,
)
from analysis.signal_processing import (
    analyze_release,
    bandpass_filter,
    detect_release_starts,
    dominant_fft_frequency,
    load_accelerometer,
)


def ensure_output_directories():
    """Crea las carpetas de salida sin modificar los datos originales."""
    for directory in (
        config.RESULTS_DIR,
        config.FIGURES_DIR,
        config.TABLES_DIR,
        config.PROCESSED_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)


def save_figure(path):
    """Exporta una figura lista para publicación y libera su memoria."""
    plt.tight_layout()
    plt.savefig(path, dpi=220, bbox_inches="tight")
    plt.close()


def analyze_experiment(code, experiment):
    """Analiza las tres liberaciones contenidas en un registro experimental."""
    source = config.DATA_DIR / experiment["folder"] / "Accelerometer.csv"
    frame, time, raw, sample_rate = load_accelerometer(source, config.ANALYSIS_AXIS)
    filtered = bandpass_filter(
        raw,
        sample_rate,
        config.LOWCUT_HZ,
        config.HIGHCUT_HZ,
        config.FILTER_ORDER,
    )
    starts, envelope = detect_release_starts(
        time,
        filtered,
        sample_rate,
        count=3,
        minimum_separation_seconds=config.MIN_RELEASE_SEPARATION_SECONDS,
    )

    plt.figure(figsize=(11, 4.8))
    plt.plot(time, raw, color="0.70", linewidth=0.7, label="Señal cruda, eje Z")
    plt.plot(time, filtered, color="#1565c0", linewidth=0.8, label="Señal filtrada")
    for number, start in enumerate(starts, 1):
        plt.axvline(time[start], color="#c62828", linestyle="--", linewidth=1)
        plt.text(time[start], plt.ylim()[1] * 0.82, f"L{number}", color="#c62828")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Aceleración (m/s²)")
    plt.title(f"{code}: registro completo y liberaciones detectadas")
    plt.legend()
    plt.grid(alpha=0.25)
    save_figure(config.FIGURES_DIR / f"{code}_registro_completo.png")

    analyses = []
    window_samples = int(round(config.RELEASE_WINDOW_SECONDS * sample_rate))
    for number, start in enumerate(starts, 1):
        end = min(len(time), start + window_samples)
        local_time = time[start:end] - time[start]
        analyses.append(
            analyze_release(
                number,
                local_time,
                raw[start:end],
                filtered[start:end],
                sample_rate,
                config.LOWCUT_HZ,
                config.HIGHCUT_HZ,
                config.PEAK_MIN_SEPARATION_SECONDS,
                config.RDT_WINDOW_SECONDS,
                config.RDT_MAX_SEGMENTS,
            )
        )

    selected = max(analyses, key=lambda item: item.score)
    selected_frame = pd.DataFrame(
        {
            "time_s": selected.time,
            "raw_acceleration_m_s2": selected.raw,
            "filtered_acceleration_m_s2": selected.filtered,
        }
    )
    selected_frame.to_csv(
        config.PROCESSED_DIR / f"{code}_liberacion_seleccionada.csv", index=False
    )

    plt.figure(figsize=(10, 4.8))
    plt.plot(selected.time, selected.raw, color="0.65", linewidth=0.8, label="Cruda")
    plt.plot(
        selected.time,
        selected.filtered,
        color="#1565c0",
        linewidth=1.1,
        label="Filtrada",
    )
    plt.scatter(
        selected.time[selected.peak_indices],
        selected.filtered[selected.peak_indices],
        color="#c62828",
        s=16,
        label="Picos positivos",
        zorder=3,
    )
    plt.xlabel("Tiempo desde la liberación (s)")
    plt.ylabel("Aceleración (m/s²)")
    plt.title(f"{code}: liberación {selected.release_number} seleccionada")
    plt.legend()
    plt.grid(alpha=0.25)
    save_figure(config.FIGURES_DIR / f"{code}_liberacion_seleccionada.png")

    frequency_fft_hz, frequencies, spectrum = dominant_fft_frequency(
        selected.filtered,
        sample_rate,
        config.LOWCUT_HZ,
        config.HIGHCUT_HZ,
    )
    valid = frequencies <= config.HIGHCUT_HZ
    plt.figure(figsize=(8, 4.6))
    plt.plot(frequencies[valid], spectrum[valid], color="#4527a0")
    plt.axvline(
        frequency_fft_hz,
        color="#c62828",
        linestyle="--",
        label=f"Pico: {frequency_fft_hz:.3f} Hz",
    )
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.title(f"{code}: espectro FFT")
    plt.legend()
    plt.grid(alpha=0.25)
    save_figure(config.FIGURES_DIR / f"{code}_fft.png")

    plt.figure(figsize=(8, 4.6))
    plt.plot(selected.rdt_time, selected.rdt_signal, color="#00897b")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Aceleración equivalente (m/s²)")
    plt.title(f"{code}: Random Decrement Technique")
    plt.grid(alpha=0.25)
    save_figure(config.FIGURES_DIR / f"{code}_rdt.png")

    release_rows = []
    for item in analyses:
        release_rows.append(
            {
                "experiment": code,
                "displacement_cm": experiment["displacement_cm"],
                "release": item.release_number,
                "start_time_s": item.start_time,
                "end_time_s": item.end_time,
                "quality_score": item.score,
                "selected": item.release_number == selected.release_number,
                "period_s": item.period_s,
                "frequency_peaks_hz": item.frequency_peaks_hz,
                "frequency_fft_hz": item.frequency_fft_hz,
                "logarithmic_decrement": item.logarithmic_decrement,
                "damping_ratio": item.damping_ratio,
                "number_of_peaks": len(item.peak_indices),
                "sample_rate_hz": sample_rate,
            }
        )
    return release_rows


def add_model_results(selected):
    """Construye modelos nominal/calibrado y los compara con las liberaciones."""
    model_inputs = {
        "length_m": config.FREE_LENGTH_M,
        "width_m": config.WIDTH_M,
        "young_modulus_pa": config.YOUNG_MODULUS_PA,
        "density_kg_m3": config.STEEL_DENSITY_KG_M3,
        "phone_mass_kg": config.PHONE_MASS_KG,
        "modal_mass_factor": config.MODAL_MASS_FACTOR,
    }
    nominal = cantilever_model(thickness_m=config.NOMINAL_THICKNESS_M, **model_inputs)
    target_frequency = float(selected["frequency_fft_hz"].mean())
    calibrated_thickness = calibrate_thickness(target_frequency, model_inputs)
    calibrated = cantilever_model(thickness_m=calibrated_thickness, **model_inputs)

    model_table = pd.DataFrame(
        [
            {"model": "Nominal", **nominal},
            {"model": "Calibrated", **calibrated},
        ]
    )
    model_table["error_vs_experimental_percent"] = (
        100.0
        * (model_table["natural_frequency_hz"] - target_frequency)
        / target_frequency
    )
    model_table.to_csv(config.TABLES_DIR / "model_comparison.csv", index=False)

    comparison_rows = []
    for _, row in selected.iterrows():
        processed = pd.read_csv(
            config.PROCESSED_DIR / f"{row['experiment']}_liberacion_seleccionada.csv"
        )
        time = processed["time_s"].to_numpy()
        experimental = processed["filtered_acceleration_m_s2"].to_numpy()
        damping = row["damping_ratio"] if np.isfinite(row["damping_ratio"]) else 0.02
        theoretical = theoretical_acceleration(
            time,
            row["displacement_cm"] / 100.0,
            calibrated["natural_frequency_hz"],
            damping,
        )
        # Iguala la amplitud para comparar principalmente la forma y el decaimiento.
        if np.max(np.abs(theoretical)) > 0:
            theoretical *= np.max(np.abs(experimental)) / np.max(np.abs(theoretical))
        rmse = float(np.sqrt(np.mean((experimental - theoretical) ** 2)))
        nrmse = rmse / max(np.ptp(experimental), np.finfo(float).eps)
        comparison_rows.append(
            {
                "experiment": row["experiment"],
                "displacement_cm": row["displacement_cm"],
                "rmse_m_s2": rmse,
                "normalized_rmse": nrmse,
            }
        )

        plt.figure(figsize=(10, 4.8))
        plt.plot(time, experimental, color="#1565c0", label="Experimental filtrada")
        plt.plot(
            time,
            theoretical,
            color="#c62828",
            linestyle="--",
            label="Modelo calibrado",
        )
        plt.xlabel("Tiempo desde la liberación (s)")
        plt.ylabel("Aceleración (m/s²)")
        plt.title(f"{row['experiment']}: comparación experimental-teórica")
        plt.legend()
        plt.grid(alpha=0.25)
        save_figure(
            config.FIGURES_DIR / f"{row['experiment']}_experimental_teorica.png"
        )

    pd.DataFrame(comparison_rows).to_csv(
        config.TABLES_DIR / "experimental_theoretical_error.csv", index=False
    )


def create_global_figures(selected):
    """Compara frecuencia y amortiguamiento entre los desplazamientos iniciales."""
    plt.figure(figsize=(8, 4.8))
    plt.plot(
        selected["displacement_cm"],
        selected["frequency_fft_hz"],
        "o-",
        label="FFT",
    )
    plt.plot(
        selected["displacement_cm"],
        selected["frequency_peaks_hz"],
        "s--",
        label="Picos temporales",
    )
    plt.xlabel("Desplazamiento inicial (cm)")
    plt.ylabel("Frecuencia (Hz)")
    plt.title("Frecuencia identificada frente al desplazamiento inicial")
    plt.legend()
    plt.grid(alpha=0.25)
    save_figure(config.FIGURES_DIR / "comparacion_frecuencias.png")

    plt.figure(figsize=(8, 4.8))
    plt.plot(
        selected["displacement_cm"],
        100.0 * selected["damping_ratio"],
        "o-",
        color="#ef6c00",
    )
    plt.xlabel("Desplazamiento inicial (cm)")
    plt.ylabel("Relación de amortiguamiento (%)")
    plt.title("Amortiguamiento frente al desplazamiento inicial")
    plt.grid(alpha=0.25)
    save_figure(config.FIGURES_DIR / "comparacion_amortiguamiento.png")


def main():
    """Ejecuta el flujo reproducible completo para cada ensayo configurado."""
    if not config.DATA_DIR.exists():
        raise FileNotFoundError("No se encontró la carpeta de sensores")
    ensure_output_directories()
    all_rows = []
    for code, experiment in config.EXPERIMENTS.items():
        print(f"Analizando {code}...")
        all_rows.extend(analyze_experiment(code, experiment))

    releases = pd.DataFrame(all_rows)
    releases.to_csv(config.TABLES_DIR / "all_releases.csv", index=False)
    selected = releases[releases["selected"]].copy().sort_values("displacement_cm")
    selected.to_csv(config.TABLES_DIR / "selected_releases_summary.csv", index=False)

    create_global_figures(selected)
    add_model_results(selected)

    summary = {
        "selected_releases": selected[
            [
                "experiment",
                "displacement_cm",
                "release",
                "frequency_peaks_hz",
                "frequency_fft_hz",
                "damping_ratio",
                "sample_rate_hz",
            ]
        ].to_dict(orient="records"),
        "mean_fft_frequency_hz": float(selected["frequency_fft_hz"].mean()),
        "mean_peak_frequency_hz": float(selected["frequency_peaks_hz"].mean()),
        "mean_damping_ratio": float(selected["damping_ratio"].mean()),
    }
    (config.RESULTS_DIR / "summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(f"Resultados guardados en: {config.RESULTS_DIR}")


if __name__ == "__main__":
    main()
