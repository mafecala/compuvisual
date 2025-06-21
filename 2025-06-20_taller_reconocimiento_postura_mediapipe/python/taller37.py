import cv2
import mediapipe as mp
import numpy as np
import time

# === Inicialización ===
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# === Captura de video ===
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ No se pudo abrir la cámara.")
    exit()

# === Variables para caminar ===
prev_left_y = None
prev_right_y = None
walk_counter = 0
walk_threshold = 10  # Frames de movimiento mínimo

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ No se pudo leer un frame.")
        break

    # Voltear para efecto espejo (opcional)
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar frame con MediaPipe
    results = pose.process(rgb)

    action = "🧍 En espera"

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Extraer landmarks
        lm = results.pose_landmarks.landmark

        # Extraer coordenadas relevantes
        left_wrist_y = lm[mp_pose.PoseLandmark.LEFT_WRIST].y
        right_wrist_y = lm[mp_pose.PoseLandmark.RIGHT_WRIST].y
        nose_y = lm[mp_pose.PoseLandmark.NOSE].y

        left_hip_y = lm[mp_pose.PoseLandmark.LEFT_HIP].y
        right_hip_y = lm[mp_pose.PoseLandmark.RIGHT_HIP].y
        left_knee_y = lm[mp_pose.PoseLandmark.LEFT_KNEE].y
        right_knee_y = lm[mp_pose.PoseLandmark.RIGHT_KNEE].y

        left_foot_y = lm[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y
        right_foot_y = lm[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y

        # === Lógica de acciones ===

        if left_wrist_y < nose_y and right_wrist_y < nose_y:
            action = "🙌 Brazos levantados"

        elif left_hip_y > left_knee_y and right_hip_y > right_knee_y:
            action = "🪑 Sentado"

        elif prev_left_y is not None and prev_right_y is not None:
            if abs(left_foot_y - prev_left_y) > 0.02 or abs(right_foot_y - prev_right_y) > 0.02:
                walk_counter += 1
                if walk_counter > walk_threshold:
                    action = "🚶 Caminando"
            else:
                walk_counter = 0

        # Actualizar valores previos
        prev_left_y = left_foot_y
        prev_right_y = right_foot_y

    # Mostrar acción detectada
    cv2.putText(frame, f"Accion: {action}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar ventana
    cv2.imshow("MediaPipe Pose - Acciones", frame)

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
