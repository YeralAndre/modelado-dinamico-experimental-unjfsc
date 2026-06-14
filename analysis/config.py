from pathlib import Path

# Todas las rutas del proyecto se derivan de la ubicación de este archivo.
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "sensor"
RESULTS_DIR = ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
TABLES_DIR = RESULTS_DIR / "tables"
PROCESSED_DIR = RESULTS_DIR / "processed_data"

# Este diccionario relaciona los códigos científicos de los ensayos con las
# carpetas privadas de origen y los desplazamientos iniciales controlados.
EXPERIMENTS = {
    "E01_10mm": {
        "folder": "1cm-2026-05-28_19-22-54",
        "displacement_cm": 1.0,
    },
    "E02_15mm": {
        "folder": "1_5cm-2026-05-28_19-28-28",
        "displacement_cm": 1.5,
    },
    "E03_20mm": {
        "folder": "2cm-2026-05-28_19-39-25",
        "displacement_cm": 2.0,
    },
    "E04_25mm": {
        "folder": "2_5cm-2026-05-28_19-44-02",
        "displacement_cm": 2.5,
    },
    "E05_30mm": {
        "folder": "3cm-2026-05-28_20-11-58",
        "displacement_cm": 3.0,
    },
}

# Parámetros del procesamiento. Se centralizan para que todas las figuras y
# tablas puedan reproducirse utilizando exactamente los mismos supuestos.
ANALYSIS_AXIS = "z"
LOWCUT_HZ = 2.0
HIGHCUT_HZ = 15.0
FILTER_ORDER = 4
RELEASE_WINDOW_SECONDS = 12.0
MIN_RELEASE_SEPARATION_SECONDS = 12.0
PEAK_MIN_SEPARATION_SECONDS = 0.08
RDT_WINDOW_SECONDS = 4.0
RDT_MAX_SEGMENTS = 80

# Propiedades utilizadas por el modelo físico.
YOUNG_MODULUS_PA = 2.0e11
STEEL_DENSITY_KG_M3 = 7850.0
FREE_LENGTH_M = 0.20
WIDTH_M = 0.038
NOMINAL_THICKNESS_M = 0.002
PHONE_MASS_KG = 0.210
MODAL_MASS_FACTOR = 0.236
