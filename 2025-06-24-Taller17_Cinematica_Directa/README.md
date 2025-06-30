# 🦾 Cinemática Directa: Animando Brazos Robóticos o Cadenas Articuladas

## 📅 Fecha
2025-06-24 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Aplicar conceptos de **cinemática directa (Forward Kinematics)** para animar objetos enlazados como brazos robóticos, cadenas de huesos o criaturas segmentadas. El objetivo es comprender cómo rotaciones encadenadas afectan el movimiento y la posición de cada parte en una estructura jerárquica, estableciendo las bases fundamentales para sistemas de animación más complejos.

---

## 🧠 Conceptos Aprendidos

- Fundamentos de **cinemática directa** y su aplicación en sistemas articulados jerárquicos.
- Construcción de estructuras de objetos enlazados usando jerarquías de transformaciones en Unity.
- Control de rotaciones encadenadas mediante `localRotation` y `Quaternion.Euler`.
- Aplicación de animaciones sinusoidales usando `Mathf.Sin(Time.time)` para movimiento fluido.
- Visualización de trayectorias del extremo con `Debug.DrawLine()` y marcadores de posición.
- Integración de controles UI para manipulación interactiva de ángulos articulares.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- Transform Hierarchy System
- Quaternion Mathematics
- UI System (Slider Components)

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Construcción de jerarquía articulada: `Base → Brazo1 → Brazo2 → Pinza` usando GameObjects vacíos.
2. Implementación de sistema de animación sinusoidal independiente para cada articulación.
3. Aplicación de rotaciones locales mediante `localRotation` para movimiento encadenado correcto.
4. Sistema de visualización de trayectoria del extremo para análisis de movimiento.
5. Controles UI con sliders para manipulación manual de ángulos articulares.
6. Integración de animación automática y control manual intercambiables.

### 🔹 Código relevante

```csharp
// Sistema de cinemática directa con animación sinusoidal
void AnimateArm()
{
    // Animación sinusoidal para cada articulación
    brazo1Angle = Mathf.Sin(timeCounter * 0.8f) * 45f;
    brazo2Angle = Mathf.Sin(timeCounter * 1.2f) * 60f;
    pinzaAngle = Mathf.Sin(timeCounter * 1.5f) * 90f;
}

void ApplyRotations()
{
    // Aplicar rotaciones locales a cada articulación        
    if (brazo1Transform != null)
        brazo1Transform.localRotation = Quaternion.Euler(brazo1Angle, 0, 0);
    
    if (brazo2Transform != null)
        brazo2Transform.localRotation = Quaternion.Euler(brazo2Angle, 0, 0);
    
    if (pinzaTransform != null)
        pinzaTransform.localRotation = Quaternion.Euler(0, 0, pinzaAngle);
}
```

---

## 📊 Resultados Visuales

El sistema demuestra los principios de cinemática directa de manera clara y educativa:
- **Jerarquía Articulada:** Estructura `Base → Brazo1 → Brazo2 → Pinza` con dependencias correctas
- **Animación Sinusoidal:** Cada articulación oscila con frecuencias diferentes (0.8f, 1.2f, 1.5f)
- **Rotaciones Encadenadas:** Movimiento del brazo1 afecta posición de brazo2 y pinza automáticamente
- **Visualización de Trayectoria:** Marcadores que muestran el camino recorrido por el extremo

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-06-24-Taller17_Cinematica_Directa/Unity/GifCinematicaDirecta.gif)

La experiencia permite observar cómo pequeños cambios en articulaciones proximales generan grandes movimientos en el extremo, principio fundamental de la cinemática directa. Los controles interactivos facilitan la experimentación con diferentes configuraciones angulares.

**Nota:** El uso de `localRotation` asegura que cada articulación rote en su propio espacio local, manteniendo la coherencia jerárquica del sistema.

---

## 🧩 Prompts Usados

- Necesito crear un taller de cinemática directa en Unity para animar brazos robóticos articulados. Debe incluir construcción de jerarquía de objetos enlazados, aplicación de rotaciones encadenadas usando localRotation, animación sinusoidal automática para cada articulación, visualización de trayectorias, y controles UI con sliders para manipulación manual de ángulos. ¿Podrías ayudarme a estructurar el código para demostrar claramente los principios de Forward Kinematics?

---

## 💬 Reflexión Final

A través de este taller, se estableció una comprensión sólida de los principios de cinemática directa, fundamental para animación de personajes, robótica, simulaciones físicas y sistemas procedurales. Esta base permite el desarrollo de sistemas de animación más complejos como cinemática inversa, physics-based animation y herramientas de rigging avanzadas para producción 3D profesional.

---