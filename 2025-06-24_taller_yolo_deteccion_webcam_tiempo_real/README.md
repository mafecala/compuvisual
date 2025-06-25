# 🎯 Detección de Objetos en Tiempo Real con YOLO

## 📅 Fecha
2025-06-24

---

## 🎯 Objetivo del Taller

Implementar un sistema de detección de objetos en tiempo real utilizando YOLO y la webcam. El proyecto se enfoca en evaluar el rendimiento del modelo en términos de precisión y velocidad (FPS) en un entorno de procesamiento en vivo.

---

## 🧠 Conceptos Aprendidos

- **Inferencia en tiempo real** con YOLO
- **Procesamiento de video** con OpenCV
- **Medición de rendimiento** (FPS, tiempo de inferencia)
- **Visualización de resultados** en tiempo real
- **Optimización de rendimiento** en detección de objetos

---

## 🔧 Herramientas y Entornos

- Python 3.12
- Ultralytics YOLO
- OpenCV
- PyTorch
- NumPy

---

## 🧪 Implementación


### 🔹 Código Principal

```python
class ObjectDetector:
    def __init__(self, model_path='yolov8n.pt', conf_threshold=0.5):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.fps_history = []
        
    def process_frame(self, frame):
        start_time = time.time()
        results = self.model(frame, stream=True)
        inference_time = time.time() - start_time
        
        # Procesar detecciones
        for r in results:
            boxes = r.boxes
            for box in boxes:
                if float(box.conf[0]) > self.conf_threshold:
                    self.draw_detection(frame, box)
        
        fps = 1.0 / inference_time
        self.draw_stats(frame, fps, inference_time)
        return frame
```

---

## 📊 Resultados y Métricas

- **FPS Promedio:** ~20-30 FPS (CPU)
- **Tiempo de Inferencia:** ~30-50ms por frame
- **Precisión de Detección:** Configurable via conf_threshold
- **Clases Detectables:** 80 objetos diferentes

> ![Demostración de Detección](./results/yolo_objects.gif)

---

## ⚠️ Requisitos

- Webcam funcional
- Python 3.12+
- 8GB RAM mínimo
- GPU recomendada para mejor rendimiento
- Buena iluminación para detección óptima

---

## 🕹️ Controles

- `q`: Salir de la aplicación
- `+`: Aumentar umbral de confianza
- `-`: Disminuir umbral de confianza
- `s`: Guardar captura actual

---

## 🧩 Prompts Usados

- Necesito implementar un sistema de detección de objetos en tiempo real usando YOLO y una webcam. El sistema debe mostrar FPS, tiempo de inferencia y permitir ajustar el umbral de confianza en tiempo real.

---

## 💬 Reflexión Final

Este proyecto demuestra la capacidad de YOLO para realizar detección de objetos en tiempo real con recursos limitados. La implementación permite un equilibrio ajustable entre precisión y velocidad, siendo útil para aplicaciones prácticas de visión por computador.

---