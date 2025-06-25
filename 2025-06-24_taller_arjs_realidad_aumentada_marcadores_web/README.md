# 🎯 Taller - Introducción a Realidad Aumentada Web: Marcadores con AR.js

## 📅 Fecha  
**2025-06-21**

---

## 🌷 Equipo de trabajo

**Mi grupo está conformado por:**

- Julián Ramírez Díaz (julramirezdi@unal.edu.co)  
- Julián David Rincón Orjuela (jurinconor@unal.edu.co)  
- María Fernanda Cala Rodríguez (mcalar@unal.edu.co)

**Este taller fue realizado por:**

- María Fernanda Cala Rodríguez (mcalar@unal.edu.co)

---

## 🎯 Objetivo del Taller

Implementar una experiencia básica de realidad aumentada basada en marcadores directamente desde el navegador, usando AR.js y Three.js. El objetivo fue proyectar un modelo 3D personalizado sobre un marcador y activar una animación rotativa cuando este es detectado, todo sin necesidad de instalar aplicaciones móviles.

---

## 🧠 Conceptos Aplicados

- ✅ Uso de AR.js sobre A-Frame
- ✅ Integración de modelos 3D en formato `.glb`
- ✅ Detección de marcadores personalizados (`.patt`)
- ✅ Animaciones en entidades A-Frame
- ✅ Eventos de detección (`markerFound`, `markerLost`)
- ✅ Escena 3D embebida con cámara AR

---

## 🛠️ Herramientas Utilizadas

- HTML5 + JavaScript
- [A-Frame](https://aframe.io/)
- [AR.js (aframe-ar)](https://github.com/AR-js-org/AR.js)
- Navegador moderno con acceso a cámara (Chrome, Firefox)

---

## 📁 Estructura del Proyecto

```
yyyy-mm-dd_taller_arjs_realidad_aumentada_marcadores_web/
├── index.html
├── models/
│   └── modelo.glb
├── markers/
│   └── marcador.patt
├── demo.gif
├── README.md
```

---

## 🔧 Fragmento Clave del Código

```html
<a-marker type="pattern" url="marcador.patt" markerhandler>
  <a-entity gltf-model="url(modelo.glb)"
            position="0 0.5 0"
            scale="2 2 2"
            animation="property: rotation; to: 0 360 0; loop: true; dur: 5000">
  </a-entity>
</a-marker>
```

```javascript
AFRAME.registerComponent('markerhandler', {
  init: function () {
    const marker = this.el;
    marker.addEventListener('markerFound', () => {
      console.log('📍 ¡Marcador detectado!');
    });
    marker.addEventListener('markerLost', () => {
      console.log('❌ Marcador perdido.');
    });
  }
});
```

---

## 📊 Demostraciones

![demo](demo.gif)

---

## 🧠 Prompts Utilizados

GPT-4o:
```
Crea una experiencia AR web usando AR.js y A-Frame donde:
- Se detecte un marcador personalizado
- Al detectar el marcador, se muestre un modelo .glb rotando
- Se registren eventos cuando el marcador aparece o desaparece
- Todo funcione embebido en HTML
```

GPT-4o:
```
Genera un README.md completo para un taller titulado "Introducción a Realidad Aumentada Web con AR.js".
Debe incluir: título, fecha, equipo, objetivo, herramientas, conceptos aplicados, estructura, fragmentos de código, demo, reflexión final y prompts.
```

---

## 💡 Reflexión Final

Este taller permitió explorar la facilidad con la que se puede desplegar una experiencia de realidad aumentada desde el navegador, sin instalaciones adicionales. El sistema basado en AR.js y A-Frame permitió cargar modelos personalizados, detectar marcadores físicos y ejecutar animaciones.

Una limitación importante es la dependencia de una buena iluminación y estabilidad de la cámara para que el marcador sea reconocido correctamente. En contextos educativos o artísticos, esta tecnología puede ser útil para enriquecer materiales impresos, crear instalaciones interactivas o desarrollar recursos pedagógicos accesibles.

