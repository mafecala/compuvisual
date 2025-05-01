# 🧪 Jerarquías y Transformaciones: El Árbol del Movimiento

## [](#-fecha)📅 Fecha

`2025-05-01`

----------

## [](#-objetivo-del-taller)🎯 Objetivo del Taller

El objetivo principal de este taller es comprender en profundidad las estructuras fundamentales que componen los modelos tridimensionales, específicamente las mallas poligonales. A través de la exploración práctica en diferentes entornos de desarrollo, se busca visualizar y analizar la disposición de vértices, aristas y caras, así como entender el contenido de formatos de archivo comunes como .OBJ.

----------

## [](#-conceptos-aprendidos)🧠 Conceptos Aprendidos


-   Transformaciones geométricas (escala, rotación, traslación)
-   Jerarquías de objetos 3D y transformaciones en cascada
-   Interacción en tiempo real con escenas 3D
-   Implementación de controles de usuario con Leva
-   Estructura de componentes en React Three Fiber
-   Organización de escenas 3D con grupos y mallas
----------

## [](#-herramientas-y-entornos)🔧 Herramientas y Entornos

-   Three.js



----------

## [](#-estructura-del-proyecto)📁 Estructura del Proyecto

2025-05-01_taller_jerarquias_transformaciones/
├── threejs/

----------

## [](#-implementaci%C3%B3n)🧪 Implementación (Python)


### 🔹 Etapas realizadas

1.  Creación de la estructura jerárquica con tres niveles: padre, hijo y nieto
2.  Implementación de diferentes geometrías para cada nivel de la jerarquía
3.  Desarrollo de controles interactivos usando Leva para manipular el nodo padre
4.  Visualización de transformaciones en cascada mediante animación
5.  Incorporación de ayudas visuales (ejes, grilla) para mejor comprensión espacial


### 🔹 Código relevante

jsx

```jsx
// Estructura jerárquica con transformaciones en cascada
<group 
  ref={groupRef} 
  position={[positionX, positionY, 0]}
  scale={scale}
>
  {/* Objeto del padre */}
  <mesh>
    <torusGeometry args={[2, 0.5, 16, 32]} />
    <meshStandardMaterial color="orange" />
  </mesh>
  
  {/* Hijos - posicionados relativos al padre */}
  <Hijo 
    position={[0, 0, 3]} 
    rotation={[0, Math.PI / 4, 0]} 
    color="green" 
  />
  
  // Y dentro del componente Hijo:
  <Nieto position={[0, 1.5, 0]} color="pink" />
```

## 🧪 Implementación (React + Three.js) 🌐✨

### 🔹 Etapas realizadas

1. **🔧 Preparación de escena y modelo**
   - Importación de librerías necesarias (`react-three-fiber`, `drei`, `three`)
   - Carga del modelo 3D en formato `.obj` usando `OBJLoader`
   - Asignación de materiales estándar al modelo (`MeshStandardMaterial`)
   - Configuración de la cámara y luces en la escena (`ambientLight`, `directionalLight`)

2. **🔄 Aplicación de modos de visualización**
   - Manejo del estado del modo de visualización usando `useState`
   - Implementación de cuatro modos visuales:
     - `faces`: material normal
     - `wireframe`: visualización tipo alambre
     - `edges`: resaltado de aristas con `EdgesGeometry`
     - `points`: visualización por vértices con `PointsMaterial`
   - Lógica para cambiar entre los modos con un botón flotante

3. **🧭 Visualización e interacción**
   - Renderizado interactivo del modelo 3D
   - Controles de cámara con `OrbitControls` (rotar, hacer zoom, desplazar)
   - Visualización diferenciada de geometría (según modo activo)
   - Escalado y centrado del modelo para mejor visibilidad

4. **💾 Resultados y salida**
   - Vista en tiempo real del modelo con distintos efectos visuales
   - Interfaz intuitiva para cambiar de vista con un clic
   - Escenario 3D embebido directamente en una app React moderna

---

### 🔹 Código relevante

Este fragmento muestra cómo aplicar y alternar los distintos modos de visualización sobre el modelo 3D `.obj`:

```jsx
// useState para manejar los modos
const [mode, setMode] = useState('faces');
const modes = ['faces', 'wireframe', 'edges', 'points'];

// Dentro del componente Model
obj.traverse((child) => {
  if (child.isMesh) {
    // Material base (wireframe si aplica)
    child.material = new THREE.MeshStandardMaterial({
      color: 'pink',
      roughness: 0.7,
      wireframe: mode === 'wireframe'
    });

    // Modo "points" - vértices azules
    if (mode === 'points') {
      const pointsMaterial = new THREE.PointsMaterial({
        color: 'blue',
        size: 0.05,
      });
      const points = new THREE.Points(child.geometry, pointsMaterial);
      child.add(points);
    }

    // Modo "edges" - aristas negras
    if (mode === 'edges') {
      const edges = new THREE.EdgesGeometry(child.geometry);
      const line = new THREE.LineSegments(
        edges,
        new THREE.LineBasicMaterial({ color: 'black' })
      );
      child.add(line);
    }
  }
});
```

----------

## [](#-resultados-visuales)📊 Resultados Visuales


----------

## [](#-prompts-usados)🧩 Prompts Usados


Modelo Generativo Claude 3.7 Sonnet :
```
crea una escena 3d interactiva con react three fiber y vite, que tenga un sistema jerárquico de transformación tipo padre-hijo-nieto. usa <group> y <mesh> para armar la jerarquía. el padre debe poder rotar y moverse con controles en tiempo real tipo leva o dat.gui, y que esos cambios se vean reflejados también en los hijos y nietos. incluye un tercer nivel (el nieto) para ver cómo se encadenan las transformaciones. genera los archivos App.jsx, main.jsx, App.css y index.css.
```

Modelo Generativo: GPT-4o
```
genera un documento en markdown que describa un proyecto donde se implementa un sistema jerárquico 3D usando React Three Fiber y Vite. el documento debe tener:
una descripción del objetivo del taller
explicación de los conceptos aprendidos como transformaciones en cascada, jerarquías de objetos, uso de leva
descripción de la estructura del proyecto y los archivos: App.jsx, main.jsx, App.css, index.css y README.md
detalles técnicos de cómo funcionan las transformaciones entre padre, hijo y nieto usando <group> y <mesh>
explicación de los controles con leva, qué se puede modificar y cómo afecta la escena
pasos de implementación: jerarquía, geometrías, animaciones, ayudas visuales
un bloque de código relevante mostrando la jerarquía
una reflexión final sobre lo aprendido y qué se podría mejorar
instrucciones para ejecutar el proyecto, instalar dependencias y correr el servidor
```
----------

## [](#-reflexi%C3%B3n-final)💬 Reflexión Final

El desarrollo de este taller me permitió comprender de manera práctica cómo funcionan las transformaciones en cascada en un entorno 3D. La manera en que React Three Fiber facilita la creación de estructuras jerárquicas mediante componentes anidados resulta particularmente poderosa, ya que permite organizar escenas complejas de forma lógica y mantenible.

La parte más interesante fue implementar los controles interactivos y observar cómo los cambios en el objeto padre se propagan instantáneamente a través de toda la jerarquía. Esto demuestra claramente el principio fundamental de las matrices de transformación en gráficos 3D, donde cada objeto hijo hereda y combina las transformaciones de su padre con las propias.

En futuros proyectos, me gustaría expandir este concepto para crear sistemas más complejos, como un modelo de personaje articulado o un mecanismo con piezas móviles interconectadas. También sería interesante implementar la capacidad de guardar y cargar diferentes configuraciones de transformación para crear animaciones predefinidas o secuencias de movimiento.