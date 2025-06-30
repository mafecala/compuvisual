# 🧍‍♂️ Avatares Virtuales: Integración y Personalización en Unity

## 📅 Fecha
2025-06-24 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Aprender a integrar **avatares 3D** en entornos interactivos usando Unity, permitiendo su visualización, personalización básica y movimiento mediante entradas del usuario o animaciones predefinidas. El objetivo es comprender el flujo completo desde la importación de modelos de avatar hasta su personalización visual y control de animaciones, creando una experiencia interactiva que sirva como base para aplicaciones de realidad virtual, videojuegos o aplicaciones sociales.

---

## 🧠 Conceptos Aprendidos

- Comprensión fundamental de **avatares virtuales** y su rol en experiencias digitales.
- Dominio de formatos de modelos 3D: `.GLB`, `.GLTF`, `.FBX`, `.VRM` y sus características.
- Importación y configuración correcta de modelos con **esqueleto** desde plataformas como **Mixamo**.
- Implementación de **personalización visual** mediante controles de color dinámicos.
- Configuración de **Animator Controller** para reproducción automática de animaciones.
- Integración de **UI interactiva** con sliders para modificación en tiempo real.
- Configuración de **iluminación** y **escenarios** para presentación óptima de avatares.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- Animator Controller System
- UI System (Slider Components)
- Lighting System
- Mixamo Platform (avatares y animaciones)
- Modelos 3D (.FBX, .GLB, .GLTF, .VRM)

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Importación de avatar 3D con esqueleto desde Mixamo en formato `.FBX` o `.GLB`.
2. Configuración del modelo en escena con iluminación adecuada para visualización.
3. Configuración del Animator Controller para reproducción automática de animaciones.
4. Implementación de sistema de personalización visual mediante controles de color RGB.
5. Creación de interfaz interactiva con sliders para modificación en tiempo real.
6. Integración completa avatar-escena-controles para experiencia fluida.

### 🔹 Código relevante

```csharp
public class ColorControlller : MonoBehaviour
{
    public Slider sliderR, sliderG, sliderB;
    public Renderer targetRenderer;

    void Update()
    {
        Color newColor = new Color(sliderR.value, sliderG.value, sliderB.value);
        targetRenderer.material.color = newColor;
    }
}
```

---

## 📊 Resultados Visuales

El sistema proporciona una experiencia completa de integración de avatares virtuales:
- **Visualización Óptima:** Avatar correctamente iluminado y posicionado en escena 3D
- **Personalización Interactiva:** Sliders RGB permiten modificación de color en tiempo real
- **Animación Automática:** Reproducción fluida de animaciones predefinidas (caminar, saludar)
- **Control Dinámico:** Cambios inmediatos reflejados visualmente sin interrupciones

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-06-24-Taller20_Avatares_Virtuales/Unity/GifAvataresVirtuales.gif)

La experiencia permite experimentar con diferentes configuraciones de color, observar el comportamiento de las animaciones y comprender la integración completa entre modelo 3D, sistema de animación y controles de usuario. La interfaz intuitiva facilita la exploración de posibilidades de personalización.

**Nota:** El uso de modelos de Mixamo garantiza compatibilidad con el sistema humanoide de Unity y proporciona animaciones de calidad profesional para una experiencia más realista.

---

## 🧩 Prompts Usados

- Necesito crear un taller de avatares virtuales en Unity que enseñe a integrar modelos 3D de personajes con personalización básica y animaciones. Debe incluir la importación de avatares desde Mixamo en formato .FBX o .GLB, configuración de iluminación de escena, sistema de personalización visual con sliders RGB para cambio de color, y reproducción automática de animaciones como caminar o saludar. ¿Podrías ayudarme a estructurar el código para crear una experiencia completa de avatar virtual interactivo?

---

## 💬 Reflexión Final

A través de este taller, se adquirió una comprensión práctica de la integración de avatares virtuales, una habilidad fundamental en el desarrollo de aplicaciones interactivas modernas. Esta técnica es esencial para crear experiencias inmersivas en videojuegos, aplicaciones de realidad virtual y aumentada, plataformas sociales virtuales y aplicaciones de capacitación, donde la representación digital del usuario y su personalización determinan en gran medida el nivel de engagement y la conexión emocional con la experiencia digital.

---