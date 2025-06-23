import cv2
import os
from datetime import datetime
import pandas as pd
from ultralytics import YOLO
from tkinter import *
from PIL import Image, ImageTk

# ==== Configuración de carpetas y archivos ====
os.makedirs("logs", exist_ok=True)
os.makedirs("capturas", exist_ok=True)
log_path = "logs/eventos.csv"

# Crear CSV si no existe
if not os.path.exists(log_path):
    with open(log_path, "w") as f:
        f.write("timestamp,evento,clase,confianza\n")

# ==== Inicializar modelo YOLOv8 ====
model = YOLO("yolov8n.pt")  # Usa el modelo pequeño para velocidad

# ==== Contadores globales ====
conteo_objetos = {}

# ==== Función para registrar evento ====
def registrar_evento(evento, clase, conf):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"{timestamp},{evento},{clase},{conf:.2f}\n")

# ==== Interfaz con tkinter ====
root = Tk()
root.title("Detector en Tiempo Real")
root.geometry("900x700")

lbl_estado = Label(root, text="Estado: Inactivo", font=("Arial", 14))
lbl_estado.pack()

panel = Label(root)
panel.pack()

lbl_contador = Label(root, text="", font=("Arial", 12), justify=LEFT)
lbl_contador.pack(pady=10)

# ==== Captura de video y detección ====
cap = cv2.VideoCapture(1)

def procesar_frame():
    ret, frame = cap.read()
    if not ret:
        return

    results = model(frame, verbose=False)[0]
    nombres = model.names
    conteo_objetos.clear()

    for r in results.boxes:
        clase = int(r.cls[0])
        nombre = nombres[clase]
        conf = float(r.conf[0])
        conteo_objetos[nombre] = conteo_objetos.get(nombre, 0) + 1

        x1, y1, x2, y2 = map(int, r.xyxy[0])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{nombre} {conf:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Registrar si es persona
        if nombre == "person" and conf > 0.6:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path_img = f"capturas/persona_{timestamp}.jpg"
            cv2.imwrite(path_img, frame)
            registrar_evento("Persona detectada", nombre, conf)
            registrar_evento("Captura guardada", nombre, conf)
            lbl_estado.config(text="Estado: Alerta - Persona detectada")

    # Mostrar estado e imagen
    if "person" not in conteo_objetos:
        lbl_estado.config(text="Estado: Inactivo")

    # Mostrar conteo
    texto = "Conteo de objetos:\n"
    for clase, cantidad in conteo_objetos.items():
        texto += f"• {clase}: {cantidad}\n"
    lbl_contador.config(text=texto)

    # Mostrar imagen en Tkinter
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=img_pil.resize((800, 500)))
    panel.imgtk = img_tk
    panel.config(image=img_tk)

    root.after(30, procesar_frame)

# ==== Iniciar loop ====
procesar_frame()
root.mainloop()

cap.release()
cv2.destroyAllWindows()
