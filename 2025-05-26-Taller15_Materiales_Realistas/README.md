# ✨ Materiales Realistas: Introducción a PBR en Unity

## 📅 Fecha
2025-05-28 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Comprender los principios del renderizado basado en física (PBR, *Physically-Based Rendering*) y aplicarlos a modelos 3D para mejorar su realismo visual. Este taller permite comparar cómo la luz interactúa con diferentes tipos de materiales y cómo las texturas afectan el resultado visual final, estableciendo las bases para crear contenido 3D fotorrealista.

---

## 🧠 Conceptos Aprendidos

- Fundamentos del renderizado basado en física (PBR) y su importancia en el realismo visual.
- Comprensión de los mapas de textura esenciales: **Base Color (Albedo)**, **Roughness**, **Metalness** y **Normal Map**.
- Aplicación correcta del shader `Standard (PBR)` de Unity para materiales realistas.
- Diferencias visuales entre materiales PBR completos y materiales básicos sin mapas.
- Control dinámico de propiedades de material mediante scripting y UI interactiva.
- Optimización de workflow para importación y aplicación de texturas PBR profesionales.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- Standard (PBR) Shader
- UI System (Slider Components)
- Material System y Texture Import
- Fuentes de texturas: ambientCG, PolyHaven

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Configuración de escena 3D básica con luz direccional y primitivas geométricas.
2. Importación y configuración de conjunto completo de texturas PBR profesionales.
3. Creación de material PBR usando shader Standard con mapas correctamente asignados.
4. Implementación de material de comparación básico (solo color plano).
5. Sistema de control dinámico mediante sliders para propiedades Metallic y Smoothness.
6. Análisis visual comparativo entre diferentes configuraciones de material.

### 🔹 Código relevante

```csharp
// Control dinámico de propiedades PBR en tiempo real
public class MaterialController : MonoBehaviour
{
    [Header("Material to Control")]
    public Material targetMaterial;
    
    [Header("UI Sliders")]
    public Slider metallicSlider;
    public Slider smoothnessSlider;
    
    void Update()
    {
        if (targetMaterial != null)
        {
            // Actualizar propiedades del material
            targetMaterial.SetFloat("_Metallic", metallicSlider.value);
            targetMaterial.SetFloat("_Glossiness", smoothnessSlider.value);
        }
    }
}
```

---

## 📊 Resultados Visuales

El sistema permite una comparación visual inmediata y educativa:
- **Material PBR Completo:** Textura Base Color, mapas de Roughness, Metalness y Normal Map trabajando en conjunto
- **Material Básico:** Solo color plano para contraste y comparación directa
- **Control Interactivo:** Sliders que modifican Metallic (0.0 - 1.0) y Smoothness (0.0 - 1.0) en tiempo real
- **Respuesta Visual:** Cambios instantáneos en reflexiones, especularidad y comportamiento de la luz

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-05-26-Taller15_Materiales_Realistas/Unity/GifMaterialesRealistas.gif)

La experiencia demuestra claramente cómo cada componente PBR contribuye al realismo final, desde la respuesta metálica hasta la rugosidad de superficie. Los controles interactivos permiten experimentar con diferentes combinaciones para comprender el impacto de cada parámetro.

**Nota:** Las texturas PBR de alta calidad de fuentes como PolyHaven proporcionan resultados profesionales que ilustran efectivamente los principios del renderizado físicamente correcto.

---

## 🧩 Prompts Usados

- Necesito crear un taller de introducción a PBR en Unity que demuestre los principios del renderizado basado en física. Debe incluir la importación de texturas PBR completas (Albedo, Roughness, Metalness, Normal), aplicación en el shader Standard, comparación con materiales básicos, y controles UI con sliders para modificar propiedades Metallic y Smoothness en tiempo real. ¿Podrías ayudarme a estructurar el código para que permita experimentación interactiva con los parámetros PBR?

---

## 💬 Reflexión Final

A través de este taller, se estableció una comprensión sólida de los principios PBR y su aplicación práctica en Unity. Esta base permite crear contenido 3D con mayor realismo visual, fundamental para videojuegos modernos, visualización arquivectónica, experiencias XR y cualquier aplicación que requiera representación visual convincente de materiales del mundo real.

---