# IDENTIFICACIÓN EXPERIMENTAL Y MODELADO DE PARÁMETROS DINÁMICOS DE UNA VIGA EN VOLADIZO MEDIANTE UN ACELERÓMETRO MÓVIL

**Yeral Reyes Solis, Deyvid Borja Chiroque y Robert Vasquez Altunas**  
Universidad Nacional José Faustino Sánchez Carrión  
Curso: Ecuaciones Diferenciales  
Docente: GOÑY AMERI Carlos Francisco  
Huacho, Perú, 2026

> **Nota de trabajo:** Este archivo contiene el texto base de la primera parte del artículo. El resumen, los resultados, la discusión y las conclusiones deberán actualizarse después del procesamiento definitivo en Python. Las indicaciones entre corchetes son marcadores editoriales y no deben permanecer en la entrega final.

## Resumen provisional

El presente estudio tiene como objetivo identificar experimentalmente los principales parámetros dinámicos de un sistema simplificado de un grado de libertad mediante ensayos de vibración libre. El espécimen estuvo constituido por una escuadra metálica de acero dispuesta como viga en voladizo y un teléfono inteligente fijado en su extremo libre, empleado simultáneamente como masa concentrada y sensor de aceleración. Se realizaron cinco mediciones aplicando desplazamientos iniciales controlados de 1.0, 1.5, 2.0, 2.5 y 3.0 cm. Para cada nivel se registraron tres liberaciones sucesivas mediante la aplicación Sensor Logger.

De cada registro completo se seleccionará una liberación representativa para analizar la aceleración dominante en el eje Z. El procesamiento computacional comprenderá la segmentación de la señal, filtrado digital, detección de picos, cálculo del periodo y la frecuencia amortiguada, estimación del amortiguamiento mediante decremento logarítmico, análisis mediante Transformada Rápida de Fourier y aplicación de la técnica de decremento aleatorio. Asimismo, se desarrollará un modelo matemático equivalente de un grado de libertad a partir de las propiedades físicas del montaje. Finalmente, la respuesta experimental será comparada con la respuesta teórica para evaluar la capacidad del modelo simplificado de representar el comportamiento dinámico observado.

**Palabras clave:** vibración libre, sistema de un grado de libertad, acelerómetro móvil, frecuencia natural, amortiguamiento, viga en voladizo.

## 1. Introducción

El estudio de la respuesta estructural ante acciones variables en el tiempo permite comprender fenómenos asociados con vibraciones mecánicas, excitaciones ambientales y movimientos sísmicos. Entre las propiedades fundamentales utilizadas para caracterizar dinámicamente un sistema se encuentran su masa, rigidez, frecuencia natural y capacidad de disipación de energía. La identificación adecuada de estos parámetros resulta importante porque permite describir la respuesta del sistema, evaluar su sensibilidad ante diferentes excitaciones y formular modelos matemáticos capaces de aproximar su comportamiento real (Chopra, 2017; Inman, 2014).

Los ensayos dinámicos convencionales suelen requerir acelerómetros especializados y equipos de adquisición de datos. Sin embargo, los dispositivos móviles actuales incorporan sensores microelectromecánicos capaces de registrar aceleraciones en diferentes ejes. Estos sensores permiten desarrollar experiencias educativas y análisis experimentales preliminares mediante instrumentos accesibles, aunque presentan limitaciones relacionadas con ruido, orientación, frecuencia de muestreo y características particulares del dispositivo (Gallitto & Lupo, 2015; Monteiro et al., 2014).

En esta investigación se analiza una escuadra metálica de acero configurada como una viga en voladizo, con un teléfono inteligente fijado en el extremo libre. El sistema fue excitado mediante desplazamientos iniciales conocidos y liberado sin la aplicación deliberada de una fuerza posterior. La respuesta de aceleración registrada presenta el comportamiento oscilatorio decreciente característico de una vibración libre amortiguada.

El trabajo combina dos perspectivas complementarias. La primera corresponde a la identificación experimental de los parámetros dinámicos a partir de las señales registradas por el acelerómetro. La segunda consiste en la formulación de un modelo matemático equivalente de un grado de libertad construido a partir de las dimensiones, masa y propiedades estimadas del espécimen. La comparación entre ambas perspectivas permitirá evaluar el nivel de correspondencia entre el sistema físico real y su idealización matemática.

### 1.1 Planteamiento del problema

Los modelos dinámicos simplificados permiten representar el comportamiento predominante de numerosos sistemas físicos. No obstante, las propiedades ideales asumidas durante su formulación pueden diferir de las condiciones reales debido a incertidumbres geométricas, flexibilidad del empotramiento, distribución de masas, ruido instrumental y variaciones introducidas durante la excitación manual.

En consecuencia, se plantea la siguiente pregunta de investigación:

**¿En qué medida un modelo matemático equivalente de un grado de libertad permite representar la respuesta experimental de una viga en voladizo instrumentada con un acelerómetro móvil y sometida a diferentes desplazamientos iniciales?**

### 1.2 Objetivo general

Identificar experimentalmente los parámetros dinámicos de una viga metálica en voladizo mediante un acelerómetro móvil y comparar su respuesta con la obtenida a partir de un modelo matemático equivalente de un grado de libertad.

### 1.3 Objetivos específicos

1. Registrar la respuesta de vibración libre del sistema para desplazamientos iniciales de 1.0, 1.5, 2.0, 2.5 y 3.0 cm.
2. Seleccionar y procesar una liberación representativa de cada medición experimental.
3. Determinar el periodo, la frecuencia dominante y la relación de amortiguamiento mediante análisis temporal, decremento logarítmico, FFT y RDT.
4. Formular un modelo matemático equivalente utilizando las propiedades físicas disponibles del montaje.
5. Comparar las respuestas y los parámetros obtenidos experimental y teóricamente.
6. Evaluar la repetibilidad de la frecuencia identificada al modificar el desplazamiento inicial.

## 2. Marco teórico

### 2.1 Vibración libre amortiguada

La vibración libre se produce cuando un sistema es apartado de su posición de equilibrio y posteriormente liberado sin permanecer sometido a una excitación externa. En un sistema real, la amplitud disminuye gradualmente debido a la disipación de energía ocasionada por mecanismos como fricción interna, resistencia del aire, movimientos relativos y pérdidas en las conexiones.

La respuesta observada en el montaje corresponde a un sistema subamortiguado, condición definida por:

$$
0 < \zeta < 1
$$

donde $\zeta$ representa la relación de amortiguamiento. En este tipo de sistema se producen oscilaciones cuya amplitud decrece progresivamente con el tiempo.

### 2.2 Idealización como sistema de un grado de libertad

El montaje experimental se idealiza como un sistema de un grado de libertad compuesto por una masa equivalente $m$, una rigidez equivalente $k$ y un amortiguador viscoso equivalente $c$. El movimiento se representa mediante una única coordenada generalizada $x(t)$.

La ecuación de movimiento para vibración libre amortiguada es:

$$
m\ddot{x}(t)+c\dot{x}(t)+kx(t)=0
$$

donde:

- $m$ es la masa equivalente del sistema;
- $c$ es el coeficiente de amortiguamiento equivalente;
- $k$ es la rigidez equivalente;
- $x(t)$ es el desplazamiento dinámico;
- $\dot{x}(t)$ es la velocidad;
- $\ddot{x}(t)$ es la aceleración.

[Insertar posteriormente una figura conceptual del sistema SDOF.]

### 2.3 Parámetros dinámicos

La frecuencia angular natural no amortiguada se determina mediante:

$$
\omega_n=\sqrt{\frac{k}{m}}
$$

La frecuencia natural expresada en hercios es:

$$
f_n=\frac{\omega_n}{2\pi}
$$

La frecuencia angular amortiguada se relaciona con la frecuencia natural mediante:

$$
\omega_d=\omega_n\sqrt{1-\zeta^2}
$$

El periodo amortiguado y la frecuencia amortiguada se expresan como:

$$
T_d=\frac{2\pi}{\omega_d}
$$

$$
f_d=\frac{1}{T_d}
$$

Para sistemas con amortiguamiento reducido, la frecuencia amortiguada es cercana a la frecuencia natural no amortiguada. Esta aproximación deberá comprobarse a partir de los resultados experimentales.

### 2.4 Viga en voladizo con masa en el extremo

La escuadra metálica utilizada se representa como una viga en voladizo de sección rectangular. Para una carga aplicada en el extremo libre, la rigidez equivalente puede aproximarse mediante:

$$
k=\frac{3EI}{L^3}
$$

donde $E$ es el módulo de elasticidad del material, $I$ es el momento de inercia geométrico de la sección y $L$ es la longitud libre.

Para una sección rectangular:

$$
I=\frac{bh^3}{12}
$$

donde $b$ representa el ancho y $h$ el espesor de la sección en la dirección de flexión. Debido a que el espesor aparece elevado al cubo, pequeñas incertidumbres en su medición pueden producir variaciones importantes en la rigidez teórica calculada.

La masa equivalente del sistema puede aproximarse mediante:

$$
m_{eq}=m_{celular}+\alpha m_{viga}
$$

donde $\alpha\approx0.236$ representa la contribución modal aproximada de la masa distribuida de una viga uniforme en voladizo para su primer modo de vibración.

### 2.5 Decremento logarítmico

La relación de amortiguamiento puede estimarse a partir de la reducción de amplitudes entre picos positivos de una respuesta subamortiguada. Para dos amplitudes separadas por $n$ ciclos, el decremento logarítmico se calcula mediante:

$$
\delta=\frac{1}{n}\ln\left(\frac{A_i}{A_{i+n}}\right)
$$

La relación de amortiguamiento se obtiene como:

$$
\zeta=\frac{\delta}{\sqrt{4\pi^2+\delta^2}}
$$

El uso de picos separados por varios ciclos permite reducir la sensibilidad del cálculo frente al ruido asociado con un único par de amplitudes.

### 2.6 Transformada Rápida de Fourier

La Transformada Rápida de Fourier permite representar una señal temporal en el dominio de la frecuencia. En el espectro resultante, la frecuencia asociada con el pico principal corresponde a la componente dominante de la respuesta. Para un sistema gobernado principalmente por su primer modo, dicha frecuencia debe ser cercana a la frecuencia obtenida a partir de los picos temporales.

Antes de aplicar la FFT se debe seleccionar una ventana útil, retirar la componente media de la señal y considerar el intervalo temporal real entre muestras. Estas acciones evitan interpretar componentes constantes o errores de escala como contenido dinámico del sistema (Oppenheim & Schafer, 2010).

### 2.7 Técnica de decremento aleatorio

La técnica de decremento aleatorio o Random Decrement Technique permite obtener una respuesta equivalente mediante la selección y el promedio de segmentos que cumplen una condición de activación. Durante el promedio, las componentes aleatorias tienden a reducirse, mientras que la respuesta coherente del sistema permanece. Esta técnica puede emplearse para facilitar la identificación de frecuencia y amortiguamiento en señales contaminadas por ruido (Tamura et al., 1999).

## 3. Metodología

### 3.1 Enfoque y diseño experimental

La investigación presenta un enfoque cuantitativo y experimental. Se estudió la respuesta de vibración libre de un sistema físico sometido a cinco desplazamientos iniciales controlados. Para cada nivel de desplazamiento se realizaron tres liberaciones sucesivas, registradas dentro de un mismo archivo de adquisición.

La variable modificada durante los ensayos fue el desplazamiento inicial. Las propiedades geométricas del espécimen, la ubicación del teléfono, la condición de apoyo y el procedimiento de liberación se mantuvieron aproximadamente constantes.

### 3.2 Espécimen y montaje

El espécimen estuvo compuesto por una escuadra metálica de acero dispuesta horizontalmente como viga en voladizo. Uno de sus extremos fue fijado mediante una prensa a una superficie rígida, mientras que en el extremo libre se colocó un teléfono inteligente sin funda y asegurado con una cantidad reducida de cinta adhesiva.

El dispositivo móvil cumplió simultáneamente dos funciones: actuó como masa concentrada adicional y registró la aceleración del sistema mediante su acelerómetro integrado.

**Tabla. Parámetros físicos disponibles del montaje**

| Parámetro | Símbolo | Valor disponible | Condición |
| --- | --- | ---: | --- |
| Longitud libre | $L$ | 0.20 m | Medida durante el montaje |
| Ancho de la escuadra | $b$ | 0.038 m | Medida nominal |
| Espesor | $h$ | Cercano a 0.002 m | Estimación visual pendiente de calibración |
| Material | — | Acero | Confirmado |
| Masa del celular | $m_{celular}$ | 0.210 kg | Valor utilizado en el avance |
| Masa de la escuadra completa | — | 0.300–0.350 kg | Estimación; no equivale a la masa vibrante |
| Módulo elástico adoptado | $E$ | $2.0\times10^{11}$ Pa | Valor teórico para acero |

[Insertar fotografía del montaje: `01_montaje_prensa_regla.jpg` o `05_ensayo_1_5cm_vibracion.jpg`.]

[Insertar fotografía de la escuadra: `09_escuadra_metalica_acero.png`.]

### 3.3 Instrumentación y adquisición

La adquisición se realizó mediante un teléfono Redmi Note 14 Pro+ 5G y la aplicación Sensor Logger. La aplicación registró simultáneamente diferentes sensores y exportó los resultados en archivos CSV. Para el análisis dinámico se utilizará principalmente el archivo `Accelerometer.csv`, que contiene el tiempo transcurrido y las componentes de aceleración correspondientes a los ejes X, Y y Z.

La respuesta dominante se observó en el eje Z, por lo que esta componente será utilizada como señal principal. La frecuencia efectiva de muestreo será calculada directamente a partir de la columna temporal de cada archivo, debido a que el intervalo real entre muestras puede diferir de la configuración solicitada a la aplicación.

### 3.4 Procedimiento experimental

El procedimiento aplicado fue el siguiente:

1. Se fijó la escuadra metálica a una superficie rígida mediante una prensa, estableciendo una longitud libre aproximada de 20 cm.
2. Se colocó el teléfono inteligente en el extremo libre y se aseguró para reducir movimientos relativos.
3. Se inició el registro mediante Sensor Logger antes de producir la liberación.
4. Se aplicó un desplazamiento vertical inicial conocido y se liberó el sistema procurando no impartir una velocidad adicional.
5. Se esperó hasta que la respuesta disminuyera y el sistema se aproximara nuevamente al reposo.
6. Se repitió la liberación tres veces para el mismo desplazamiento.
7. El procedimiento completo se realizó para desplazamientos iniciales de 1.0, 1.5, 2.0, 2.5 y 3.0 cm.
8. Los registros fueron identificados y exportados para su procesamiento computacional.

**Tabla. Matriz experimental**

| Ensayo | Desplazamiento inicial | Liberaciones registradas | Componente principal |
| --- | ---: | ---: | --- |
| E01 | 1.0 cm | 3 | Eje Z |
| E02 | 1.5 cm | 3 | Eje Z |
| E03 | 2.0 cm | 3 | Eje Z |
| E04 | 2.5 cm | 3 | Eje Z |
| E05 | 3.0 cm | 3 | Eje Z |

### 3.5 Selección de la liberación representativa

Cada archivo contiene tres respuestas de vibración libre. Para mantener un procedimiento consistente, se seleccionará una liberación representativa por desplazamiento mediante criterios objetivos:

- presencia de un inicio identificable;
- ausencia de contacto o manipulación durante el decaimiento;
- respuesta completa hasta aproximarse al nivel de ruido;
- amplitud inicial coherente con las demás liberaciones del mismo ensayo;
- ausencia de valores atípicos o interrupciones;
- comportamiento oscilatorio predominantemente amortiguado.

La selección no dependerá necesariamente de que la liberación sea la primera, segunda o tercera. El segmento elegido tendrá una duración aproximada de 10 a 12 segundos y será documentado mediante sus tiempos inicial y final.

### 3.6 Procesamiento computacional propuesto

El procesamiento será desarrollado en Python utilizando bibliotecas para lectura, cálculo numérico, procesamiento de señales y representación gráfica. Las etapas serán:

1. Lectura de los archivos CSV y verificación de las columnas temporales y acelerométricas.
2. Cálculo de la frecuencia efectiva de muestreo.
3. Visualización del registro completo con las tres liberaciones.
4. Selección de una liberación representativa por desplazamiento.
5. Retiro de la media y corrección de tendencia cuando resulte necesario.
6. Aplicación de un filtro digital apropiado, documentando sus frecuencias de corte.
7. Identificación automática de picos positivos.
8. Cálculo del periodo y frecuencia mediante diferencias temporales entre picos.
9. Estimación del amortiguamiento mediante decremento logarítmico.
10. Obtención del espectro de frecuencias mediante FFT.
11. Aplicación de RDT y estimación de parámetros sobre la señal equivalente.
12. Generación de tablas y figuras comparativas entre desplazamientos.

**Tabla. Productos previstos del procesamiento**

| Etapa | Producto esperado |
| --- | --- |
| Registro completo | Gráfica con las tres liberaciones |
| Segmentación | Gráfica de la liberación seleccionada |
| Filtrado | Comparación entre señal cruda y filtrada |
| Detección de picos | Periodo, frecuencia y amplitudes |
| Decremento logarítmico | Relación de amortiguamiento |
| FFT | Frecuencia dominante |
| RDT | Respuesta equivalente con reducción de ruido |
| Comparación global | Parámetros frente al desplazamiento inicial |

### 3.7 Formulación del modelo teórico

El modelo teórico se construirá mediante la idealización de la escuadra como una viga uniforme en voladizo y del teléfono como una masa concentrada en el extremo libre. A partir de las dimensiones disponibles se calcularán el momento de inercia, la rigidez y la masa equivalente.

Debido a que el espesor no fue medido mediante un instrumento de precisión y afecta considerablemente la rigidez calculada, se desarrollarán dos representaciones:

1. **Modelo nominal:** empleará los parámetros geométricos disponibles y el espesor estimado.
2. **Modelo calibrado:** ajustará el parámetro geométrico incierto dentro de un intervalo físicamente razonable para aproximar la frecuencia experimental.

La calibración no será presentada como una medición directa, sino como un procedimiento de actualización del modelo. La diferencia entre el modelo nominal, el modelo calibrado y la respuesta experimental permitirá discutir las limitaciones de la idealización.

### 3.8 Comparación experimental y teórica

La respuesta teórica se generará para cada desplazamiento inicial empleando la frecuencia y el amortiguamiento correspondientes al modelo. Posteriormente, se comparará con la aceleración experimental seleccionada.

La evaluación incluirá:

- superposición temporal entre las respuestas experimental y teórica;
- comparación del periodo y la frecuencia;
- comparación de amplitudes y envolventes de decaimiento;
- error porcentual de los parámetros;
- índice de ajuste o métrica de error entre señales;
- análisis de sensibilidad frente al espesor, longitud efectiva y masa equivalente.

[Insertar posteriormente la gráfica de comparación experimental-teórica generada directamente desde Python.]

## Referencias preliminares verificables

Chopra, A. K. (2017). *Dynamics of structures: Theory and applications to earthquake engineering* (5th ed.). Pearson.

Clough, R. W., & Penzien, J. (2003). *Dynamics of structures* (3rd ed.). Computers & Structures.

Gallitto, A. A., & Lupo, L. (2015). A mechanical model of the smartphone's accelerometer. *Physics Education, 50*(6), 646–650. https://doi.org/10.1088/0031-9120/50/6/646

Inman, D. J. (2014). *Engineering vibration* (4th ed.). Pearson.

Monteiro, M., Cabeza, C., & Martí, A. C. (2014). Acceleration measurements using smartphone sensors: Dealing with the equivalence principle. *Revista Brasileira de Ensino de Física, 36*(1), 1303. https://doi.org/10.1590/S1806-11172014000100003

Oppenheim, A. V., & Schafer, R. W. (2010). *Discrete-time signal processing* (3rd ed.). Pearson.

Tamura, Y., Suganuma, S., & Hibi, K. (1999). Random decrement technique for damping evaluation of structures. *Journal of Wind Engineering and Industrial Aerodynamics, 83*(1–3), 137–146. https://doi.org/10.1016/S0167-6105(99)00068-5

## Secciones que se completarán después de programar

- Resultados experimentales.
- Parámetros obtenidos mediante picos, FFT, decremento logarítmico y RDT.
- Comparación entre los cinco desplazamientos iniciales.
- Comparación entre el modelo nominal, el modelo calibrado y la respuesta experimental.
- Discusión de resultados.
- Conclusiones.
- Resumen definitivo.
- Anexos de código y cálculos.
