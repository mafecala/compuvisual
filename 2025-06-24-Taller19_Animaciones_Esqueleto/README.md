# 🦴 Animaciones por Esqueleto: Importando y Reproduciendo Animaciones

## 📅 Fecha
2025-06-24 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Explorar las animaciones basadas en huesos (esqueleto) como técnica fundamental para dar vida a personajes 3D mediante la importación y reproducción de animaciones desde archivos externos como `.FBX` o `.GLTF`. El objetivo es comprender cómo funcionan las animaciones esqueléticas, cómo importarlas correctamente desde plataformas como Mixamo y cómo integrarlas en escenas interactivas con control dinámico de estados de animación.

---

## 🧠 Conceptos Aprendidos

- Fundamentos de **animación esquelética** y su importancia en la animación de personajes 3D.
- Comprensión de sistemas de **rig** y configuración de huesos (Humanoid vs Generic).
- Importación correcta de modelos animados desde **Mixamo** en formato `.FBX`.
- Configuración y uso del componente **Animator** y **Animator Controller**.
- Creación de **transiciones de estado** entre diferentes animaciones (idle → walk → run).
- Implementación de controles interactivos mediante **Input System** y **UI Elements**.
- Manejo de **eventos de animación** y sincronización con gameplay.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- Animator Controller System
- UI System (Button, Dropdown Components)
- Input System (GetKeyDown, GetAxis)
- Mixamo Platform (modelos y animaciones)
- Modelos 3D (.FBX, .GLTF)

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Descarga de modelo animado desde Mixamo con rig humanoide en formato `.FBX`.
2. Importación correcta en Unity verificando configuración de rig (Humanoid/Generic).
3. Configuración del Animator Controller con múltiples estados de animación.
4. Implementación de transiciones automáticas y manuales entre estados.
5. Creación de controles UI para pausar, reiniciar y cambiar animaciones.
6. Integración con Input System para control mediante teclado y interfaz.

### 🔹 Código relevante

```csharp
    public bool paused = false;

    public void SetAnimation(int index)
    {
        animator.SetInteger("animationIndex", index);
    }

    public void PauseAnimation()
    {
        paused = !paused;
        if (paused == true)
        {
            animator.speed = 0f;
        }
        else
        {
            animator.speed = 1f;
        }        
    }   
```

---

## 📊 Resultados Visuales

El sistema proporciona una experiencia completa para comprender las animaciones esqueléticas:
- **Control de Estados:** Transiciones suaves entre idle, caminar y correr mediante Animator Controller
- **Interfaz Interactiva:** Dropdown y botones para selección y control de animaciones
- **Input Responsivo:** Control mediante teclado (1-2-3 para cambiar, Space para pausar)
- **Funcionalidad Completa:** Play, pause, restart y cambio dinámico de animaciones

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-06-24-Taller19_Animaciones_Esqueleto/Unity/GifAnimacionesEsqueleto.gif)

La experiencia permite experimentar con diferentes tipos de animación, comprender el flujo de estados en el Animator Controller y dominar la integración entre animaciones y gameplay. Los controles múltiples (UI + teclado) demuestran la flexibilidad del sistema para diferentes tipos de interacción.

**Nota:** El uso de modelos de Mixamo proporciona animaciones de calidad profesional con rig humanoide estándar, ideal para aprendizaje y prototipado rápido.

---

## 🧩 Prompts Usados

- Necesito crear un taller de animaciones esqueléticas en Unity que enseñe a importar y controlar animaciones de personajes 3D desde Mixamo. Debe incluir la descarga de modelos .FBX con rig humanoide, configuración del Animator Controller con múltiples estados (idle, walk, run), transiciones entre animaciones, y controles UI con dropdown y botones para seleccionar y controlar las animaciones. También quiero integrar control por teclado para cambio rápido de estados. ¿Podrías ayudarme a estructurar el código para un sistema completo de control de animaciones esqueléticas?

---

## 💬 Reflexión Final

A través de este taller, se adquirió una comprensión práctica de las animaciones esqueléticas, una técnica fundamental en el desarrollo de videojuegos y aplicaciones 3D interactivas. Esta habilidad es esencial para crear personajes convincentes y dinámicos, desde NPCs en videojuegos hasta avatares en experiencias VR/AR, donde la calidad de las animaciones y su integración fluida con la jugabilidad determinan en gran medida la inmersión y credibilidad de la experiencia digital.

---