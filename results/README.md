# Resultados preliminares del pipeline

Estos resultados se generan ejecutando:

```powershell
.\.venv\Scripts\python.exe -m analysis.analyze_experiments
```

## Hallazgos preliminares

- Frecuencia efectiva de muestreo: aproximadamente 57.88 Hz.
- Frecuencia promedio mediante picos temporales: aproximadamente 7.235 Hz.
- Frecuencia promedio mediante FFT: aproximadamente 7.246 Hz.
- La frecuencia permanece prácticamente constante entre 1.0 y 3.0 cm.
- Relación de amortiguamiento estimada: aproximadamente 0.26% a 0.45%.
- Frecuencia teórica nominal usando 2 mm de espesor: aproximadamente 14.22 Hz.
- Espesor equivalente calibrado frente a la frecuencia experimental: aproximadamente 1.26 mm.

## Selección automática actual

| Ensayo | Desplazamiento | Liberación seleccionada |
| --- | ---: | ---: |
| E01_10mm | 1.0 cm | 3 |
| E02_15mm | 1.5 cm | 1 |
| E03_20mm | 2.0 cm | 3 |
| E04_25mm | 2.5 cm | 1 |
| E05_30mm | 3.0 cm | 1 |

Las selecciones deben confirmarse visualmente antes de cerrar el artículo.

## Nota técnica

Los registros del teléfono presentan pequeños saltos temporales. Antes del
filtrado y la FFT, el pipeline interpola las señales sobre una malla temporal
uniforme. Sin esta corrección, la FFT produce frecuencias desplazadas.
