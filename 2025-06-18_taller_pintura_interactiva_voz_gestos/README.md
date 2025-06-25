# 🎨 Pintura Interactiva: Control por Voz y Gestos

## 📅 Fecha
2025-06-23 

---

## 🎯 Objetivo del Taller

Desarrollar una aplicación interactiva que permita crear arte digital mediante el control por gestos y comandos de voz, eliminando la necesidad de interfaces tradicionales como mouse y teclado. Este proyecto explora la integración de tecnologías de reconocimiento natural para crear una experiencia artística más intuitiva y accesible.

---

## 🧠 Conceptos Aprendidos

- Implementación de **reconocimiento de gestos** usando MediaPipe Hands
- Integración de **comandos de voz** para control de la aplicación
- Manejo de **threading** para procesamiento simultáneo de audio y video
- Desarrollo de **interfaces naturales** para aplicaciones creativas
- Gestión de **feedback visual** en tiempo real
- Implementación de sistema de **guardado automático** de obras

---

## 🔧 Herramientas y Entornos

- Python 3.12
- OpenCV
- MediaPipe
- NumPy
- SpeechRecognition
- Sounddevice
- Threading

---

## 🧪 Implementación

### 🔹 Flujo General
1. Captura de video en tiempo real mediante webcam
2. Detección y tracking de manos usando MediaPipe
3. Reconocimiento de comandos de voz en español
4. Renderizado de trazos según posición del dedo índice
5. Gestión de estados de dibujo mediante gestos
6. Sistema de guardado automático de obras

### 🔹 Código relevante

```python
def draw(self, image, hand_landmarks):
    index_tip = hand_landmarks.landmark[8]
    h, w, _ = image.shape
    x, y = int(index_tip.x * w), int(index_tip.y * h)
    
    if self.drawing:
        cv2.circle(self.canvas, (x, y), self.brush_size, self.current_color, -1)
```

---

## 📊 Resultados Visuales

La aplicación ofrece una experiencia artística natural e intuitiva:
- **Control Gestual:** El dedo índice funciona como pincel virtual
- **Comandos por Voz:** Cambio de colores y acciones mediante palabras
- **Feedback Visual:** Indicadores en pantalla muestran el estado actual
- **Guardado Automático:** Las obras se almacenan con marca temporal

> ![Demostración de la aplicación](pintura_interactiva.gif)

Los usuarios pueden crear arte digital de forma intuitiva, alternando entre colores y herramientas mediante voz mientras dibujan con movimientos naturales de la mano.

---

## 🧩 Prompts Usados

- Necesito crear una aplicación de pintura digital que use reconocimiento de gestos y voz para permitir dibujar sin periféricos tradicionales. Debe detectar la posición del dedo índice para dibujar y responder a comandos de voz para cambiar colores y guardar el trabajo. ¿Podrías ayudarme con la estructura del código y la integración de estas tecnologías?

---

## 💬 Reflexión Final

Este taller demuestra el potencial de las interfaces naturales en aplicaciones creativas. La combinación de reconocimiento de gestos y voz no solo hace la experiencia más accesible, sino que también abre nuevas posibilidades para la expresión artística digital.

---