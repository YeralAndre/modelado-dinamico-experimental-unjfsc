# Pipeline de análisis experimental

Este directorio contiene el procesamiento reproducible de los cinco ensayos de
vibración libre. Los archivos originales de `data/sensor` nunca se modifican.

## Instalación

Desde la terminal integrada, ubicada en la raíz del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Ejecución

```powershell
python -m analysis.analyze_experiments
```

## Funcionamiento

1. Lee `Accelerometer.csv` de cada ensayo.
2. Calcula la frecuencia efectiva de muestreo.
3. Interpola los registros irregulares sobre una malla temporal uniforme.
4. Filtra el eje Z entre 2 y 15 Hz.
5. Detecta las tres liberaciones del registro completo.
6. Analiza y puntúa las tres liberaciones.
7. Selecciona automáticamente la respuesta más representativa.
8. Calcula periodo, frecuencia, FFT, decremento logarítmico y amortiguamiento.
9. Genera una señal equivalente mediante RDT.
10. Construye los modelos físicos nominal y calibrado.
11. Exporta gráficas, tablas y datos procesados dentro de `results`.

## Archivos importantes

- `config.py`: parámetros físicos, rutas y ajustes del procesamiento.
- `signal_processing.py`: filtros, detección de liberaciones, picos, FFT y RDT.
- `modeling.py`: modelo de viga en voladizo y respuesta teórica.
- `analyze_experiments.py`: comando principal que ejecuta todo.

## Resultados

- `results/figures`: gráficas listas para revisar e insertar en el artículo.
- `results/tables/all_releases.csv`: métricas de las 15 liberaciones.
- `results/tables/selected_releases_summary.csv`: liberación elegida por ensayo.
- `results/tables/model_comparison.csv`: comparación nominal y calibrada.
- `results/processed_data`: segmentos seleccionados sin alterar los originales.
- `results/summary.json`: resumen legible por programas.

La selección automática debe revisarse visualmente antes de cerrar el artículo.
