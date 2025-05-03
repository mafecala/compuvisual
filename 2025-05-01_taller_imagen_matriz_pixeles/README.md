# 🧪 De Pixels a Coordenadas: Explorando la Imagen como Matriz

## [](#-fecha)📅 Fecha

`2025-05-01`

----------

## [](#-objetivo-del-taller)🎯 Objetivo del Taller

Este taller tiene como objetivo explorar y comprender el procesamiento de imágenes digitales como matrices de píxeles utilizando OpenCV, NumPy y Matplotlib en Google Colab. Se busca demostrar cómo manipular las imágenes a nivel de píxel, visualizar sus componentes de color, realizar transformaciones básicas y aplicar ajustes interactivos en tiempo real.

----------

## [](#-conceptos-aprendidos)🧠 Conceptos Aprendidos


-   Representación matricial de imágenes digitales (RGB, HSV)
-   Manipulación directa de regiones de píxeles mediante slicing de matrices
-   Análisis de distribución de intensidades mediante histogramas
-   Transformaciones de brillo y contraste
-   Visualización interactiva con widgets
-   Segmentación básica de imágenes por regiones
----------

## [](#-herramientas-y-entornos)🔧 Herramientas y Entornos

-   Google Colab
- Python



----------

## [](#-estructura-del-proyecto)📁 Estructura del Proyecto

2025-05-01_taller_segmentacion_formas
├── python/
├── README.md



## 🧪 Implementación

### 🔹 Etapas realizadas

1.  **Preparación y carga de datos**: Carga de imagen desde sistema local o generación de muestra.
2.  **Análisis de canales de color**: Separación y visualización de canales RGB y HSV.
3.  **Manipulación de regiones**: Modificación de áreas específicas y clonación de regiones.
4.  **Análisis de histograma**: Cálculo y visualización de distribución de intensidades por canal.
5.  **Transformaciones de intensidad**: Ajustes de brillo y contraste con diferentes parámetros.
6.  **Interacción en tiempo real**: Implementación de controles interactivos para modificación dinámica.

### 🔹 Código relevante

python

```python
# Separar canales RGB
r, g, b = cv2.split(imagen_rgb)

# Crear visualizaciones para cada canal de color
zeros = np.zeros_like(r)
canal_r = cv2.merge([r, zeros, zeros])
canal_g = cv2.merge([zeros, g, zeros])
canal_b = cv2.merge([zeros, zeros, b])

# Modificar una región específica usando slicing
imagen_mod1[y1:y2, x1:x2, 0] = 255  # Canal R
imagen_mod1[y1:y2, x1:x2, 1] = 50   # Canal G
imagen_mod1[y1:y2, x1:x2, 2] = 50   # Canal B

# Calcular histograma usando OpenCV
hist = cv2.calcHist([canal], [0], None, [256], [0, 256])

# Ajustar brillo y contraste
imagen_ajustada = cv2.convertScaleAbs(imagen, alpha=alfa, beta=beta)

# Interfaz interactiva para ajustes en tiempo real
interact(
    aplicar_ajustes,
    contraste=FloatSlider(min=0.1, max=3.0, step=0.1, value=1.0),
    brillo=IntSlider(min=-100, max=100, step=5, value=0)
)
```
----------

## [](#-resultados-visuales)📊 Resultados Visuales
Estas son solamente algunas de las imágenes, para verlas todas y poder experimentar con los sliders, por favor visita el notebook en https://colab.research.google.com/drive/1pylXulXqbt69sstMnNEdj0Ux_vo4pD5E?usp=sharing

![demo](demo.png)
----------

## [](#-prompts-usados)🧩 Prompts Usados


Modelo Generativo Claude 3.7 Sonnet :
```
Genera un script en Python (compatible con Google Colab) que utilice OpenCV, NumPy y Matplotlib para explorar una imagen como matriz de píxeles. El código debe:
Cargar una imagen a color usando cv2.imread() y mostrarla.
Separar y visualizar por separado los canales RGB y HSV.
Usar slicing de matrices para modificar regiones específicas de la imagen:
Cambiar el color de un área rectangular.
Copiar una región de la imagen y pegarla en otra posición.
Calcular y visualizar el histograma de intensidades (por canal si es posible) usando cv2.calcHist() o matplotlib.pyplot.hist().
Ajustar brillo y contraste de forma manual (usando una fórmula) y también con cv2.convertScaleAbs().
Incluir una interfaz interactiva con sliders usando cv2.createTrackbar() para modificar el brillo y el contraste en tiempo real.
Muestra los resultados con matplotlib.pyplot.imshow() para facilitar la visualización dentro del notebook.

```

Modelo Generativo: GPT-4o
```

Genera un documento en formato Markdown describiendo un taller de procesamiento de imágenes con OpenCV en Python. El taller debe enfocarse en segmentación binaria, detección de contornos y análisis geométrico de objetos, enseñando a usar Python y OpenCV para procesar imágenes, aplicar segmentación binaria, detectar contornos y calcular propiedades geométricas como centroides, áreas y perímetros.

El documento debe incluir un objetivo claro del taller, describiendo brevemente el propósito del mismo. También debe cubrir los conceptos aprendidos, como segmentación mediante umbralización, detección de contornos, cálculo de propiedades geométricas y visualización de resultados. La sección de implementación debe incluir las etapas realizadas, como la carga de la imagen, la segmentación binaria, la detección de contornos y el cálculo de propiedades geométricas. Además, debe incluir un bloque de código funcional que realice la conversión a escala de grises, la segmentación binaria, la detección de contornos y el cálculo de centroides, áreas y perímetros, con visualización de resultados usando Matplotlib.

El taller debe concluir con una reflexión final sobre las técnicas aprendidas, destacando lo más útil o interesante, además de proponer posibles mejoras futuras. Finalmente, debe incluir instrucciones para reproducir el proyecto en Google Colab, especificando cómo instalar las dependencias necesarias, cargar imágenes y ejecutar el código paso a paso


```
----------


## 💬 Reflexión Final



Este taller me permitió comprender a fondo cómo las imágenes digitales son realmente matrices multidimensionales que pueden manipularse matemáticamente. Reforcé conceptos fundamentales del procesamiento digital de imágenes como la separación de canales de color, el análisis de histogramas y la manipulación directa de regiones de píxeles. La conexión entre la teoría matemática y la aplicación práctica mediante bibliotecas como OpenCV y NumPy resulta fascinante.

La parte más compleja e interesante fue la implementación de la interfaz interactiva para ajustar brillo y contraste en tiempo real, ya que requiere comprender cómo los widgets interactivos se integran con el flujo de procesamiento de imágenes. También resultó interesante el análisis de histogramas bidimensionales para comprender la distribución conjunta de los canales de color, proporcionando una visión más profunda de la composición de la imagen.

Para futuros proyectos, me interesaría expandir este conocimiento hacia técnicas más avanzadas como la segmentación automática basada en color, la detección de bordes y características, y la aplicación de filtros de convolución personalizados. También sería valioso integrar estas técnicas con métodos de aprendizaje automático para análisis y reconocimiento de patrones en imágenes.
