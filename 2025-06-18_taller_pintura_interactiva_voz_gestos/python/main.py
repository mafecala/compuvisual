import os
import cv2
import mediapipe as mp
import numpy as np
from datetime import datetime
import sounddevice as sd
import speech_recognition as sr
import threading

class DigitalCanvas:
    def __init__(self):
        # Inicialización de MediaPipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils
        self.output_dir = "./obras"
        os.makedirs(self.output_dir, exist_ok=True)

        # Inicialización de la cámara
        self.cap = cv2.VideoCapture(0)
        
        # Canvas y variables de dibujo
        self.canvas = np.zeros((480, 640, 3), dtype=np.uint8)
        self.drawing = False
        self.current_color = (0, 0, 255)  # Rojo por defecto
        self.brush_size = 5
        self.brush_type = "circle"
        
        # Variables para feedback visual
        self.feedback_text = ""
        self.feedback_time = 0

        self.recognizer = sr.Recognizer()
        self.is_listening = True
        
        # Iniciar thread de reconocimiento de voz
        self.voice_thread = threading.Thread(target=self.voice_recognition_loop)
        self.voice_thread.daemon = True
        self.voice_thread.start()

    def show_feedback(self, text):
        self.feedback_text = text
        self.feedback_time = 50  # Duración del feedback en frames

    def save_canvas(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.output_dir, f"arte_digital_{timestamp}.png")
        
        try:
            cv2.imwrite(filename, self.canvas)
            self.show_feedback(f"Imagen guardada en {filename}")
        except Exception as e:
            self.show_feedback(f"Error al guardar: {str(e)}")

    def handle_keyboard(self, key):
        if key == ord('r'):
            self.current_color = (0, 0, 255)  # Rojo
            self.show_feedback("Color: Rojo")
        elif key == ord('g'):
            self.current_color = (0, 255, 0)  # Verde
            self.show_feedback("Color: Verde")
        elif key == ord('b'):
            self.current_color = (255, 0, 0)  # Azul
            self.show_feedback("Color: Azul")
        elif key == ord('c'):
            self.canvas = np.zeros((480, 640, 3), dtype=np.uint8)
            self.show_feedback("Canvas limpiado")
        elif key == ord('s'):
            self.save_canvas()

    def draw(self, image, hand_landmarks):
        # Obtener posición del dedo índice
        index_tip = hand_landmarks.landmark[8]
        h, w, _ = image.shape
        x, y = int(index_tip.x * w), int(index_tip.y * h)
        
        # Detectar si el dedo medio está levantado
        middle_tip = hand_landmarks.landmark[12]
        middle_y = int(middle_tip.y * h)
        index_y = int(index_tip.y * h)
        
        self.drawing = middle_y > index_y
        
        if self.drawing:
            if self.brush_type == "circle":
                cv2.circle(self.canvas, (x, y), self.brush_size, self.current_color, -1)
            elif self.brush_type == "square":
                cv2.rectangle(self.canvas, 
                            (x - self.brush_size, y - self.brush_size),
                            (x + self.brush_size, y + self.brush_size),
                            self.current_color, -1)
    def voice_recognition_loop(self):
        while self.is_listening:
            try:
                # Configurar el reconocimiento de voz usando sounddevice
                duration = 3  # duración de cada grabación en segundos
                sample_rate = 44100
                
                # Grabar audio
                recording = sd.rec(int(duration * sample_rate),
                                 samplerate=sample_rate,
                                 channels=1,
                                 dtype=np.int16)
                sd.wait()
                
                # Convertir el audio a un formato compatible con speech_recognition
                audio_data = sr.AudioData(recording.tobytes(),
                                        sample_rate,
                                        2)
                
                # Reconocer el comando
                text = self.recognizer.recognize_google(audio_data, language="es-ES").lower()
                
                # Procesar comandos
                if "rojo" in text:
                    self.current_color = (0, 0, 255)
                    self.show_feedback("Color: Rojo")
                elif "verde" in text:
                    self.current_color = (0, 255, 0)
                    self.show_feedback("Color: Verde")
                elif "azul" in text:
                    self.current_color = (255, 0, 0)
                    self.show_feedback("Color: Azul")
                elif "limpiar" in text:
                    self.canvas = np.zeros((480, 640, 3), dtype=np.uint8)
                    self.show_feedback("Canvas limpiado")
                elif "guardar" in text:
                    self.save_canvas()
                    
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue
            except Exception as e:
                print(f"Error: {e}")
                continue
    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)
            
            output = frame.copy()
            mask = self.canvas > 0
            output[mask] = self.canvas[mask]
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(output, hand_landmarks, 
                                             self.mp_hands.HAND_CONNECTIONS)
                    self.draw(frame, hand_landmarks)
            
            if self.feedback_time > 0:
                cv2.putText(output, self.feedback_text, (10, 30),
                          cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                self.feedback_time -= 1
            
            # Mostrar controles
            cv2.putText(output, "R: Rojo | G: Verde | B: Azul | C: Limpiar | S: Guardar | ESC: Salir", 
                       (10, output.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            cv2.imshow("Digital Canvas", output)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                break
            self.handle_keyboard(key)
            
            if cv2.waitKey(1) & 0xFF == 27:  # ESC
                self.is_listening = False  # Stop voice recognition thread
                break
            
            self.handle_keyboard(key)  
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    canvas = DigitalCanvas()
    canvas.run()