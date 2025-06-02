# 🎮 Sistema de Input y UI Interactiva en Unity

## 📅 Fecha
2025-05-26 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Aprender a capturar y procesar **entradas del usuario** (mouse, teclado, touch) e implementar interfaces visuales (UI) que permitan interacción dinámica en **Unity**. Este taller es clave para desarrollar aplicaciones interactivas, videojuegos o experiencias XR, proporcionando las bases fundamentales para crear experiencias de usuario fluidas y responsivas.

---

## 🧠 Conceptos Aprendidos

- Captura de entradas múltiples: teclado (`WASD`), mouse (clicks y movimiento) y controles táctiles.
- Sistema de movimiento de primera persona con física realista usando `Rigidbody`.
- Implementación de controles de cámara con rotación horizontal y vertical limitada.
- Creación de interfaces UI dinámicas con `Canvas`, `Text`, `Button` y `Slider`.
- Integración de sistemas de entrada con elementos de interfaz para feedback visual.
- Gestión de estados de juego mediante interacciones del usuario.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- C# Scripting
- Input System (clásico)
- UI System (Canvas, Button, Slider, Text)
- Physics System (Rigidbody, ForceMode)

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Configuración de personaje/cámara con componente Rigidbody para física realista.
2. Implementación de sistema de movimiento WASD con velocidad constante.
3. Controles de mouse para rotación de jugador (horizontal) y cámara (vertical).
4. Sistema de salto mediante click izquierdo con aplicación de fuerza impulsiva.
5. Creación de Canvas UI con elementos informativos y controles interactivos.
6. Sincronización entre acciones del jugador y retroalimentación visual en la interfaz.

### 🔹 Código relevante

```csharp
// Sistema completo de movimiento y rotación de cámara con física
void Update()
{
    // Movimiento normal (sin AddForce)
    float horizontal = Input.GetAxis("Horizontal");
    float vertical = Input.GetAxis("Vertical");
    Vector3 moveDirection = transform.right * horizontal + transform.forward * vertical;
    Vector3 moveVelocity = moveDirection * moveSpeed;
    Vector3 currentVelocity = rb.velocity;
    rb.velocity = new Vector3(moveVelocity.x, currentVelocity.y, moveVelocity.z);

    // Salto con clic izquierdo (AddForce)
    if (Input.GetMouseButtonDown(0))
    {
        rb.AddForce(transform.up * jumpForce, ForceMode.Impulse);
    }

    // Rotación horizontal del jugador
    float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity * Time.deltaTime;
    transform.Rotate(Vector3.up * mouseX);

    // Rotación vertical de la cámara
    float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity * Time.deltaTime;
    rotationY -= mouseY;
    rotationY = Mathf.Clamp(rotationY, -90f, 90f);
    cameraTransform.localRotation = Quaternion.Euler(rotationY, 0f, 0f);
}
```

---

## 📊 Resultados Visuales

El sistema implementa un control de primera persona completo y responsivo:
- **Movimiento WASD:** Desplazamiento fluido en todas las direcciones con física realista
- **Control de Mouse:** Rotación libre horizontal del jugador y vertical limitada de la cámara
- **Sistema de Salto:** Mecánica de salto mediante click con aplicación de fuerza física
- **UI Dinámica:** Interfaz que muestra coordenadas, estado del jugador y controles interactivos

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-05-26-Taller14_Input_Interfaz/Unity/GifInputInterfaz.gif)

La experiencia combina controles intuitivos con retroalimentación visual inmediata, creando una base sólida para aplicaciones interactivas más complejas. Los elementos UI se actualizan en tiempo real reflejando el estado del sistema de entrada.

**Nota:** El sistema mantiene la velocidad vertical del Rigidbody para preservar la física de gravedad mientras permite control directo del movimiento horizontal.

---

## 🧩 Prompts Usados

- Necesito crear un taller de sistemas de entrada e interfaz de usuario en Unity. Debe incluir movimiento WASD con Rigidbody, controles de mouse para rotación de jugador y cámara, sistema de salto con click, y una UI dinámica con Canvas que muestre información del estado y permita interacciones. ¿Podrías ayudarme a estructurar el código de manera que integre smoothly los inputs con la física y la interfaz de usuario?

---

## 💬 Reflexión Final

A través de este taller, se establecieron los fundamentos esenciales para crear experiencias interactivas en Unity, combinando sistemas de entrada robustos con interfaces de usuario dinámicas. Esta base permite el desarrollo de videojuegos, aplicaciones educativas y experiencias XR más complejas, donde la respuesta fluida a las acciones del usuario es fundamental para crear experiencias envolventes y satisfactorias.

---
