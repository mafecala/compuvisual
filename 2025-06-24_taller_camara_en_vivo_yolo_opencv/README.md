# 📸 Cámara en Vivo: Procesamiento con YOLO

## 📅 Fecha
2025-06-24

---

## 🎯 Objetivo del Taller

Desarrollar un sistema de procesamiento de video en tiempo real que integra filtros clásicos de visión por computador con detección de objetos mediante YOLO. El proyecto captura video desde la webcam y aplica diferentes técnicas de procesamiento visual en vivo.

---

## 🧠 Conceptos Aprendidos

- **Captura de video** en tiempo real con OpenCV
- **Filtros de imagen** básicos y avanzados
- **Detección de objetos** con YOLO
- **Procesamiento en tiempo real** de frames
- **Interacción mediante teclado** para control de la aplicación
- **Grabación y captura** de resultados

---

## 🔧 Herramientas y Entornos

- Python 3.12
- OpenCV
- Ultralytics YOLO
- NumPy

Instalación:
```bash
pip install opencv-python numpy ultralytics
```

---

## 🧪 Implementación

### 🔹 Estructura del Proyecto
```
camera-processing/
├── src/
│   ├── main.py               # Aplicación principal
│   ├── processors/
│   │   ├── __init__.py
│   │   ├── yolo_detector.py  # Detector YOLO
│   │   └── filters.py        # Filtros de imagen
│   └── utils/
│       ├── __init__.py
│       └── video_utils.py    # Utilidades de video
└── README.md
```

### 🔹 Código Principal

```python
# Ejemplo de Sistema de Procesamiento Visual
class VideoProcessor:
    def __init__(self):
        # Inicializar detectores y filtros
        self.yolo = YOLODetector()
        self.filters = ImageFilters()
        self.cap = cv2.VideoCapture(0)
        
        # Estados del sistema
        self.modes = {
            'original': lambda f: self.yolo.detect(f),
            'gray': lambda f: self.filters.grayscale(f),
            'binary': lambda f: self.filters.binary(f, threshold=127),
            'edges': lambda f: self.filters.canny_edges(f, 100, 200)
        }
        self.current_mode = 'original'
        
    def process_frame(self, frame):
        # Procesar frame según el modo actual
        processed = self.modes[self.current_mode](frame)
        
        
        # Agregar información en pantalla
        if self.current_mode == 'original':
            people_count = self.yolo.person_count
            cv2.putText(processed, 
                       f'Personas detectadas: {people_count}',
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                       1, (0, 255, 0), 2)
            
        # Agregar modo actual en la esquina
        cv2.putText(processed,
                   f'Modo: {self.current_mode}',
                   (10, processed.shape[0] - 20),
                   cv2.FONT_HERSHEY_SIMPLEX,
                   0.6, (255, 255, 255), 2)
                   
        return processed

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            # Procesar y mostrar frame
            processed = self.process_frame(frame)
            cv2.imshow('Monitor Visual', processed)
            
            # Control de teclado (q: salir, 1-4: cambiar modo)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif ord('1') <= key <= ord('4'):
                self.current_mode = list(self.modes.keys())[key - ord('1')]
```

### 🔹 Controles del Sistema

- `q`: Salir de la aplicación
- `p`: Pausar/Reanudar
- `s`: Guardar captura
- `r`: Iniciar/Detener grabación
- `1-4`: Cambiar filtros
  1. Original + YOLO
  2. Escala de grises
  3. Binario
  4. Detección de bordes

---

## 📊 Resultados

Funcionalidades implementadas:
- **Detección en vivo** de objetos con YOLO
- **Conteo de personas** en tiempo real
- **Múltiples filtros** de procesamiento
- **Grabación** de video procesado
- **Captura** de frames individuales

> ![Demostración de Procesamiento](./results/yolo.gif)

---

## ⚠️ Requisitos

- Webcam funcional
- Python 3.12+
- 4GB RAM mínimo
- GPU recomendada para mejor rendimiento
- Buena iluminación para detección óptima

---

## 🧩 Prompts Usados

- Necesito implementar un sistema de procesamiento de video en tiempo real que combine filtros clásicos de OpenCV con detección de objetos usando YOLO. El sistema debe poder cambiar entre diferentes modos de visualización y permitir la grabación de resultados.

---

## 💬 Reflexión Final

Este proyecto demuestra la integración efectiva de técnicas clásicas de procesamiento de imagen con métodos modernos de detección basados en deep learning. La combinación de filtros tradicionales con YOLO permite una experiencia completa de análisis visual en tiempo real.

---