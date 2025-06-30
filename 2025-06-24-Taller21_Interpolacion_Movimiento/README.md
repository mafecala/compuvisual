# 🎭 Interpolación de Movimiento: Suavizando Animaciones en Tiempo Real

## 📅 Fecha
2025-06-24 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Implementar técnicas de interpolación (LERP, SLERP, Bézier) para crear animaciones suaves y naturales en objetos 3D mediante control preciso del paso del tiempo y la transición entre estados. El objetivo es dominar diferentes métodos de interpolación para lograr efectos realistas como aceleración, desaceleración y movimientos curvos, proporcionando herramientas fundamentales para crear animaciones procedurales de alta calidad visual.

---

## 🧠 Conceptos Aprendidos

- Fundamentos de **interpolación matemática** y su aplicación en animaciones 3D.
- Comprensión de **LERP** (Linear Interpolation) para transiciones lineales de posición.
- Dominio de **SLERP** (Spherical Linear Interpolation) para rotaciones suaves.
- Implementación de **curvas de suavizado** con AnimationCurve y Mathf.SmoothStep.
- Control preciso del **tiempo normalizado** (0-1) para animaciones consistentes.
- Técnicas de **easing** (ease in/out) para aceleración y desaceleración natural.
- Visualización en tiempo real de **trayectorias** y **indicadores temporales**.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- Vector3.Lerp y Quaternion.Slerp
- AnimationCurve System
- UI System (Text Components)
- Mathf Functions (SmoothStep, Clamp01)
- Time.deltaTime para independencia de framerate

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Configuración de puntos de inicio y final para la interpolación de movimiento.
2. Implementación de interpolación lineal (LERP) para transición suave de posición.
3. Integración de interpolación esférica (SLERP) para rotaciones naturales.
4. Aplicación de curvas de suavizado personalizables mediante AnimationCurve.
5. Sistema de visualización en tiempo real con indicadores de progreso temporal.
6. Controles interactivos para reinicio y experimentación con diferentes curvas.

### 🔹 Código relevante

```csharp
    void Update()
    {
        
        tiempo += Time.deltaTime;
        float t = Mathf.Clamp01(tiempo / duracion);
        float tCurvado = curvaSuavizado.Evaluate(t);

        if (textoTiempo != null && duracion>tiempo)
        {
            textoTiempo.text = $"{tiempo:F2}s";
        }

        transform.position = Vector3.Lerp(puntoInicio.position, puntoFinal.position, tCurvado);

        // Interpolación de rotación suave
        Quaternion rotInicial = Quaternion.identity;
        Quaternion rotFinal = Quaternion.Euler(0, 180, 0);
        transform.rotation = Quaternion.Slerp(rotInicial, rotFinal, tCurvado);

        if (Input.GetKeyDown("space"))
        {
            tiempo = 0f;
        }
    }
```

---

## 📊 Resultados Visuales

El sistema proporciona una experiencia completa para comprender la interpolación de movimiento:
- **Visualización Clara:** Objeto moviéndose suavemente entre puntos
- **Control Temporal:** Indicadores en tiempo real de duración de animación
- **Curvas Personalizables:** AnimationCurve permite experimentar con diferentes tipos de easing
- **Interactividad Completa:** Controles para reiniciar la animación

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-06-24-Taller21_Interpolacion_Movimiento/Unity/GifInterpolacionMov.gif)

La experiencia permite experimentar directamente con diferentes tipos de interpolación, observar el impacto visual de las curvas de suavizado y comprender cómo el control temporal afecta la percepción de naturalidad en las animaciones. Los controles interactivos facilitan la comparación entre configuraciones.

**Nota:** El uso de AnimationCurve proporciona flexibilidad total para crear efectos de easing personalizados, desde movimientos lineales hasta bounces complejos y transiciones orgánicas.

---

## 🧩 Prompts Usados

- Necesito crear un taller de interpolación de movimiento en Unity que enseñe técnicas LERP, SLERP y curvas de suavizado para animaciones naturales. Debe incluir movimiento suave entre puntos usando Vector3.Lerp, rotación con Quaternion.Slerp, curvas personalizables con AnimationCurve, visualización de trayectoria, indicadores de tiempo en UI, y controles interactivos para reiniciar y experimentar con diferentes velocidades y tipos de easing. ¿Podrías ayudarme a estructurar el código para crear una experiencia educativa completa sobre interpolación matemática aplicada a animaciones 3D?

---

## 💬 Reflexión Final

A través de este taller, se adquirió una comprensión profunda de las técnicas de interpolación, herramientas fundamentales para crear animaciones convincentes y naturales en aplicaciones 3D. Esta habilidad es esencial en el desarrollo de videojuegos, aplicaciones interactivas, visualizaciones arquitectónicas y experiencias inmersivas, donde la suavidad y naturalidad del movimiento determinan en gran medida la calidad percibida y la credibilidad de la experiencia digital, desde transiciones de UI hasta animaciones de personajes complejas.

---