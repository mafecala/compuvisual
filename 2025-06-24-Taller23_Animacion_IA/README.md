# 🤖 Animación con AI en Unity para Personajes Autónomos

## 📅 Fecha
2025-06-24 – Fecha de entrega

---

## 🎯 Objetivo del Taller

Explorar técnicas básicas para implementar **comportamientos autónomos** en personajes dentro de Unity, utilizando componentes de inteligencia artificial como sistemas de navegación, detección de obstáculos, decisiones reactivas y control de animaciones en tiempo real para crear NPCs (Non-Playable Characters) inteligentes.

---

## 🧠 Conceptos Aprendidos

- **IA en videojuegos** para simular comportamientos inteligentes en NPCs autónomos.
- **NavMesh** como sistema de navegación para desplazamientos realistas y evasión de obstáculos.
- **NavMeshAgent** para control de movimiento automático y pathfinding dinámico.
- **Máquinas de estados** para gestionar transiciones entre comportamientos (patrullaje, persecución, idle).
- **Algoritmos de detección** basados en distancia, ángulo de visión y raycast para awareness del entorno.
- Integración entre sistemas de IA y Animator Controllers para animaciones contextuales.

---

## 🔧 Herramientas y Entornos

- Unity (versión LTS)
- NavMesh System y Navigation Panel
- C# Scripting para lógica de IA
- Mixamo (modelos humanoides con rigging)
- Animator Controller y Animation Blending
- Physics Raycast y Collision Detection

---

## 🧪 Implementación en Unity

### 🔹 Flujo General
1. Configuración del entorno con terreno, obstáculos y generación de NavMesh.
2. Importación de personaje 3D con rigging y configuración de NavMeshAgent.
3. Implementación de sistema de patrullaje automático entre waypoints.
4. Desarrollo de sistema de detección de jugador con cono de visión y raycast.
5. Creación de máquina de estados para alternar entre comportamientos (patrulla/persecución).

### 🔹 Código relevante

```csharp
// Sistema de detección inteligente con cono de visión y raycast
bool PuedeVerJugador()
{
    Vector3 origen = transform.position + Vector3.up*0.8f;
    Vector3 destino = jugador.position + Vector3.up *0.8f;
    Vector3 direccion = destino - origen;
    float distancia = direccion.magnitude;

    if (distancia > rangoVision)
        return false;

    float angulo = Vector3.Angle(transform.forward, direccion.normalized);
    if (angulo > anguloVision / 2f)
        return false;

    // Aquí solo hacemos raycast si ya está dentro del cono
    if (Physics.Linecast(origen, destino, out RaycastHit hit))
    {
        if (hit.collider.CompareTag("Player"))
        {
            return true;
        }
    }

    return false;
}
```

---

## 📊 Resultados Visuales

El sistema de IA autónoma permite observar comportamientos emergentes y realistas en el NPC:

> ![Muestra del funcionamiento en Unity](https://github.com/Jul1014/Compuvisual-General/blob/master/2025-06-24-Taller23_Animacion_IA/Unity/GifAnimacionIA.gif)

- **Modo Patrullaje:** El NPC se desplaza automáticamente entre waypoints predefinidos usando NavMesh
- **Detección de Jugador:** Sistema de cono de visión que activa la persecución cuando detecta al player
- **Persecución Inteligente:** El agente sigue al jugador evitando obstáculos y recalculando rutas dinámicamente
- **Animaciones Contextuales:** Transiciones fluidas entre walk y run

**Nota:** El comportamiento del NPC emerge de la combinación de múltiples sistemas (navegación, detección, animación) creando una experiencia de IA convincente.

---

## 🧩 Prompts Usados

- Necesito crear un sistema de IA básica en Unity donde un NPC tenga comportamientos autónomos como patrullar, detectar al jugador y perseguirlo. El personaje debe usar NavMesh para moverse, tener un sistema de detección basado en cono de visión con raycast, y sincronizar sus animaciones con sus acciones. ¿Podrías ayudarme a estructurar una máquina de estados simple que gestione estos comportamientos de forma fluida?

---

## 💬 Reflexión Final

A través de este taller, se logró comprender los fundamentos de la inteligencia artificial aplicada a personajes en videojuegos. La combinación de NavMesh, sistemas de detección y máquinas de estados demuestra cómo crear NPCs que sienten vivos y responden de manera creíble al entorno y al jugador. Este conocimiento es fundamental para el desarrollo de videojuegos inmersivos, desde enemigos inteligentes hasta compañeros de equipo autónomos, sentando las bases para sistemas de IA más complejos como behavior trees y redes neuronales aplicadas a gaming.

---