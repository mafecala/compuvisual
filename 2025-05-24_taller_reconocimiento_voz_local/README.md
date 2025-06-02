# 🧠 Taller - Voz al Código: Comandos por Reconocimiento de Voz Local

## 📅 Fecha
`2025-05-24`

## 🌷 Equipo de trabajo
Mi grupo está conformado por:

- Julián Ramírez Díaz (julramirezdi@unal.edu.co)
- Xamir Ernesto Rojas Gamboa (xerojasga@unal.edu.co)
- Julián David Rincón Orjuela (jurinconor@unal.edu.co)
- María Fernanda Cala Rodríguez (mcalar@unal.edu.co)

Este taller fue realizado por:

**Julián David Rincón Orjuela (jurinconor@unal.edu.co)**

## 🎯 Objetivo del Taller

Desarrollar una aplicación interactiva que utilice reconocimiento de voz local para ejecutar comandos visuales en una interfaz gráfica creada con Tkinter. La aplicación responde a comandos de voz y proporciona retroalimentación visual y auditiva.

---

## 🧠 Conceptos Aprendidos

- Uso de la biblioteca `speech_recognition` para reconocimiento de voz local.
- Integración de `pyttsx3` para retroalimentación por voz.
- Creación de interfaces gráficas interactivas con Tkinter.
- Uso de hilos (`threading`) para manejar tareas concurrentes.

---

## 🔧 Herramientas y Entornos

- Python 3
- Bibliotecas: `tkinter`, `speech_recognition`, `pyttsx3`, `threading`

---

## 🧪 Implementación

### 🔹 Etapas realizadas
1. Configuración del motor de voz y reconocimiento de comandos.
2. Creación de una interfaz gráfica con Tkinter.
3. Implementación de reconocimiento de voz en tiempo real.
4. Retroalimentación visual y auditiva basada en comandos reconocidos.

### 🔹 Código relevante

- **Inicialización del Motor de Voz**: Configura el motor de texto a voz.

```python
engine = pyttsx3.init()
engine.setProperty("rate", 150)
```


- **Reconocimiento de Comandos:** Escucha y procesa comandos de voz.

```python
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
```

- **Interfaz Gráfica:** Cambia el color de fondo y muestra el comando reconocido.

```python
def actualizar(self, color, texto):
    self.canvas.config(bg=color)
    self.label.config(text=f"Comando: {texto}")
    hablar(f"Ejecutando comando {texto}") 
```


- **Hilos para Reconocimiento Continuo:** Ejecuta el reconocimiento de voz en un hilo separado.
```python
def iniciar_reconocimiento_en_hilo(self):
    threading.Thread(target=self.reconocer_comando).start()
    self.root.after(5000, self.iniciar_reconocimiento_en_hilo)
```
---

## 📊 Resultados Visuales

Interfaz Gráfica: Una ventana que cambia de color según el comando reconocido.
Retroalimentación Auditiva: El sistema confirma el comando ejecutado mediante voz.


### Python

![Resultado Reconocimiento de Voz](resultados/reconocimiento%20voz.gif)




## 💬 Reflexión Final

Este taller permitió explorar el uso de reconocimiento de voz local y su integración con interfaces gráficas. La implementación de retroalimentación visual y auditiva demuestra cómo se pueden crear aplicaciones interactivas que respondan a comandos de voz en tiempo real. ` 
