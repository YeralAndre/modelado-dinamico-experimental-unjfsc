# Ficha maestra para el artículo científico

## Identificación

- **Título de trabajo:** Identificación experimental de parámetros dinámicos en un sistema de un grado de libertad utilizando acelerómetros móviles.
- **Autores:** Yeral Reyes Solis, Deyvid Borja Chiroque y Robert Vasquez Altunas.
- **Institución:** Universidad Nacional José Faustino Sánchez Carrión (UNJFSC).
- **Curso:** Ecuaciones Diferenciales.
- **Docente:** GOÑY AMERI Carlos Francisco.
- **Lugar y año:** Huacho, Perú, 2026.

## Datos físicos confirmados

- **Sistema:** Regla metálica en voladizo con un celular fijado en el extremo libre.
- **Material de la regla:** Acero de alta resistencia.
- **Longitud libre:** 20 cm (0.20 m).
- **Ancho de la regla:** 3.8 cm (0.038 m).
- **Espesor de la regla:** 1 mm (0.001 m).
- **Celular:** Redmi Note 14 Pro+ 5G.
- **Masa medida del celular:** 0.210 kg.
- **Masa aproximada de la escuadra completa:** entre 0.300 y 0.350 kg.
- **Instrumento de adquisición:** Acelerómetro del celular mediante Sensor Logger.
- **Eje principal analizado:** Eje Z, correspondiente a la dirección dominante del movimiento.
- **Desplazamientos iniciales:** 1.0, 1.5, 2.0, 2.5 y 3.0 cm.
- **Liberaciones registradas:** Tres por cada desplazamiento inicial.
- **Ventana de análisis:** Una liberación representativa de aproximadamente 10 a 12 s por desplazamiento.

## Datos que deben tratarse como estimaciones

- El avance no registra una masa medida de la regla.
- La masa aproximada de 0.300 a 0.350 kg corresponde a la escuadra completa y no debe utilizarse directamente como masa del tramo libre vibrante.
- Para el modelo puede estimarse la masa del tramo libre mediante `m = rho * b * h * L`, indicando expresamente la densidad de acero adoptada.
- El módulo de elasticidad usado en el avance es un valor teórico para acero de `E = 2.0 x 10^11 Pa`.
- El espesor se estima visualmente cercano a 2 mm, pero no ha sido medido con vernier. Con `h = 2 mm` y `L = 20 cm`, el modelo ideal predice aproximadamente 14.22 Hz, valor muy superior a la frecuencia experimental cercana a 7.22 Hz.
- Al calibrar únicamente el espesor para reproducir la frecuencia experimental, manteniendo los demás parámetros nominales, se obtiene un espesor equivalente aproximado de 1.25 mm. El artículo debe presentar este resultado como una calibración o análisis de sensibilidad, no como una medición física.
- La masa adicional de cinta se considera despreciable y el celular fue utilizado sin funda.
- La liberación seleccionada no está fijada en el avance. Debe elegirse con un criterio reproducible: señal completa, ausencia de manipulación, decaimiento limpio y amplitud inicial representativa.
- La frecuencia de adquisición configurada y la frecuencia efectiva observada deben distinguirse al redactar la metodología.

## Fotografías extraídas y pies sugeridos

### Figuras recomendadas para el cuerpo principal

**01_montaje_prensa_regla.jpg**

Figura. Montaje de referencia del sistema experimental compuesto por una regla metálica empotrada mediante una prensa y un dispositivo móvil ubicado en el extremo libre.

**03_registro_sensor_logger.jpg**

Figura. Visualización de la respuesta acelerométrica registrada mediante la aplicación Sensor Logger durante la demostración del ensayo de vibración libre.

**04_ensayo_1_5cm_preparacion.jpg**

Figura. Preparación del montaje experimental para el ensayo correspondiente a un desplazamiento inicial de 1.5 cm.

**05_ensayo_1_5cm_vibracion.jpg**

Figura. Ejecución del ensayo de vibración libre con el dispositivo móvil fijado al extremo de la regla metálica.

**06_comparacion_grafica_python.jpg**

Figura. Revisión de la comparación gráfica entre respuestas dinámicas durante la etapa de procesamiento computacional.

### Figuras auxiliares u opcionales

**02_explicacion_desplazamientos.jpg**

Figura. Revisión de las indicaciones para la aplicación controlada de desplazamientos iniciales durante los ensayos.

Nota: la imagen presenta baja nitidez y se recomienda reemplazarla si existe una fotografía original del procedimiento.

**07_modelo_y_resultados_referencia.jpg**

Figura. Revisión de una estructura de referencia para la presentación del modelo matemático y los resultados experimentales.

Nota: utilizar únicamente como evidencia de trabajo o anexo, no como resultado científico propio.

**08_revision_procesamiento_opcional.jpg**

Figura. Revisión preliminar del procesamiento computacional de una señal dinámica.

Nota: la imagen presenta baja nitidez y debe sustituirse por las gráficas finales exportadas directamente desde Python.

**09_escuadra_metalica_acero.png**

Figura. Escuadra metálica de acero empleada como elemento flexible del montaje experimental.

Nota: la fotografía permite identificar la geometría general y las escalas de la escuadra, pero no permite determinar su espesor con precisión.

## Criterio recomendado para las figuras finales

Las fotografías documentan el procedimiento, pero las gráficas científicas del artículo deben exportarse directamente desde Python. No se deben utilizar fotografías de pantallas como sustituto de las figuras de resultados.
