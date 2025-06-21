# 🌐 Visualización de Imágenes y Video 360° en Unity y Three.js

## 📅 Fecha
2025-05-26 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Aprender a cargar e integrar **imágenes panorámicas (equirectangulares)** y **videos 360°** dentro de entornos 3D inmersivos usando **Unity**. Este tipo de contenido es clave para experiencias XR, recorridos virtuales y visualización inmersiva, proporcionando al usuario una experiencia envolvente completa.

---

## 🧠 Conceptos Aprendidos

- **Imagen 360° equirectangular**: proyección plana de una esfera completa que permite visualización panorámica.
- **Video 360°**: secuencia visual que cubre todos los ángulos de una escena en movimiento.
- **Skybox o Esfera invertida**: técnica para mostrar el entorno alrededor del usuario desde el interior.
- **Mapeo UV y proyección interna** para representar correctamente contenido esférico en el espacio 3D.
- Gestión dinámica de contenido multimedia mediante scripting en Unity.
- Implementación de interfaces de usuario para alternar entre modos de visualización.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- VideoPlayer Component
- Material System y Texturas
- UI System (Slider, Canvas)

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Configuración de objeto esférico con normales invertidas para visualización interna.
2. Creación de material con textura equirectangular para imágenes 360°.
3. Implementación de VideoPlayer component para reproducción de video 360°.
4. Sistema de gestión para alternar entre modos imagen y video.
5. Interfaz de usuario con slider para control dinámico de visualización.
6. Sincronización de estados entre componentes multimedia.

### 🔹 Código relevante

```csharp
// Sistema de alternancia entre imagen y video panorámico
public void CambiarModo(float valor)
{
    int modoSeleccionado = Mathf.RoundToInt(valor);
    
    switch (modoSeleccionado)
    {
        case 1:
            MostrarImagen();
            break;
        case 2:
            MostrarVideo();
            break;
        default:
            Debug.LogWarning("Modo no válido: " + modoSeleccionado);
            break;
    }
}

private void MostrarVideo()
{
    esferapanoramica.SetActive(false);
    esferaVideo.SetActive(true);
    
    // Iniciar reproducción automáticamente
    if (videoScript != null)
    {
        videoScript.ReproducirVideo();
    }
}
```

---

## 📊 Resultados Visuales

El sistema permite una experiencia inmersiva completa con dos modos de visualización:
- **Modo 1:** Imagen panorámica 360° estática con proyección equirectangular perfecta
- **Modo 2:** Video 360° dinámico con reproducción automática y controles integrados

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025_05_26_Taller13_Visualizacion_Imagenes_Video/Unity/GifVisualizImgVideo.gif)


La transición entre modos es fluida y mantiene la posición de cámara, permitiendo al usuario explorar el contenido mediante rotación libre de la vista. El control mediante slider proporciona una interfaz intuitiva para alternar entre contenido estático y dinámico.

**Nota:** El sistema gestiona automáticamente la pausa/reproducción de video para optimizar recursos cuando no está activo.

---

## 🧩 Prompts Usados

- Necesito crear un taller de visualización 360° en Unity que permita cargar imágenes panorámicas equirectangulares y videos 360° en esferas invertidas. El sistema debe incluir un manager que alterne entre imagen y video usando un slider, con controles automáticos de reproducción y pausa. ¿Podrías ayudarme a estructurar el código con un sistema modular que gestione ambos tipos de contenido multimedia de forma eficiente?

---

## 💬 Reflexión Final

A través de este taller, se exploró cómo Unity facilita la creación de experiencias inmersivas mediante contenido 360°, abriendo posibilidades para aplicaciones en realidad virtual, tours virtuales, visualización arquitectónica y experiencias educativas envolventes. La comprensión de técnicas de proyección esférica y gestión de multimedia sienta las bases para el desarrollo de aplicaciones XR más complejas y experiencias interactivas de próxima generación.

---
