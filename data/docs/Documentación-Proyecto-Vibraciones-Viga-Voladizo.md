## 1. DISEÑO Y CONSTRUCCIÓN DEL ESPÉCIMEN

### OBJETIVO
Construir un sistema físico simple que pueda vibrar libremente y comportarse aproximadamente como un sistema dinámico de un grado de libertad (SDOF).

### MODELO SELECCIONADO
Viga en voladizo + celular en el extremo
* [Esquema del sistema mecánico: Viga empotrada en el extremo izquierdo con longitud libre $L$, masa $m$ en el extremo libre representando el celular, y desplazamiento lateral indicado como $x(t)$].

### ¿POR QUÉ ESTE MODELO?
* Económico
* Fácil de fabricar
* Fácil de medir
* Permite registrar vibraciones con el acelerómetro del celular

### MATERIALES
| Material | Función |
| --- | --- |
| Regla metálica o lámina flexible | Actúa como viga |
| Mesa rígida | Soporte fijo |
| Prensa o tornillos | Empotramiento |
| Celular | Sensor acelerométrico |
| Cinta adhesiva | Fijación del celular |

### ESQUEMA FÍSICO DEL SISTEMA
* Empotramiento (fijación rígida)
* Viga en voladizo
* Celular (acelerómetro)
* $L$ Longitud libre

### IDEALIZACIÓN MATEMÁTICA
El sistema real se simplifica como un sistema de un grado de libertad (SDOF):
$$m\ddot{x} + c\dot{x} + kx = 0$$

Donde:
* $m =$ masa equivalente
* $c =$ amortiguamiento
* $k =$ rigidez
* $x(t) =$ desplazamiento

### RIGIDEZ DE LA VIGA
Para una viga en voladizo con carga en el extremo:
$$k = \frac{3EI}{L^3}$$

Donde:
* $E =$ módulo de elasticidad
* $I =$ momento de inercia
* $L =$ longitud libre

### MOMENTO DE INERCIA
Para sección rectangular:
$$I = \frac{bh^3}{12}$$

Donde:
* $b =$ ancho
* $h =$ espesor

### DESCRIPCIÓN FÍSICA
Cuando el extremo libre se desplaza y luego se libera:
* La viga intenta regresar a su posición original.
* Aparece una fuerza restauradora elástica.
* Se genera vibración libre amortiguada.

**Fuerza restauradora:**
$$F = -kx$$

Donde:
* $k =$ rigidez de la viga
* $x =$ desplazamiento lateral

### FIJACIÓN DEL CELULAR
El celular debe fijarse rígidamente para evitar movimientos relativos.
El celular mide:
$$a(t) = \ddot{x}(t)$$

* Aceleración instantánea
* Amplitud vibratoria
* Frecuencia natural

**FORMA CORRECTA DE FIJACIÓN:**
* Fijación rígida con cinta adhesiva resistente [Correcto]
* Fijación incorrecta: puede generar movimientos relativos [Incorrecto]

### FORMA FÍSICA DE LA VIBRACIÓN
Respuesta esperada (vibración libre amortiguada):
$$x(t) = X_0 e^{-\zeta \omega_n t} \cos(\omega_d t)$$

Donde:
* $\zeta =$ relación de amortiguamiento
* $\omega_n =$ frecuencia natural no amortiguada
* $\omega_d =$ frecuencia natural amortiguada
* [Gráfico de decaimiento temporal mostrando picos sucesivos decrecientes amortiguados en los tiempos $T_d, 2T_d, 3T_d, 4T_d, 5T_d$ entre amplitudes $X_0$ y $-X_0$].

### PARÁMETROS GEOMÉTRICOS PROPUESTOS
| Parámetro | Valor |
| --- | --- |
| Longitud libre (L) | 0.50 m |
| Ancho (b) | 0.03 m |
| Espesor (h) | 0.003 m |
| Masa del celular (m) | 0.18 kg |
| Módulo de elasticidad (E) | $2.0 \times 10^{11} \text{ Pa (acero)}$ |

### CÁLCULOS INICIALES (EJEMPLO)
* **Momento de inercia:**
  $$I = \frac{bh^3}{12}$$
  $$I = \frac{0.03(0.003)^3}{12} = 6.75 \times 10^{-11} \text{ m}^4$$

* **Rigidez de la viga:**
  $$k = \frac{3EI}{L^3}$$
  $$k = \frac{3(2 \times 10^{11})(6.75 \times 10^{-11})}{(0.50)^3} = 324 \text{ N/m}$$

* **Frecuencia natural teórica:**
  $$f_n = \frac{1}{2\pi}\sqrt{\frac{k}{m}}$$
  $$f_n = \frac{1}{2\pi}\sqrt{\frac{324}{0.18}} = 6.75 \text{ Hz}$$

### INTERPRETACIÓN FÍSICA
* Si aumenta $E \rightarrow$ la viga es más rígida.
* Si aumenta $h \rightarrow$ aumenta mucho la rigidez.
* Si aumenta $L \rightarrow$ disminuye la rigidez.
* Vigas largas vibran más lento.
* Vigas rígidas vibran más rápido.
* Mayor masa $\rightarrow$ menor frecuencia.

### CONCLUSIÓN DEL DISEÑO
El espécimen construido representa adecuadamente un sistema SDOF. Permite medir vibraciones reales y obtener:
* Frecuencia natural
* Período natural
* Amortiguamiento
* Respuesta dinámica

Será utilizado para los ensayos experimentales y el procesamiento posterior.

---

## 2. EJECUCIÓN DEL ENSAYO

**VIBRACIÓN LIBRE DEL ESPÉCIMEN: VIGA EN VOLADIZO CON CELULAR**

### OBJETIVO
Inducir una vibración libre al espécimen, registrar varias series de respuestas dinámicas con el acelerómetro del celular y realizar un mínimo de 5 ensayos repetidos para validar la consistencia de resultados (cada ensayo con al menos 3 vibraciones libres).

### 2.1. INDUCCIÓN DE LA VIBRACIÓN LIBRE
1. **DESPLAZAMIENTO INICIAL:** Desplazar el extremo libre de la viga lateralmente una distancia conocida ($x_0$).
2. **LIBERACIÓN:** Soltar suavemente el extremo libre sin impartir velocidad inicial.
3. **VIBRACIÓN LIBRE:** La viga vibra libremente en torno a su posición de equilibrio.

*Nota:* La respuesta esperada es una vibración libre amortiguada, que disminuye su amplitud con el tiempo debido al amortiguamiento del sistema.

### 2.2. REGISTRO DE LA RESPUESTA DINÁMICA
Se utiliza el acelerómetro del celular para registrar la aceleración en el eje vertical (eje y).
1. **Aplicación recomendada:** *Phyphox*, *Physics Toolbox Sensor Suite* o similar.
2. **Frecuencia de muestreo sugerida:** $\ge 100 \text{ Hz}$ (recomendado $200 \text{ Hz}$).
3. **Duración de registro:** $\ge 10 \text{ segundos}$ (al menos 3 ciclos completos).
4. Colocar el celular firmemente sujeto al extremo libre de la viga.
5. Iniciar el registro ANTES de liberar la viga.

**SEÑAL ESPERADA (ACELERACIÓN vs TIEMPO):**
* [Gráfico de curvas sinusoidales decrecientes limitadas por una envolvente exponencial amortiguada].
* *Nota en gráfico:* La amplitud disminuye exponencialmente con el tiempo.

### 2.3. REPETICIÓN DE ENSAYOS
Realizar un mínimo de 5 ensayos repetidos en condiciones similares para verificar la consistencia de los resultados.

| Ensayo | Desplazamiento inicial ($x_0$) | Número mínimo de vibraciones libres | Duración mínima de registro | Observaciones |
| --- | --- | --- | --- | --- |
| 1 | 2.0 cm | $\ge 3 \text{ ciclos}$ | $\ge 10 \text{ s}$ | — |
| 2 | 2.2 cm | $\ge 3 \text{ ciclos}$ | $\ge 10 \text{ s}$ | — |
| 3 | 1.8 cm | $\ge 3 \text{ ciclos}$ | $\ge 10 \text{ s}$ | — |
| 4 | 2.1 cm | $\ge 3 \text{ ciclos}$ | $\ge 10 \text{ s}$ | — |
| 5 | 2.0 cm | $\ge 3 \text{ ciclos}$ | $\ge 10 \text{ s}$ | — |

**CONDICIONES IMPORTANTES:**
* Mantener la misma posición del celular.
* Asegurar la misma rigidez en el empotramiento.
* No aplicar empujones adicionales al soltar.
* Realizar los ensayos en el mismo entorno (temperatura, superficie, etc.).
* Esperar unos segundos entre ensayos.

**ERROR COMÚN A EVITAR:**
* No soltar la viga suavemente o empujarla al liberar, ya que se introduce energía adicional y la respuesta no será de vibración libre pura.

### 2.4. MONTAJE EXPERIMENTAL
* Empotramiento (fijación rígida) $\rightarrow$ Viga en voladizo $\rightarrow$ Celular (acelerómetro) en el extremo libre.
* $L =$ Longitud libre de la viga.

### 2.5. RESUMEN DEL PROCEDIMIENTO
1. Abrir aplicación del acelerómetro y configurar.
2. Desplazar lateralmente el extremo libre ($x_0$).
3. Soltar suavemente la viga.
4. Registrar la respuesta hasta que se extinga.
5. Repetir el ensayo al menos 5 veces en total.

**Resultado esperado:** Series de señales de aceleración en el tiempo para cada ensayo, con al menos 3 vibraciones libres por ensayo, listas para su procesamiento (filtros, cálculo de periodo y amortiguamiento).

---

## 3. PROCESAMIENTO DE DATOS

### OBJETIVO
Aplicar filtros y representar las señales en el dominio del tiempo y de la frecuencia. Determinar el periodo natural y el amortiguamiento mediante el método del decremento logarítmico y la Random Decrement Technique (RDT).

### 3.1. SEÑAL EN EL DOMINIO DEL TIEMPO
Señal cruda registrada con el acelerómetro del celular.
* [Gráfico de aceleración $a \text{ (m/s}^2\text{)}$ vs tiempo $t \text{ (s)}$ que muestra una oscilación amortiguada con ligeras irregularidades por ruido de fondo].
* **Observación:** La señal corresponde a una vibración libre amortiguada. Su amplitud disminuye con el tiempo debido al amortiguamiento del sistema.

### 3.2. FILTRADO DE LA SEÑAL
Se aplica un filtro pasa-banda para eliminar ruido y componentes indeseadas.
* **Señal cruda (con ruido)** $\rightarrow$ [Proceso de filtrado] $\rightarrow$ **Señal filtrada (pasa-banda)**
* *Efecto:* El filtrado permite obtener una señal más limpia, mejorando la identificación de picos, periodos y parámetros dinámicos.

### 3.3. DETERMINACIÓN DEL PERIODO NATURAL
Se identifican los picos positivos consecutivos de la señal filtrada.
* [Gráfico de picos numerados correlativamente del 1 al 7].

**Tiempos de los picos (ejemplo):**
| Pico (i) | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tiempo $t_i \text{ (s)}$ | 0.50 | 1.98 | 3.46 | 4.94 | 6.42 | 7.90 | 9.38 |

* **Periodo amortiguado (promedio):**
  $$T_d = \frac{1}{n-1}\sum_{i=1}^{n-1}(t_{i+1} - t_i)$$

* **Frecuencia amortiguada:**
  $$f_d = \frac{1}{T_d}$$

* **Frecuencia angular amortiguada:**
  $$\omega_d = 2\pi f_d$$

### 3.4. DETERMINACIÓN DEL AMORTIGUAMIENTO - MÉTODO DEL DECREMENTO LOGARÍTMICO
Picos positivos de la señal filtrada: $A_1, A_2, A_3, A_4, \dots, A_n, A_{n+1}$

* **Decremento logarítmico:**
  $$\delta = \frac{1}{n} \ln\left(\frac{A_1}{A_{n+1}}\right)$$

* **Relación de amortiguamiento:**
  $$\zeta = \frac{\delta}{\sqrt{4\pi^2 + \delta^2}}$$

Donde:
* $A_1 =$ primer pico
* $A_{n+1} =$ pico $n+1$
* $n =$ número de ciclos

**Ejemplo numérico:**
* $A_1 = 5.20 \text{ m/s}^2$
* $A_6 = 1.35 \text{ m/s}^2$
* $n = 5$
$$\delta = \frac{1}{5} \ln\left(\frac{5.20}{1.35}\right) = 0.226$$
$$\zeta = \frac{0.226}{\sqrt{4\pi^2 + 0.226^2}} = 0.0358 \text{ (3.58\%)} $$

### 3.5. ANÁLISIS EN EL DOMINIO DE LA FRECUENCIA (FFT)
Transformada Rápida de Fourier de la señal filtrada.
* [Gráfico de Amplitud $\text{(m/s}^2\text{)}$ vs Frecuencia $\text{(Hz)}$ que presenta un pico nítido y aislado].
* **Pico principal (frecuencia dominante):** $f_{FFT} = 6.62 \text{ Hz}$
* *Nota:* El pico principal del espectro indica la frecuencia dominante del sistema, que debe ser cercana a la frecuencia natural estimada.

### 3.6. ESTIMACIÓN POR RANDOM DECREMENT TECHNIQUE (RDT)
**Procedimiento:**
1. Seleccionar múltiples puntos de cruce por cero con pendiente positiva.
2. Extraer segmentos de la señal alrededor de cada punto.
3. Promediar los segmentos.
4. Obtener la función de decrecimiento promedio.

* **Función de decrecimiento obtenue (RDT):**
  [Gráfico limpio de decaimiento armónico estabilizado mediante promediado estadístico]
* *Nota:* A partir de esta función se estiman $T_d$ y $\zeta$ usando el mismo procedimiento del decremento logarítmico.

### 3.7. RESUMEN DE PARÁMETROS OBTENIDOS (EJEMPLO)
| Parámetro | Símbolo | Valor obtenido (ejemplo) | Unidad | Método |
| --- | --- | --- | --- | --- |
| Periodo amortiguado | $T_d$ | 0.151 | s | Picos de la señal filtrada |
| Frecuencia amortiguada | $f_d$ | 6.62 | Hz | $1 / T_d$ |
| Frecuencia angular amortiguada | $\omega_d$ | 41.62 | rad/s | $2\pi f_d$ |
| Amortiguamiento | $\zeta$ | 0.0358 (3.58%) | — | Decremento logarítmico |
| Frecuencia dominante (FFT) | $f_{FFT}$ | 6.62 | Hz | Transformada de Fourier |
| Amortiguamiento (RDT) | $\zeta_{RDT}$ | 0.0345 (3.45%) | — | Random Decrement Technique |

**Nota:** Es importante realizar el mismo procesamiento para cada uno de los ensayos y luego obtener el promedio para validar la consistencia y repetibilidad de los resultados.

**CONCLUSIÓN DEL PROCESAMIENTO:**
Los métodos aplicados permiten determinar de manera confiable el periodo natural, la frecuencia natural y el amortiguamiento del sistema a partir de la respuesta medida con el acelerómetro del celular.

**SOFTWARE RECOMENDADO:**
Phyphox, Excel, MATLAB, Python (Pandas, NumPy, SciPy, Matplotlib)

---

## 4. MODELADO MATEMÁTICA

### OBJETIVO
Proponer un modelo simplificado de un grado de libertad (SDOF) que represente la dinámica del espécimen y comparar las curvas experimentales con la respuesta teórica obtenida mediante el modelo.

### 4.1. IDEALIZACIÓN DEL SISTEMA
* **Sistema físico real:** Viga en voladizo con celular en el extremo (sensor acelerométrico y masa adicional).
* **Modelo idealizado (SDOF):** [Representación equivalente compuesta por un bloque de masa $m$, acoplado en paralelo a un resorte de rigidez $k$ y a un amortiguador de coeficiente $c$, con coordenada de desplazamiento lateral $x(t)$].

### 4.2. ECUACIÓN DE MOVIMIENTO (SDOF)
Para vibración libre amortiguada:
$$m\ddot{x} + c\dot{x} + kx = 0$$

**Parámetros dinámicos:**
* **Frecuencia natural no amortiguada:**
  $$\omega_n = \sqrt{\frac{k}{m}}$$
* **Frecuencia natural (Hz):**
  $$f_n = \frac{\omega_n}{2\pi}$$
* **Relación de amortiguamiento:**
  $$\zeta = \frac{c}{2m\omega_n}$$
* **Frecuencia amortiguada:**
  $$\omega_d = \omega_n \sqrt{1 - \zeta^2}$$
  $$f_d = \frac{\omega_d}{2\pi}$$

### 4.3. CÁLCULO DE PARÁMETROS DEL MODELO
* **Rigidez equivalente de la viga en voladizo:** Para una carga en el extremo libre:
  $$k = \frac{3EI}{L^3}$$
  Donde:
  * $E =$ módulo de elasticidad del material
  * $I =$ momento de inercia de la sección
  * $L =$ longitud libre de la viga

* **Momento de inercia (sección rectangular):**
  $$I = \frac{bh^3}{12}$$

* **Masa equivalente del sistema:**
  $$m_{eq} = m_{celular} + \alpha m_{viga}$$
  Donde $\alpha \approx 0.236$ para el primer modo de una viga en voladizo.

### 4.4. RESPUESTA TEÓRICA DEL MODELO
* **Respuesta en desplazamiento (vibración libre amortiguada):**
  $$x(t) = X_0 e^{-\zeta \omega_n t} \cos(\omega_d t)$$

* **Respuesta en aceleración (medida por el celular):**
  $$a(t) = \ddot{x}(t) = -X_0 \omega_n^2 e^{-\zeta \omega_n t} \left[ \cos(\omega_d t) + \frac{\zeta}{\sqrt{1 - \zeta^2}} \sin(\omega_d t) \right]$$
* *Nota en gráfico:* La amplitud disminuye exponencialmente con el tiempo debido al amortiguamiento.

### 4.5. PROCEDIMIENTO DE MODELADO
1. Obtener dimensiones geométricas de la viga ($L, b, h$). $\rightarrow$ *Datos geométricos y material*
2. Conocer propiedades del material ($E$). $\rightarrow$ *Cálculo de $I$ y $k$*
3. Calcular $I$ y luego la rigidez equivalente $k$. $\rightarrow$ *Cálculo de $m_{eq}$*
4. Estimar la masa equivalente $m_{eq}$. $\rightarrow$ *Obtención de $\omega_n, f_n, \zeta$*
5. Calcular $\omega_n, f_n$ y $\zeta$ usando los parámetros experimentales. $\rightarrow$ *Respuesta teórica $a(t)$*
6. Generar la respuesta teórica $a(t)$ del modelo. $\rightarrow$ *Comparación con datos experimentales*
7. Comparar con la respuesta experimental medida por el acelerómetro.

### 4.6. EJEMPLO NUMÉRICO
* $L = 0.50 \text{ m}$
* $b = 0.03 \text{ m}$
* $h = 0.003 \text{ m}$
* $E = 2.0 \times 10^{11} \text{ Pa (acero)}$
* $m_{celular} = 0.18 \text{ kg}$
* $m_{viga} = 0.10 \text{ kg (aprox.)}$
* $\alpha = 0.236$

1. **Momento de inercia:**
   $$I = \frac{bh^3}{12} = \frac{0.03(0.003)^3}{12} = 6.75 \times 10^{-11} \text{ m}^4$$

2. **Rigidez equivalente:**
   $$k = \frac{3EI}{L^3} = \frac{3(2 \times 10^{11})(6.75 \times 10^{-11})}{(0.50)^3} = 324 \text{ N/m}$$

3. **Masa equivalente:**
   $$m_{eq} = 0.18 + 0.236(0.10) = 0.2036 \text{ kg}$$

4. **Frecuencia natural:**
   $$\omega_n = \sqrt{\frac{k}{m_{eq}}} = \sqrt{\frac{324}{0.2036}} = 39.90 \text{ rad/s}$$
   $$f_n = \frac{\omega_n}{2\pi} = \frac{39.90}{2\pi} = 6.35 \text{ Hz}$$

### 4.7. COMPARACIÓN ENTRE RESPUESTA EXPERIMENTAL Y TEÓRICA
* **Ejemplo de comparación (aceleración vs tiempo):** Superposición de las curvas *Experimental (celular)* [línea azul continua] y *Teórica (modelo SDOF)* [línea roja segmentada].

**Comparación de parámetros:**
| Parámetro | Experimental | Teórico (modelo) | Error (%) |
| --- | --- | --- | --- |
| Periodo amortiguado $T_d \text{ (s)}$ | 0.153 | 0.157 | 2.61 |
| Frecuencia amortiguada $f_d \text{ (Hz)}$ | 6.54 | 6.37 | 2.67 |
| Frecuencia natural $f_n \text{ (Hz)}$ | 6.70 | 6.35 | 5.22 |
| Amortiguamiento $\zeta \text{ (\%)}$ | 3.60 | 3.50 | 2.78 |

* **Índice de ajuste (correlación):** Coeficiente de correlación entre señales: $R = 0.96$
* *Conclusión:* El modelo SDOF representa adecuadamente el comportamiento dinámico del espécimen.

### 4.8. CONCLUSIÓN DEL MODELADO
El modelo simplificado de un grado de libertad (SDOF) describe de forma adecuada la dinámica de la viga en voladizo con el celular en el extremo. Los parámetros estimados permiten reproducir con buena aproximación la respuesta experimental obtenida con el acelerómetro del celular.

**SUPUESTOS DEL MODELO:**
* La viga se comporta linealmente (rango elástico).
* El primer modo de vibración domina la respuesta.
* Amortiguamiento viscoso proporcional.
* La masa del celular se considera concentrada en el extremo libre.
* La unión en el empotramiento es suficientemente rígida.

---

## 5. ELABORACIÓN DEL REPORTE

### OBJETIVO
Presentar un documento técnico con formato de artículo científico (APA, 6–12 páginas, doble columna) que incluya todas las secciones requeridas, con los resultados del ensayo, procesamiento de datos y modelado matemático.

### 5.1. FORMATO GENERAL DEL DOCUMENTO
* **Formato:** Artículo científico APA (6 a 12 páginas, doble columna)
* **Fuente recomendada:** Times New Roman o Arial
* **Tamaño de fuente:** 10 a 11 pt
* **Interlineado:** 1.5
* **Márgenes:** 2.54 cm en todos los lados
* **Alineación:** Justificada
* **Columnas:** 2
* **Numeración de páginas:** inferior centrado
* **Figuras y tablas:** numeradas y con título (APA)
* **Citas y referencias:** Norma APA (7ª edición)

### 5.2. ESTRUCTURA DEL REPORTE
El artículo debe contener las siguientes secciones:
1. **Resumen y palabras clave:** Resumen de 150–250 palabras y 3–5 palabras clave.
2. **Introducción:** Presenta el problema, objetivo y justificación del estudio.
3. **Marco teórico:** Fundamentos de vibración, SDOF, amortiguamiento, decremento logarítmico y RDT.
4. **Metodología experimental:** Descripción del espécimen, instrumento, procedimiento del ensayo y adquisición de datos.
5. **Resultados:** Presentación de datos en tablas, gráficos y valores obtenidos.
6. **Discusión:** Interpretación de resultados y comparación con el modelo teórico.
7. **Conclusiones:** Principales hallazgos que responden a los objetivos.
8. **Referencias bibliográficas:** Citas y referencias en formato APA (7ª edición).
9. **Anexos:** Registros completos, hojas de cálculo, código, fotos adicionales, etc.
10. **Agradecimientos (opcional):** Reconocer apoyo institucional o personal.

### 5.3. CONTENIDO SUGERIDO POR SECCIÓN
| Sección | Contenido sugerido |
| --- | --- |
| Resumen | Breve descripción del problema, método, resultados principales y conclusión. |
| Introducción | Antecedentes, importancia del tema, planteamiento del problema, objetivo general y objetivos específicos. |
| Marco teórico | Conceptos de vibración libre, SDOF, frecuencia natural, amortiguamiento, decremento logarítmico y RDT. |
| Metodología | Descripción del espécimen, materiales, sensor, montaje, procedimiento del ensayo y procesamiento de datos. |
| Resultados | Tablas, gráficos (tiempo, frecuencia), parámetros obtenidos, comparación experimental-teórica. |
| Discusión | Análisis de resultados, fuentes de error, comparación con otros estudios o con el modelo matemático. |
| Conclusiones | Cumplimiento de objetivos y respuesta a la pregunta de investigación. |
| Referencias | Todas las fuentes utilizadas en formato APA 7ª edición. |
| Anexos | Datos crudos, hojas de cálculo, código, fotos, videos, etc. |

### 5.4. EJEMPLO DE FIGURAS Y TABLAS A INCLUIR
* **Figura: Respuesta en el dominio del tiempo** [Gráfico de aceleración $a \text{ (m/s}^2\text{)}$ vs tiempo $t \text{ (s)}$].
* **Figura: Espectro de frecuencia (FFT)** [Gráfico de Amplitud vs Frecuencia con una línea indicativa de la frecuencia natural en $f_n = 6.62 \text{ Hz}$].
* **Tabla: Parámetros dinámicos obtenidos**

| Parámetro | Símbolo | Valor | Unidad | Método |
| --- | --- | --- | --- | --- |
| Periodo amortiguado | $T_d$ | 0.151 | s | Picos filtrados |
| Frecuencia amortiguada | $f_d$ | 6.62 | Hz | $1 / T_d$ |
| Frecuencia natural | $f_n$ | 6.70 | Hz | Modelo / RDT |
| Amortiguamiento | $\zeta$ | 0.0358 | — | Decremento log. |
| Amortiguamiento (RDT) | $\zeta_{RDT}$ | 0.0345 | — | RDT |

### 5.5. NORMAS APA (7ª EDICIÓN) – RESUMEN
* Citas en el texto: (Autor, año).
* Cita con dos autores: (Autor & Autor, año).
* Más de dos autores: (Autor et al., año).
* Referencias al final en orden alfabético.
* Formato: Autor. (Año). Título. Editorial.
* Figuras y tablas: numeración en arábigos y título en la parte superior (APA).

**EJEMPLO DE REFERENCIA:**
Clough, R. W., & Penzien, J. (2003). *Dynamics of structures* (3rd ed.). McGraw-Hill.

### 5.6. CONSEJOS PARA UN BUEN REPORTE
* Redactar con claridad, precisión y en tercera persona.
* Usar figuras y tablas de alta calidad y bien etiquetadas.
* Explicar todos los procedimientos y supuestos del modelo.
* Comparar siempre los resultados experimentales con los teóricos.
* Discutir fuentes de error y limitaciones del estudio.
* Revisar ortografía, gramática y formato antes de entregar.

### 5.7. ENTREGA DEL REPORTE
* Documento en PDF
* Figuras y tablas numeradas
* Referencias en formato APA
* Anexos (datos, códigos, fotos, etc.)
* Revisión y verificación final

**RECORDAR:** Un buen reporte no solo presenta datos, sino que cuenta una historia científica completa, coherente y verificable.

---

## 6. EVIDENCIAS

### OBJETIVO
Presentar evidencias fotográficas y en video de los ensayos realizados con la identificación correspondiente.

### 6.1. EVIDENCIAS FOTOGRÁFICAS DEL ENSAYO
1. **Montaje experimental:** Vista general del espécimen: viga en voladizo con el celular (acelerómetro) en el extremo.
2. **Detalle de fijación del celular:** El celular se fija firmemente para evitar movimientos relativos.
3. **Desplazamiento inicial:** Se aplica un desplazamiento lateral inicial ($x_0$).
4. **Liberación:** Se libera suavemente sin impartir velocidad inicial.
5. **Vibración libre:** La viga vibra libremente en torno a su posición de equilibrio.
6. **Registro de datos:** Se registra la aceleración en el eje vertical (eje y) con la aplicación del acelerómetro.
7. **Repetición del ensayo:** Se repite el procedimiento para obtener al menos 5 ensayos.
8. **Condiciones del entorno:** Se mantienen condiciones similares en todos los ensayos:
   * Temperatura: $24 \text{ °C}$
   * Superficie rígida
   * Sin viento apreciable

### 6.2. EVIDENCIAS EN VIDEO DEL ENSAYO
Se graba cada ensayo en video para documentar el procedimiento y el comportamiento dinámico del espécimen.
* Archivos correspondientes: **Ensayo 1, Ensayo 2, Ensayo 3, Ensayo 4, Ensayo 5**.
* *Requisito:* Los videos deben mostrar: montaje, desplazamiento inicial, liberación, vibración libre y registro con el acelerómetro.

### 6.3. IDENTIFICACIÓN DE LOS ENSAYOS
Cada archivo (foto o video) debe estar identificado con la siguiente información:
* Código del ensayo (Ej.: E01, E02, ..., E05)
* Fecha y hora
* Descripción breve del ensayo
* Responsable
* Condiciones del entorno

**Ejemplo de identificación:**
* **Código:** E03
* **Fecha:** 15/05/2024
* **Hora:** 10:35 a.m.
* **Descripción:** Vibración libre viga en voladizo
* **Responsable:** Grupo 1
* **Condiciones:** $24 \text{ °C}$, sin viento, superficie rígida

### 6.4. EVIDENCIAS DE RESULTADOS OBTENIDOS
* **Señal en el dominio del tiempo:** Registro típico de aceleración medida con el celular.
* **Espectro de frecuencia (FFT):** Frecuencia dominante identificada en el espectro ($f_n = 6.62 \text{ Hz}$).

### 6.5. ALMACENAMIENTO Y RESPALDO DE EVIDENCIAS
1. **Organizar** todos los archivos (fotos, videos y datos) en carpetas por ensayo.
2. **Realizar respaldo** en la nube o en un dispositivo externo.
3. **Verificar** que todos los archivos estén completos y correctamente identificados.
4. **Conservar** las evidencias hasta la entrega final del reporte.

**IMPORTANTE:**
* Asegurar buena iluminación en las fotos.
* Grabar videos estables y claros.
* No editar ni recortar la información registrada.
* Las evidencias deben ser verídicas y originales.

*Nota conclusiva:* Las evidencias presentadas deben permitir verificar la correcta realización del ensayo y respaldar los resultados reportados en el documento técnico.