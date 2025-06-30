# 🎮 Cinemática Inversa: Haciendo que el Modelo Persiga Objetivos

## 📅 Fecha
2025-06-24 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Aplicar cinemática inversa (**IK, Inverse Kinematics**) para que un modelo 3D alcance un punto objetivo dinámico, como una mano intentando tocar una esfera. Este ejercicio permite comprender cómo una cadena de articulaciones puede ajustarse automáticamente para alcanzar una posición deseada usando algoritmos como CCD (Cyclic Coordinate Descent).

---

## 🧠 Conceptos Aprendidos

- Fundamentos de cinemática inversa y su diferencia con la cinemática directa.
- Implementación del algoritmo **CCD (Cyclic Coordinate Descent)** paso a paso.
- Creación y manejo de cadenas cinemáticas jerárquicas en Unity.
- Control de iteraciones y tolerancias para optimizar el rendimiento del solver.
- Aplicación de pesos y limitaciones angulares para obtener movimientos más naturales.
- Visualización de trayectorias y debugging de sistemas IK complejos.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- Sistema de componentes Unity (Transform, Debug.DrawLine)
- Jerarquías de GameObjects para cadenas cinemáticas
- UI Canvas para controles interactivos

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Configuración de jerarquía de GameObjects (`Base → Brazo → Antebrazo → Mano`).
2. Creación del objetivo móvil (esfera) que el end effector debe alcanzar.
3. Implementación del solver CCD con iteraciones controladas y tolerancia.
4. Sistema de pesos para influencia gradual en cada articulación.
5. Controles interactivos para mover el objetivo en tiempo real.
6. Visualización de la cadena cinemática y distancia al objetivo.

### 🔹 Código relevante

```csharp

void SolveIK() 
{
    for (int iteration = 0; iteration < maxIterations; iteration++)
    {
        float distanceToTarget = Vector3.Distance(endEffector.position, target.position);
        if (distanceToTarget < tolerance)
        {
            break;
        }

        for (int i = joints.Length - 1; i >= 0; i--)
        {
            Vector3 toEndEffector = endEffector.position - joints[i].position;
            Vector3 toTarget = target.position - joints[i].position;

            float angle = Vector3.Angle(toEndEffector, toTarget);
            if (angle > 0.01f)
            {
                Vector3 rotationAxis = Vector3.Cross(toEndEffector, toTarget).normalized;

                // Factor de influencia según la distancia al end effector
                float weight = (float)(i + 1) / joints.Length;

                // Clampeo del ángulo a un valor máximo por paso
                float clampedAngle = Mathf.Min(angle, maxAngleStep * weight);

                // Rotación deseada con interpolación suave
                Quaternion targetRotation = Quaternion.AngleAxis(clampedAngle, rotationAxis) * joints[i].rotation;
                joints[i].rotation = Quaternion.Slerp(joints[i].rotation, targetRotation, 0.5f);
            }
        }
    }
}
```

---

## 📊 Resultados Visuales

El sistema de cinemática inversa permite observar cómo la cadena de articulaciones se adapta dinámicamente:

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-06-24-Taller18_Cinematica_Inversa/Unity/GifCinematicaInversa.gif)

- **Modo Automático:** La cadena persigue continuamente un objetivo
- **Visualización:** Líneas de debug muestran la conexión entre end effector y objetivo

**Nota:** El solver se ejecuta en tiempo real y muestra cómo cada articulación contribuye al movimiento global para alcanzar el objetivo.

---

## 🧩 Prompts Usados

- Necesito implementar un sistema de cinemática inversa en Unity usando el algoritmo CCD. El objetivo es crear una cadena de articulaciones (como un brazo robótico) que pueda alcanzar un punto objetivo móvil. ¿Podrías ayudarme a estructurar el código con un solver eficiente que incluya control de iteraciones, tolerancias y pesos para cada articulación?

---

## 💬 Reflexión Final

A través de este taller, se logró comprender los principios fundamentales de la cinemática inversa y su aplicación práctica en Unity. El algoritmo CCD demuestra ser una solución elegante para problemas de posicionamiento automático, con aplicaciones que van desde animación procedural hasta robótica simulada. Este conocimiento sienta las bases para sistemas más complejos como full-body IK, animación facial procedural y control de personajes avanzado en videojuegos y simulaciones.

---