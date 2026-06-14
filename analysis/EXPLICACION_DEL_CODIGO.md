# Explicación técnica del programa de análisis

Este documento explica cómo funciona el programa, cómo utiliza los datos de
configuración y cómo transforma los archivos experimentales en gráficas,
tablas y comparaciones teóricas.

## 1. Idea general

El programa separa tres tipos de información:

1. **Configuración:** datos conocidos y decisiones metodológicas.
2. **Procesamiento:** algoritmos que analizan las señales.
3. **Resultados:** valores, tablas y gráficas calculados automáticamente.

La ejecución comienza con:

```powershell
.\.venv\Scripts\python.exe -m analysis.analyze_experiments
```

El flujo general es:

```text
config.py
   |
   v
Carpetas experimentales -> Accelerometer.csv
   |
   v
Remuestreo -> filtrado -> detección de 3 liberaciones
   |
   v
Picos -> periodo/frecuencia -> amortiguamiento -> FFT -> RDT
   |
   v
Selección de una liberación por ensayo
   |
   v
Modelo físico nominal y calibrado
   |
   v
results/figures + results/tables + results/processed_data
```

## 2. Cómo se extraen los datos desde `config.py`

El programa principal importa la configuración mediante:

```python
from analysis import config
```

Desde ese momento puede consultar cualquier valor centralizado usando el
prefijo `config.`.

Por ejemplo:

```python
source = config.DATA_DIR / experiment["folder"] / "Accelerometer.csv"
```

Esta línea construye la ruta del CSV sin escribir manualmente una ruta completa.

- `config.DATA_DIR` apunta a `data/sensor`.
- `experiment["folder"]` contiene el nombre de la carpeta del ensayo actual.
- `"Accelerometer.csv"` identifica el archivo analizado.

Para `E01_10mm`, la ruta resultante es:

```text
data/sensor/1cm-2026-05-28_19-22-54/Accelerometer.csv
```

### 2.1 Diccionario de experimentos

En `config.py`, cada ensayo relaciona un código legible con su carpeta y su
desplazamiento inicial:

```python
EXPERIMENTS = {
    "E01_10mm": {
        "folder": "1cm-2026-05-28_19-22-54",
        "displacement_cm": 1.0,
    },
}
```

El programa recorre todos los ensayos mediante:

```python
for code, experiment in config.EXPERIMENTS.items():
    all_rows.extend(analyze_experiment(code, experiment))
```

Por tanto, agregar un nuevo ensayo no requiere copiar el algoritmo. Solo se
añade otra entrada a `EXPERIMENTS`.

### 2.2 Parámetros de procesamiento

Los parámetros metodológicos también se leen desde la configuración:

```python
filtered = bandpass_filter(
    raw,
    sample_rate,
    config.LOWCUT_HZ,
    config.HIGHCUT_HZ,
    config.FILTER_ORDER,
)
```

En este caso:

- `LOWCUT_HZ = 2.0`: elimina componentes lentas y deriva.
- `HIGHCUT_HZ = 15.0`: conserva la vibración dominante y reduce ruido rápido.
- `FILTER_ORDER = 4`: define el orden del filtro Butterworth.

Si se modifica uno de estos valores en `config.py`, todas las señales, tablas y
gráficas se regeneran utilizando la nueva configuración.

### 2.3 Parámetros del modelo físico

El modelo obtiene las propiedades físicas de la misma manera:

```python
model_inputs = {
    "length_m": config.FREE_LENGTH_M,
    "width_m": config.WIDTH_M,
    "young_modulus_pa": config.YOUNG_MODULUS_PA,
    "density_kg_m3": config.STEEL_DENSITY_KG_M3,
    "phone_mass_kg": config.PHONE_MASS_KG,
    "modal_mass_factor": config.MODAL_MASS_FACTOR,
}
```

Esto evita ocultar valores dentro de las ecuaciones. Las medidas pueden
revisarse y cambiarse desde un único archivo.

## 3. Responsabilidad de cada módulo

### `config.py`

Contiene:

- rutas de entrada y salida;
- relación entre códigos y carpetas experimentales;
- eje analizado;
- parámetros del filtro y segmentación;
- propiedades físicas del montaje.

No calcula resultados.

### `signal_processing.py`

Contiene los algoritmos que transforman una señal:

- lectura del CSV;
- corrección del muestreo irregular;
- filtrado;
- detección de liberaciones;
- detección de picos;
- periodo y frecuencia;
- decremento logarítmico;
- FFT;
- RDT;
- puntuación de calidad.

### `modeling.py`

Implementa las ecuaciones físicas:

$$
I=\frac{bh^3}{12}
$$

$$
k=\frac{3EI}{L^3}
$$

$$
m_{eq}=m_{celular}+0.236m_{viga}
$$

$$
f_n=\frac{1}{2\pi}\sqrt{\frac{k}{m_{eq}}}
$$

También calcula el espesor equivalente que hace coincidir la frecuencia del
modelo con la frecuencia experimental.

### `analyze_experiments.py`

Coordina los otros módulos. No contiene las fórmulas principales; decide en qué
orden aplicarlas, genera gráficas y guarda resultados.

## 4. Procesamiento paso a paso

### 4.1 Lectura y remuestreo

La función `load_accelerometer()` abre el CSV con pandas y conserva:

```text
seconds_elapsed
z
```

Luego calcula los intervalos entre muestras:

```python
dt = np.diff(original_time)
median_dt = np.median(dt)
sample_rate = 1 / median_dt
```

Los registros del teléfono contienen pequeños saltos temporales. Como un filtro
digital y la FFT requieren muestras uniformemente espaciadas, el programa crea
una malla regular:

```python
time = np.arange(inicio, final, median_dt)
acceleration = np.interp(time, original_time, original_acceleration)
```

Esta corrección fue necesaria: sin ella, la FFT produjo frecuencias desplazadas.

### 4.2 Filtrado

`bandpass_filter()`:

1. retira una tendencia lineal;
2. diseña un filtro Butterworth pasa-banda;
3. aplica el filtro hacia adelante y hacia atrás.

La aplicación bidireccional evita introducir un desplazamiento de fase:

```python
signal.sosfiltfilt(sos, centered)
```

### 4.3 Detección de las tres liberaciones

`detect_release_starts()` calcula primero la envolvente de la vibración mediante
la transformada de Hilbert:

```python
envelope = np.abs(signal.hilbert(filtered))
```

Las liberaciones aparecen como tres incrementos grandes en esa envolvente. El
programa localiza los tres máximos principales, exige una separación temporal
mínima y retrocede hasta encontrar el inicio de cada evento.

El resultado se muestra mediante líneas `L1`, `L2` y `L3` en las figuras de
registro completo.

### 4.4 Segmentación

Para cada inicio detectado, el programa toma una ventana configurada:

```python
window_samples = RELEASE_WINDOW_SECONDS * sample_rate
```

Actualmente se utilizan aproximadamente 12 segundos por liberación.

### 4.5 Detección de picos, periodo y frecuencia

`positive_peaks()` identifica máximos positivos respetando una separación
mínima entre picos.

El periodo se calcula como la mediana de las diferencias temporales:

```python
differences = np.diff(time[peak_indices])
period = np.median(differences)
frequency = 1 / period
```

La mediana reduce el efecto de un pico individual detectado con error.

### 4.6 Decremento logarítmico

El programa compara amplitudes separadas por varios ciclos:

$$
\delta=\frac{1}{n}\ln\left(\frac{A_i}{A_{i+n}}\right)
$$

Luego calcula:

$$
\zeta=\frac{\delta}{\sqrt{4\pi^2+\delta^2}}
$$

Se utiliza la mediana de múltiples estimaciones para disminuir la sensibilidad
al ruido.

### 4.7 FFT

Antes de aplicar la FFT se retira la tendencia y se multiplica la señal por una
ventana Hann. La ventana reduce la fuga espectral causada por analizar un
segmento temporal finito.

Después, el programa busca el máximo únicamente dentro de la banda configurada:

```python
valid = (frequencies >= LOWCUT_HZ) & (frequencies <= HIGHCUT_HZ)
```

El valor resultante es la frecuencia dominante experimental.

### 4.8 RDT

`random_decrement()` selecciona varios segmentos que cruzan un nivel de
activación con pendiente positiva. Luego los alinea y promedia:

```python
segments = [signal[i:i + length] for i in crossings]
rdt_signal = np.mean(segments, axis=0)
```

Las componentes aleatorias tienden a cancelarse, mientras se conserva la
respuesta periódica coherente.

### 4.9 Selección automática

Cada liberación recibe una puntuación basada en:

- cantidad de picos identificados;
- regularidad del periodo;
- proporción de amplitudes decrecientes;
- validez del amortiguamiento.

El programa selecciona la puntuación mayor:

```python
selected = max(analyses, key=lambda item: item.score)
```

La selección es automática y reproducible, pero debe revisarse visualmente
antes de cerrar el artículo.

## 5. Modelo físico

### 5.1 Modelo nominal

`cantilever_model()` usa directamente las medidas de `config.py`.

Con el espesor nominal de 2 mm obtiene una frecuencia teórica aproximada de
14.22 Hz. La diferencia frente a los 7.24 Hz experimentales muestra que existe
incertidumbre importante en las propiedades geométricas o en la idealización.

### 5.2 Modelo calibrado

`calibrate_thickness()` busca el espesor que hace que:

```text
frecuencia teórica - frecuencia experimental = 0
```

Para resolverlo utiliza el método numérico de Brent dentro de un intervalo de
0.5 a 3 mm. El espesor equivalente obtenido es aproximadamente 1.26 mm.

Este valor no se presenta como una medición física. Representa el parámetro
equivalente que permite al modelo simplificado reproducir la frecuencia real.

### 5.3 Comparación temporal

`theoretical_acceleration()` genera una respuesta amortiguada usando:

- desplazamiento inicial;
- frecuencia calibrada;
- amortiguamiento experimental.

El programa superpone esa respuesta con la señal experimental y calcula el
error cuadrático medio.

## 6. Archivos generados

### `results/figures`

Por cada ensayo:

- registro completo y liberaciones;
- liberación seleccionada y picos;
- FFT;
- RDT;
- comparación experimental-teórica.

También contiene comparaciones globales de frecuencia y amortiguamiento.

### `results/tables`

- `all_releases.csv`: resultados de las 15 liberaciones.
- `selected_releases_summary.csv`: una liberación seleccionada por ensayo.
- `model_comparison.csv`: modelo nominal y calibrado.
- `experimental_theoretical_error.csv`: error de las comparaciones.

### `results/processed_data`

Contiene únicamente los segmentos seleccionados y procesados. Los CSV
originales permanecen intactos.

### `results/summary.json`

Resume los resultados principales en un formato estructurado que puede ser
leído por otros programas.

## 7. Qué valores son configurados y cuáles son calculados

| Tipo | Ejemplos | Ubicación |
| --- | --- | --- |
| Medidas experimentales | longitud, ancho, masa del celular | `config.py` |
| Supuestos físicos | módulo de Young, densidad, factor modal | `config.py` |
| Decisiones metodológicas | banda del filtro, ventana, eje | `config.py` |
| Datos crudos | tiempo y aceleración | `data/sensor` |
| Resultados calculados | frecuencia, periodo, amortiguamiento | `results` |
| Parámetro calibrado | espesor equivalente | `results/tables/model_comparison.csv` |
