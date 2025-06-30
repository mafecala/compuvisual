# 🎮 Motion Design Interactivo: Acciones Visuales según Eventos del Usuario

## 📅 Fecha
2025-06-29 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Crear animaciones reactivas donde un **modelo 3D animado (proveniente de Mixamo)** responde a eventos del usuario, como clics, teclas o movimientos del cursor. El objetivo es introducir los fundamentos del motion design aplicado a personajes, integrando eventos y lógica de interacción con animaciones esqueléticas.

---

## 🧠 Conceptos Aprendidos

- Fundamentos de animación esquelética y sistemas de rigging en Unity.
- Integración de modelos humanoides de Mixamo con múltiples animaciones.
- Configuración de Animator Controllers con states, transitions y parámetros.
- Manejo de eventos de entrada del usuario (teclado, mouse, touch) para triggear animaciones.
- Implementación de máquinas de estados finitos para control de animaciones.
- Uso de parámetros Bool, Trigger y Float en el sistema de animación de Unity.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- Mixamo (modelos y animaciones humanoides)
- C# Scripting
- Animator Controller y Animation Window
- Sistema de Input de Unity (Input Manager)
- Modelos en formato FBX con rigging completo

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Descarga e importación de personaje animado desde Mixamo (formato FBX).
2. Configuración del Animator Controller con estados base (Idle, Walk, Wave, Dance, Jump).
3. Creación de transiciones entre estados con condiciones específicas.
4. Implementación del script de control de entrada para capturar eventos del usuario.
5. Mapeo de teclas específicas a triggers y parámetros del animador.
6. Testing y refinamiento de transiciones para lograr fluidez visual.

### 🔹 Código relevante

```csharp
// Sistema de control de animaciones basado en input del usuario
void Update()
{
    // Disparo animación Wave al presionar A
    if (Input.GetKeyDown(KeyCode.A))
    {
        animator.SetTrigger("Wave");
    }

    // Disparo animación Dancing al presionar Espacio
    if (Input.GetKeyDown(KeyCode.Space))
    {
        animator.SetTrigger("Dance");
    }

    // Activo Walk mientras se mantenga presionada la tecla W
    if (Input.GetKey(KeyCode.W))
    {
        animator.SetBool("IsWalking", true);
    }
    else
    {
        animator.SetBool("IsWalking", false);
    }
}
```

---

## 📊 Resultados Visuales

El sistema de motion design interactivo permite observar cómo el personaje responde dinámicamente a las acciones del usuario:

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-06-24-Taller22_Motion_Design/Unity/GifMotionDesign.gif)

- **Tecla A:** El personaje ejecuta una animación de saludo (Wave) y regresa al estado Idle
- **Tecla Espacio:** Activa la animación de baile (Dance) con transición suave
- **Tecla W (Mantenida):** El personaje camina continuamente mientras se mantiene presionada
- **Estado Idle:** Animación por defecto cuando no hay input activo
- **Transiciones Fluidas:** Todas las animaciones se conectan de manera natural sin cortes abruptos

**Nota:** El sistema responde en tiempo real y permite combinaciones de inputs para crear secuencias de animación más complejas.

---

## 🧩 Prompts Usados

- Necesito crear un sistema de motion design interactivo en Unity donde un personaje de Mixamo responda a eventos del usuario. El objetivo es que diferentes teclas activen animaciones específicas como caminar, saludar, bailar y saltar. ¿Podrías ayudarme a estructurar el Animator Controller y el script de control de input para lograr transiciones fluidas entre estados de animación?

---

## 💬 Reflexión Final

A través de este taller, se logró comprender los principios fundamentales del motion design interactivo aplicado a personajes 3D. La integración entre el sistema de input de Unity y el Animator Controller demuestra cómo crear experiencias inmersivas donde el usuario puede influir directamente en el comportamiento visual del personaje. Este conocimiento es esencial para el desarrollo de videojuegos, aplicaciones interactivas y experiencias de realidad virtual donde la respuesta visual inmediata a las acciones del usuario es crucial para la engagement y la experiencia del usuario.

---