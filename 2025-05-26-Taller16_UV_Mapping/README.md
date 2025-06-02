# 🗺️ UV Mapping: Texturas que Encajan

## 📅 Fecha
2025-05-30 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Explorar el mapeo UV como técnica fundamental para aplicar correctamente texturas 2D sobre modelos 3D sin distorsión. El objetivo es entender cómo se proyectan las texturas y cómo se pueden ajustar las coordenadas UV para mejorar el resultado visual, dominando una de las habilidades más importantes en el pipeline de producción 3D.

---

## 🧠 Conceptos Aprendidos

- Fundamentos del **mapeo UV** y su importancia en la aplicación de texturas 3D.
- Comprensión de coordenadas UV como sistema de proyección de texturas 2D a superficies 3D.
- Identificación y corrección de errores comunes: texturas estiradas, giradas o mal escaladas.
- Uso de texturas de prueba tipo **checkerboard** para diagnóstico visual de mapeo UV.
- Control dinámico de **Tiling** y **Offset** para ajuste fino de texturas en tiempo real.
- Workflow de importación de modelos `.OBJ` y `.GLTF` con coordenadas UV preservadas.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- Material System (mainTextureScale, mainTextureOffset)
- UI System (Slider Components)
- Modelos 3D (.OBJ, .GLTF)
- Texturas de diagnóstico (Checkerboard)

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Importación de modelo 3D con coordenadas UV correctamente configuradas.
2. Aplicación de textura checkerboard para diagnóstico visual de mapeo UV.
3. Identificación de problemas de proyección: estiramiento, rotación, escalado incorrecto.
4. Implementación de controles interactivos para ajuste de Tiling (repetición de textura).
5. Sistema de Offset para desplazamiento de textura en coordenadas U y V.
6. Comparación visual entre diferentes configuraciones para optimizar el resultado.

### 🔹 Código relevante

```csharp
// Control dinámico de Tiling y Offset para ajuste UV en tiempo real
void Update()
{
    if (targetMaterial != null)
    {
        // Actualizar tiling (repetición de textura)
        Vector2 tiling = new Vector2(tilingXSlider.value, tilingYSlider.value);
        targetMaterial.mainTextureScale = tiling;
       
        // Actualizar offset (desplazamiento de textura)
        Vector2 offset = new Vector2(offsetXSlider.value, offsetYSlider.value);
        targetMaterial.mainTextureOffset = offset;
    }
}
```

---

## 📊 Resultados Visuales

El sistema proporciona una experiencia educativa completa para comprender el mapeo UV:
- **Diagnóstico Visual:** Textura checkerboard revela inmediatamente problemas de proyección UV
- **Control de Tiling:** Sliders X e Y permiten ajustar la repetición de textura independientemente
- **Control de Offset:** Desplazamiento preciso en ambas direcciones UV para alineación perfecta
- **Feedback Inmediato:** Cambios en tiempo real muestran el impacto de cada ajuste

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-05-26-Taller16_UV_Mapping/Unity/GifUVMapping.gif)

La experiencia permite identificar rápidamente distorsiones, áreas mal mapeadas y optimizar la aplicación de texturas. Los controles interactivos facilitan la experimentación para encontrar la configuración ideal de cada modelo.

**Nota:** El uso de texturas checkerboard es una técnica estándar en la industria para verificar la calidad del mapeo UV antes de aplicar texturas finales.

---

## 🧩 Prompts Usados

- Necesito crear un taller de UV mapping en Unity que enseñe a aplicar correctamente texturas 2D sobre modelos 3D. Debe incluir la importación de modelos con coordenadas UV, uso de texturas checkerboard para diagnóstico, identificación de problemas de distorsión, y controles UI con sliders para ajustar Tiling y Offset en tiempo real. ¿Podrías ayudarme a estructurar el código para permitir experimentación interactiva con las propiedades de mapeo UV?

---

## 💬 Reflexión Final

A través de este taller, se adquirió una comprensión práctica del mapeo UV, una habilidad fundamental en el desarrollo 3D. Esta técnica es esencial para crear contenido visual de calidad profesional, desde videojuegos hasta visualización arquitectónica y experiencias XR, donde la correcta aplicación de texturas determina en gran medida el realismo y la calidad visual del resultado final.

---
