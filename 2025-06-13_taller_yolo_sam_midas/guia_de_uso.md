# **🚀 Guía Completa: Cómo Usar el Pipeline YOLO \+ SAM \+ MiDaS**

## **📋 Requisitos Previos**

* Cuenta de Google (para usar Google Colab)  
* Conexión a internet estable  
* Imágenes para procesar (opcional, se incluye demo)

---

## **🔧 PASO 1: Configuración Inicial en Google Colab**

### **1.1 Abrir Google Colab**

1. Ve a [https://colab.research.google.com](https://colab.research.google.com/)  
2. Inicia sesión con tu cuenta de Google  
3. Crea un nuevo notebook: **Archivo \> Nuevo notebook**

### **1.2 Activar GPU (Recomendado)**

1. Ve a **Entorno de ejecución \> Cambiar tipo de entorno de ejecución**  
2. Selecciona **GPU** en "Acelerador de hardware"  
3. Haz clic en **Guardar**

### **1.3 Copiar el Código**

1. Copia todo el código del pipeline en la primera celda del notebook  
2. Ejecuta la celda (Ctrl+Enter o botón ▶️)

---

## **📦 PASO 2: Instalación de Dependencias**

### **2.1 Crear y Ejecutar Celda de Instalación**

Crea una nueva celda y pega este código:

\# Instalación de todas las dependencias necesarias  
\!pip install ultralytics  
\!pip install segment-anything  
\!pip install opencv-python  
\!pip install timm  
\!pip install matplotlib  
\!pip install torch torchvision  
\!pip install numpy  
\!pip install Pillow  
\!pip install pandas

\# Descargar modelo SAM (archivo grande \~2.5GB)  
\!wget https://dl.fbaipublicfiles.com/segment\_anything/sam\_vit\_h\_4b8939.pth

\# Clonar repositorio SAM  
\!git clone https://github.com/facebookresearch/segment-anything.git

print("✅ Instalación completada\!")

**⚠️ IMPORTANTE**: Esta instalación puede tomar 5-10 minutos. Espera a que termine antes de continuar.

---

## **🎯 PASO 3: Inicialización del Pipeline**

### **3.1 Crear Celda de Inicialización**

\# Inicializar el pipeline  
print("🔄 Inicializando modelos...")  
pipeline \= VisionPipeline()  
print("✅ Pipeline listo para usar\!")

**📝 Nota**: La primera vez puede tomar 2-3 minutos descargando modelos.

---

## **🖼️ PASO 4: Opciones para Procesar Imágenes**

### **OPCIÓN A: Demo con Imagen de Ejemplo (Más Fácil)**

\# Ejecutar demo automático  
resultados \= demo\_con\_imagen\_ejemplo()

**¿Qué hace esto?**

* Descarga automáticamente una imagen de ejemplo  
* Procesa la imagen completa  
* Muestra todas las visualizaciones  
* Guarda resultados en carpetas

### **OPCIÓN B: Subir Tu Propia Imagen**

#### **B.1 Subir Imagen a Colab**

1. En el panel izquierdo, haz clic en el ícono de **📁 Archivos**  
2. Arrastra tu imagen desde tu computadora  
3. O haz clic en **📤 Subir** y selecciona la imagen

#### **B.2 Procesar Tu Imagen**

\# Cambiar "mi\_imagen.jpg" por el nombre de tu archivo  
imagen\_path \= "/content/mi\_imagen.jpg"  
resultados \= pipeline.procesar\_imagen\_completa(imagen\_path)

### **OPCIÓN C: Usar URL de Imagen**

import urllib.request

\# Descargar imagen desde URL  
url \= "https://ejemplo.com/mi\_imagen.jpg"  
urllib.request.urlretrieve(url, "imagen\_descargada.jpg")

\# Procesar  
resultados \= pipeline.procesar\_imagen\_completa("imagen\_descargada.jpg")

---

## **🔍 PASO 5: Explorar Funcionalidades Individuales**

### **5.1 Solo Detección YOLO**

\# Probar solo detección de objetos  
detecciones \= pipeline.detectar\_objetos\_yolo("mi\_imagen.jpg", confidence=0.3)  
print(f"Objetos detectados: {detecciones\['nombres\_clases'\]}")  
print(f"Confianzas: {detecciones\['confianzas'\]}")

### **5.2 Solo Segmentación SAM**

\# Primero detectar objetos  
detecciones \= pipeline.detectar\_objetos\_yolo("mi\_imagen.jpg")

\# Luego segmentar  
masks \= pipeline.segmentar\_con\_sam(detecciones\['imagen'\], detecciones\['boxes'\])  
print(f"Máscaras generadas: {len(masks)}")

### **5.3 Solo Estimación de Profundidad**

import cv2

\# Cargar imagen  
imagen \= cv2.imread("mi\_imagen.jpg")  
imagen\_rgb \= cv2.cvtColor(imagen, cv2.COLOR\_BGR2RGB)

\# Estimar profundidad  
depth\_map \= pipeline.estimar\_profundidad\_midas(imagen\_rgb)

\# Visualizar  
import matplotlib.pyplot as plt  
plt.figure(figsize=(10, 5))  
plt.subplot(1, 2, 1\)  
plt.imshow(imagen\_rgb)  
plt.title('Original')  
plt.axis('off')

plt.subplot(1, 2, 2\)  
plt.imshow(depth\_map, cmap='plasma')  
plt.title('Mapa de Profundidad')  
plt.axis('off')  
plt.show()

---

## **🎨 PASO 6: Efectos Creativos**

### **6.1 Efecto Bokeh (Desenfoque de Fondo)**

\# Procesar imagen completa primero  
resultados \= pipeline.procesar\_imagen\_completa("mi\_imagen.jpg")

\# Aplicar efecto bokeh más intenso  
imagen\_bokeh \= pipeline.aplicar\_efecto\_bokeh(  
    resultados\['detecciones'\]\['imagen'\],   
    resultados\['masks'\],   
    resultados\['depth\_map'\],  
    blur\_strength=25  \# Más desenfoque  
)

\# Mostrar resultado  
plt.figure(figsize=(12, 4))  
plt.subplot(1, 2, 1\)  
plt.imshow(resultados\['detecciones'\]\['imagen'\])  
plt.title('Original')  
plt.axis('off')

plt.subplot(1, 2, 2\)  
plt.imshow(imagen\_bokeh)  
plt.title('Efecto Bokeh')  
plt.axis('off')  
plt.show()

### **6.2 Análisis de Objetos por Distancia**

\# Obtener análisis detallado  
df \= resultados\['analisis'\]

\# Mostrar objetos ordenados por cercanía  
print("🏆 OBJETOS MÁS CERCANOS:")  
print(df\[\['clase', 'distancia\_relativa', 'profundidad\_media'\]\].head())

\# Filtrar solo objetos cercanos  
objetos\_cercanos \= df\[df\['distancia\_relativa'\] \> 0.7\]  
print(f"\\n📍 Objetos en primer plano: {len(objetos\_cercanos)}")

---

## **📁 PASO 7: Trabajar con Múltiples Imágenes**

### **7.1 Crear Carpeta de Imágenes**

import os  
os.makedirs('mis\_imagenes', exist\_ok=True)  
print("📁 Carpeta 'mis\_imagenes' creada")  
print("👆 Sube tus imágenes a esta carpeta usando el panel de archivos")

### **7.2 Procesar Todas las Imágenes**

\# Procesar todas las imágenes de la carpeta  
procesar\_multiples\_imagenes('mis\_imagenes')

---

## **📊 PASO 8: Ver y Descargar Resultados**

### **8.1 Explorar Archivos Generados**

\# Ver estructura de archivos creados  
\!ls \-la outputs/  
\!ls \-la outputs/depth\_maps/  
\!ls \-la outputs/recortes/

### **8.2 Descargar Resultados**

1. Ve al panel de **📁 Archivos** en Colab  
2. Navega a la carpeta `outputs`  
3. Haz clic derecho en cualquier archivo  
4. Selecciona **Descargar**

### **8.3 Ver CSV con Estadísticas**

import pandas as pd

\# Leer archivo CSV generado  
df \= pd.read\_csv('outputs/imagen\_analisis.csv')  
print("📈 ESTADÍSTICAS COMPLETAS:")  
print(df.to\_string())

\# Crear gráfico de distancias  
import matplotlib.pyplot as plt  
plt.figure(figsize=(10, 6))  
plt.bar(df\['clase'\], df\['distancia\_relativa'\])  
plt.title('Distancia Relativa por Objeto')  
plt.xticks(rotation=45)  
plt.tight\_layout()  
plt.show()

---

## **🔧 PASO 9: Personalización Avanzada**

### **9.1 Ajustar Parámetros de Detección**

\# Detectar más objetos (menor confianza)  
detecciones \= pipeline.detectar\_objetos\_yolo("mi\_imagen.jpg", confidence=0.2)

\# Detectar menos objetos (mayor confianza)  
detecciones \= pipeline.detectar\_objetos\_yolo("mi\_imagen.jpg", confidence=0.8)

### **9.2 Crear Visualizaciones Personalizadas**

def mi\_visualizacion\_personalizada(imagen, masks, depth\_map, nombres):  
    """Crear tu propia visualización"""  
    plt.figure(figsize=(15, 5))  
      
    \# Panel 1: Imagen original  
    plt.subplot(1, 3, 1\)  
    plt.imshow(imagen)  
    plt.title('Mi Imagen')  
    plt.axis('off')  
      
    \# Panel 2: Solo máscaras  
    plt.subplot(1, 3, 2\)  
    combined\_mask \= np.zeros(imagen.shape\[:2\])  
    for i, mask in enumerate(masks):  
        combined\_mask\[mask\] \= i \+ 1  
    plt.imshow(combined\_mask, cmap='tab10')  
    plt.title('Segmentación')  
    plt.axis('off')  
      
    \# Panel 3: Profundidad invertida (más claro \= más cerca)  
    plt.subplot(1, 3, 3\)  
    plt.imshow(1 \- depth\_map, cmap='hot')  
    plt.title('Cercanía (Claro \= Cerca)')  
    plt.axis('off')  
      
    plt.tight\_layout()  
    plt.show()

\# Usar tu visualización  
resultados \= pipeline.procesar\_imagen\_completa("mi\_imagen.jpg")  
mi\_visualizacion\_personalizada(  
    resultados\['detecciones'\]\['imagen'\],  
    resultados\['masks'\],  
    resultados\['depth\_map'\],  
    resultados\['detecciones'\]\['nombres\_clases'\]  
)

---

## **🚨 PASO 10: Solución de Problemas Comunes**

### **Error: "No se detectaron objetos"**

**Solución:**

\# Reducir umbral de confianza  
detecciones \= pipeline.detectar\_objetos\_yolo("mi\_imagen.jpg", confidence=0.1)

### **Error: "Out of memory"**

**Soluciones:**

1. Redimensionar imagen antes de procesar:

from PIL import Image  
img \= Image.open("mi\_imagen.jpg")  
img \= img.resize((800, 600))  \# Imagen más pequeña  
img.save("imagen\_pequena.jpg")

2. Usar modelo YOLO más pequeño:

pipeline.yolo\_model \= YOLO('yolov8n.pt')  \# Nano (más rápido)

### **Error: "Archivo no encontrado"**

**Verificar ruta:**

import os  
print("Archivos disponibles:")  
print(os.listdir('/content/'))

---

## **🎯 PASO 11: Casos de Uso Específicos**

### **11.1 Análisis de Seguridad**

\# Detectar personas y vehículos  
def analizar\_seguridad(imagen\_path):  
    detecciones \= pipeline.detectar\_objetos\_yolo(imagen\_path, confidence=0.4)  
      
    personas \= \[i for i, clase in enumerate(detecciones\['nombres\_clases'\]) if 'person' in clase\]  
    vehiculos \= \[i for i, clase in enumerate(detecciones\['nombres\_clases'\]) if any(v in clase for v in \['car', 'truck', 'bus'\])\]  
      
    print(f"👥 Personas detectadas: {len(personas)}")  
    print(f"🚗 Vehículos detectados: {len(vehiculos)}")  
      
    return personas, vehiculos

\# Usar  
personas, vehiculos \= analizar\_seguridad("mi\_imagen.jpg")

### **11.2 Análisis de Retail**

\# Contar productos en estantería  
def contar\_productos(imagen\_path):  
    resultados \= pipeline.procesar\_imagen\_completa(imagen\_path)  
    df \= resultados\['analisis'\]  
      
    \# Productos por distancia  
    primer\_plano \= df\[df\['distancia\_relativa'\] \> 0.6\]  
    fondo \= df\[df\['distancia\_relativa'\] \<= 0.6\]  
      
    print(f"🛍️ Productos en primer plano: {len(primer\_plano)}")  
    print(f"📦 Productos en fondo: {len(fondo)}")  
      
    return primer\_plano, fondo

---

## **📚 PASO 12: Recursos Adicionales**

### **Documentación de Modelos:**

* **YOLO**: [https://docs.ultralytics.com](https://docs.ultralytics.com/)  
* **SAM**: [https://github.com/facebookresearch/segment-anything](https://github.com/facebookresearch/segment-anything)  
* **MiDaS**: [https://github.com/intel-isl/MiDaS](https://github.com/intel-isl/MiDaS)

### **Tipos de Imágenes Ideales:**

* ✅ **Buenas**: Fotos claras, buena iluminación, objetos bien definidos  
* ✅ **Perfectas**: Escenas urbanas, interiores, retratos con fondo  
* ⚠️ **Difíciles**: Imágenes muy oscuras, objetos muy pequeños, escenas complejas

### **Límites del Sistema:**

* **Memoria**: Imágenes muy grandes (\>4K) pueden causar errores  
* **Precisión**: Objetos muy pequeños pueden no detectarse  
* **Velocidad**: Procesamiento puede tomar 30-60 segundos por imagen

---

