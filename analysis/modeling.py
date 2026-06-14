from __future__ import annotations

import numpy as np
from scipy.optimize import brentq


def cantilever_model(
    length_m,
    width_m,
    thickness_m,
    young_modulus_pa,
    density_kg_m3,
    phone_mass_kg,
    modal_mass_factor,
):
    """Calcula las propiedades equivalentes del primer modo del voladizo."""
    inertia_m4 = width_m * thickness_m**3 / 12.0
    stiffness_n_m = 3.0 * young_modulus_pa * inertia_m4 / length_m**3
    free_beam_mass_kg = density_kg_m3 * width_m * thickness_m * length_m
    equivalent_mass_kg = phone_mass_kg + modal_mass_factor * free_beam_mass_kg
    natural_angular_frequency = np.sqrt(stiffness_n_m / equivalent_mass_kg)
    natural_frequency_hz = natural_angular_frequency / (2.0 * np.pi)
    return {
        "length_m": length_m,
        "width_m": width_m,
        "thickness_m": thickness_m,
        "inertia_m4": inertia_m4,
        "stiffness_n_m": stiffness_n_m,
        "free_beam_mass_kg": free_beam_mass_kg,
        "equivalent_mass_kg": equivalent_mass_kg,
        "natural_angular_frequency_rad_s": natural_angular_frequency,
        "natural_frequency_hz": natural_frequency_hz,
    }


def calibrate_thickness(target_frequency_hz, model_inputs, bounds=(0.0005, 0.003)):
    """Encuentra el espesor equivalente que reproduce una frecuencia objetivo."""
    def residual(thickness):
        return (
            cantilever_model(thickness_m=thickness, **model_inputs)[
                "natural_frequency_hz"
            ]
            - target_frequency_hz
        )

    return brentq(residual, *bounds)


def theoretical_acceleration(time, displacement_m, natural_frequency_hz, damping_ratio):
    """Genera la aceleración teórica amortiguada del modelo SDOF."""
    omega_n = 2.0 * np.pi * natural_frequency_hz
    zeta = float(np.clip(damping_ratio, 0.0, 0.99))
    omega_d = omega_n * np.sqrt(1.0 - zeta**2)
    exponential = np.exp(-zeta * omega_n * time)
    return (
        -displacement_m
        * omega_n**2
        * exponential
        * (
            np.cos(omega_d * time)
            + zeta / np.sqrt(1.0 - zeta**2) * np.sin(omega_d * time)
        )
    )
