import cv2
import json
import csv
from datetime import datetime
from ultralytics import YOLO
import os
import time

# Crear carpeta si no existe
os.makedirs("backend", exist_ok=True)

# Cargar modelo
modelo = YOLO("yolov8n.pt")  

cap = cv2.VideoCapture(1)

# Espera a que la cámara se estabilice
for i in range(20):  # Lee varios frames antes
    ret, frame = cap.read()
    if not ret:
        print("❌ Falló la lectura del frame")
        cap.release()
        exit()
    time.sleep(0.05)  # 50 ms entre capturas

# Usa el último frame que ya es válido
cv2.imshow("Frame final capturado", frame)
cv2.waitKey(0)
cv2.imwrite("backend/deteccion.png", frame)
cv2.destroyAllWindows()

cap.release()

# Aplicar modelo
resultados = modelo(frame)[0]

# Dibujar y guardar imagen
anotado = frame.copy()
detecciones_json = {
    "timestamp": datetime.now().isoformat(),
    "objects": []
}

for box in resultados.boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    conf = float(box.conf[0])
    cls = int(box.cls[0])
    clase = modelo.names[cls]

    # Dibujar rectángulo
    cv2.rectangle(anotado, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(anotado, f"{clase} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Guardar en JSON
    detecciones_json["objects"].append({
        "class": clase,
        "confidence": round(conf, 2),
        "x": x1,
        "y": y1,
        "w": x2 - x1,
        "h": y2 - y1
    })
cv2.imshow("Frame capturado", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Guardar imagen anotada
cv2.imwrite("backend/deteccion.png", anotado)

# Guardar JSON
with open("backend/resultados.json", "w") as f:
    json.dump(detecciones_json, f, indent=2)

# Guardar CSV (opcional)
with open("backend/resumen.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["class", "confidence", "x", "y", "w", "h"])
    for obj in detecciones_json["objects"]:
        writer.writerow([obj["class"], obj["confidence"], obj["x"], obj["y"], obj["w"], obj["h"]])

print("✅ Resultados guardados en 'backend/'")
