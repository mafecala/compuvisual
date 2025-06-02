# 🎮 Modelado Procedural Básico: Geometría desde Código

## 📅 Fecha
2025-05-26 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Explorar los fundamentos del modelado procedural en Unity, aprendiendo a generar geometría de forma programática mediante código C#, desde primitivas básicas hasta mallas personalizadas, comprendiendo cómo crear contenido 3D dinámico y escalable.

---

## 🧠 Conceptos Aprendidos

- Generación programática de primitivas 3D (`Cube`, `Sphere`, `Cylinder`) usando `GameObject.CreatePrimitive()`.
- Aplicación de transformaciones mediante bucles: posición, rotación y escala.
- Creación de patrones geométricos: rejillas, espirales y estructuras fractales.
- Construcción de mallas personalizadas desde cero con `Mesh`, `Vector3[]` y arrays de triángulos.
- Organización jerárquica de objetos generados y gestión de memoria en Unity.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- Sistema de componentes Unity (Transform, MeshFilter, MeshRenderer)
- Primitivas geométricas integradas

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Configuración del script generador con parámetros públicos editables.
2. Generación de rejilla de cubos con espaciado uniforme.
3. Creación de espiral ascendente de cilindros con rotación progresiva.
4. Implementación de pirámide fractal recursiva con subdivisión.
5. Construcción de malla personalizada definiendo vértices y triángulos manualmente.
6. Sistema de limpieza y regeneración dinámica de contenido.

### 🔹 Código relevante

```csharp
// Generación de espiral de cilindros con transformaciones dinámicas
void GenerateCylinderSpiral()
{
    for (int i = 0; i < spiralCount; i++)
    {
        float angle = i * 20f * Mathf.Deg2Rad;
        float height = i * 0.5f;
        Vector3 pos = new Vector3(Mathf.Cos(angle) * spiralRadius, height, Mathf.Sin(angle) * spiralRadius);
        GameObject cylinder = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
        cylinder.transform.position = pos;
        cylinder.transform.Rotate(Vector3.up, i * 10f);
        cylinder.transform.parent = contentParent.transform;
        cylinder.GetComponent<Renderer>().material = customMaterial;
    }
}
```

---

## 📊 Resultados Visuales

El script permite visualizar diferentes patrones geométricos generados proceduralmente:

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-05-26_Taller12_Modelado_Procedural/Unity/GifModeladoProcedural.gif)

- **Modo 0:** Se eliminan los objetos
- **Modo 1:** Rejilla ordenada de cubos con espaciado uniforme
- **Modo 2:** Espiral ascendente de cilindros con rotación progresiva  
- **Modo 3:** Pirámide fractal recursiva con subdivisiones automáticas
- **Modo 4:** Malla personalizada (pirámide) construida desde vértices base

**Nota:** Los objetos se generan dinámicamente y se pueden regenerar cambiando el valor del slider en tiempo real.

---

## 🧩 Prompts Usados

- Necesito crear un taller de modelado procedural en Unity usando C#. El script debe generar primitivas como cubos, esferas y cilindros de forma programática, organizarlos en patrones como rejillas y espirales, incluir una estructura fractal recursiva, y también crear una malla personalizada desde cero definiendo vértices y triángulos. ¿Podrías ayudarme a estructurar el código de manera modular con diferentes modos de generación?

---

## 💬 Reflexión Final

A través de este taller, se pudo comprender cómo Unity permite generar contenido 3D de forma procedural, abriendo posibilidades para crear mundos dinámicos, herramientas de level design automatizado y sistemas generativos complejos. Este enfoque programático del modelado 3D sienta las bases para técnicas avanzadas como generación de terrenos, arquitectura procedural y sistemas de crafting dinámico en videojuegos.

---