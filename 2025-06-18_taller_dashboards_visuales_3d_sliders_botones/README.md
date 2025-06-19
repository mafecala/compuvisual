# 🧪 Taller - Control Interactivo de Objetos 3D con React Three Fiber

## 📅 Fecha

2025-05-17

## 🌷 Equipo de trabajo

**Mi grupo está conformado por:**

-   Julián Ramírez Díaz (julramirezdi@unal.edu.co)
    
-   Julián David Rincón Orjuela (jurinconor@unal.edu.co)
    
-   María Fernanda Cala Rodríguez (mcalar@unal.edu.co)
    

**Este taller fue realizado por:**

-   María Fernanda Cala Rodríguez (mcalar@unal.edu.co)
    

## 🎯 Objetivo del Taller

El objetivo de este taller es explorar la creación de escenas interactivas en 3D utilizando **React Three Fiber** y **Leva** para modificar dinámicamente propiedades de los objetos en tiempo real. Se trabajó con geometrías simples (caja, esfera, torus) y se implementaron controles visuales para cambiar su **escala**, **color**, **tipo de material**, **rotación automática** y **propiedades de la luz** (intensidad, color, posición).

## 🧠 Conceptos Aprendidos

✅ Uso de React Three Fiber para crear y renderizar escenas 3D  
✅ Integración de Leva para controles visuales en tiempo real  
✅ Control de escala, color y materiales de objetos 3D  
✅ Activación de rotación automática mediante booleanos  
✅ Alternancia entre materiales estándar y Phong  
✅ Manipulación de luces en escena (color, intensidad, posición)  
✅ Reactividad directa de los controles sobre las propiedades del objeto  
✅ Práctica de `useFrame`, `useRef` y `useControls` en un flujo interactivo

## 🔧 Herramientas y Entornos

-   React
    
-   Three.js
    
-   React Three Fiber
    
-   @react-three/drei
    
-   Leva (para interfaz de control interactiva)
    

## 📁 Estructura del Proyecto

2025-06-18_taller_dashboards_visuales_3d_sliders_botones/

├── threejs/
  ├── src/
│   ├── App.jsx
│   └── styles.css
├── public/
│   └── index.html
├── README.md


## 🧩 Funcionalidad Implementada

Característica

Descripción

Objeto 3D

Caja (`Box`) con posibilidad de cambiar a otras geometrías (opcional)

Control de escala

Slider para escalar uniformemente el objeto

Cambio de color

Selector de color para el material del objeto

Cambio de material

Opción entre `Standard` y `Phong`

Rotación automática

Botón toggle que activa una rotación en el eje Y

Luz editable

Sliders para modificar intensidad, color y posición de una `PointLight`

Visualización interactiva

`OrbitControls` para manipular la cámara libremente

## 🔍 Vista previa

![Demo](demo.gif)

## 🔹 Código Relevante

```
// src/App.jsx (fragmento)
function Box() {
  const meshRef = useRef()
  const [autoRotate, setAutoRotate] = useState(false)

  const { scale, color, rotate, material } = useControls({
    scale: { value: 1, min: 0.1, max: 3 },
    color: '#ff0000',
    rotate: { label: 'Auto Rotate', value: false, onChange: setAutoRotate },
    material: { options: ['Standard', 'Phong'] }
  })

  const { lightColor, intensity, position } = useControls('Light', {
    lightColor: '#ffffff',
    intensity: { value: 1, min: 0, max: 5 },
    position: { value: { x: 5, y: 5, z: 5 } }
  })

  useFrame(() => {
    if (autoRotate && meshRef.current) {
      meshRef.current.rotation.y += 0.01
    }
  })

  const Material = material === 'Phong' ? <meshPhongMaterial color={color} /> : <meshStandardMaterial color={color} />

  return (
    <>
      <pointLight position={[position.x, position.y, position.z]} intensity={intensity} color={lightColor} />
      <mesh ref={meshRef} scale={scale}>
        <boxGeometry args={[1, 1, 1]} />
        {Material}
      </mesh>
    </>
  )
}
```

## ✨ Experiencia de Usuario

Gracias a la interfaz de Leva, el usuario puede:

-   Cambiar el color del objeto de forma instantánea.
    
-   Ajustar su escala para hacerlo más grande o pequeño.
    
-   Activar/desactivar su rotación automática.
    
-   Alternar entre materiales para ver diferencias visuales.
    
-   Modificar la luz para entender cómo afecta el sombreado y la apariencia del material.
    

## 🤖 Prompt Utilizado

GPT4o:
```
Crear una escena con al menos un objeto 3D (Box, Sphere o Torus).
Usar leva o dat.GUI para crear:

- Un slider que controle la escala del objeto  (scale).
- Un slider de color  (material.color).
- Un botón que cambie entre materiales o aplique una rotación automática.

Enlazar cada control directamente a la propiedad del objeto con useControls() o GUI.add(...).

Bonus: Agregar control sobre la luz  (intensidad, color o posición).` 

```

## 💬 Reflexión Final

Este taller mostró lo poderosa que puede ser la combinación de **Three.js**, **React Three Fiber** y **Leva** para construir interfaces gráficas interactivas. Pudimos experimentar con cómo **las propiedades visuales de un objeto 3D** pueden ser controladas en tiempo real sin recargar la página ni re-renderizar todo el sistema.

Este tipo de interacción es común en **editores 3D**, **visualizadores científicos**, **configuradores de productos en línea** y **herramientas creativas**. Dominar estos conceptos sienta una base sólida para el desarrollo de experiencias 3D modernas en la web.