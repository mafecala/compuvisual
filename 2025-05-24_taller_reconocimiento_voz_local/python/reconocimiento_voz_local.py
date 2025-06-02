import tkinter as tk
import threading
import speech_recognition as sr
import pyttsx3

# Inicializar motor de voz
engine = pyttsx3.init()
engine.setProperty("rate", 150)


def hablar(mensaje):
    engine.say(mensaje)
    engine.runAndWait()


# Diccionario de comandos
comandos = {
    "red": "red",
    "blue": "blue",
    "start": "green",
    "stop": "gray",
    "rotate": "yellow",
}


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Comandos por Voz")
        self.root.geometry("400x300")
        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="white")
        self.canvas.pack()
        self.label = tk.Label(
            self.root, text="Esperando comando...", font=("Arial", 14)
        )
        self.label.pack()
        self.root.after(1000, self.iniciar_reconocimiento_en_hilo)
        self.root.mainloop()

    def actualizar(self, color, texto):
        self.canvas.config(bg=color)
        self.label.config(text=f"Comando: {texto}")
        hablar(f"Ejecutando comando {texto}")

    def iniciar_reconocimiento_en_hilo(self):
        threading.Thread(target=self.reconocer_comando).start()
        self.root.after(5000, self.iniciar_reconocimiento_en_hilo)

    def reconocer_comando(self):
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("🎤 Escuchando...")
            try:
                audio = r.listen(mic, timeout=4)
                texto = r.recognize_sphinx(audio)
                print(f"🔍 Reconocido: {texto}")
                for comando in comandos:
                    if comando in texto:
                        self.actualizar(comandos[comando], comando)
                        return
                self.label.config(text="Comando no reconocido")
                hablar("No entendí el comando")
            except sr.WaitTimeoutError:
                print("⌛ Tiempo agotado")
            except sr.UnknownValueError:
                print("❌ No entendí lo que dijiste")


# Ejecutar
if __name__ == "__main__":
    App()
