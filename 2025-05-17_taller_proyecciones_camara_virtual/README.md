# 🧪 Taller - Proyecciones 3D: Cómo ve una Cámara Virtual

## 📅 Fecha

2025-05-17

## 🌷 Equipo de trabajo

**Mi grupo está conformado por:**

- Julián Ramírez Díaz (julramirezdi@unal.edu.co)
- Xamir Ernesto Rojas Gamboa (xerojasga@unal.edu.co)
- Julián David Rincón Orjuela (jurinconor@unal.edu.co)
- María Fernanda Cala Rodríguez (mcalar@unal.edu.co)

**Este taller fue realizado por:**
- María Fernanda Cala Rodríguez (mcalar@unal.edu.co)

## 🎯 Objetivo del Taller

Este taller tiene como objetivo comprender cómo se genera una escena tridimensional desde el punto de vista de una cámara virtual, explorando los diferentes tipos de proyecciones (perspectiva y ortográfica) y cómo afectan la representación visual. A través de React Three Fiber y Three.js, desarrollamos un visualizador interactivo que permite experimentar en tiempo real los efectos de estos sistemas de proyección, entendiendo el papel fundamental que juegan las matrices de transformación en gráficos 3D.

## 🧠 Conceptos Aprendidos

✅ Diferencias entre proyección en perspectiva y ortográfica
✅ Parámetros que definen el frustum de una cámara virtual
✅ Pipeline de transformación de coordenadas 3D a 2D
✅ Manipulación de cámaras virtuales con React Three Fiber
✅ Transformación de coordenadas de mundo a coordenadas de pantalla
✅ Visualización del frustum de la cámara y sus efectos en la representación
✅ Implementación de controles interactivos para manipular la cámara
✅ Efectos del Field of View (FOV) y otros parámetros en la imagen resultante

## 🔧 Herramientas y Entornos

- React
- Three.js
- React Three Fiber
- @react-three/drei (utilidades para Three.js en React)

## 📁 Estructura del Proyecto

```
2025-05-17_taller_proyecciones_camara_virtual/
├── threejs/
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── README.md
└── README.md
```

## 📐 Proyección en Perspectiva vs. Ortográfica

### 🔹 Proyección en Perspectiva

La proyección en perspectiva simula la forma en que percibimos el mundo real, donde los objetos parecen más pequeños a medida que se alejan del observador. Este tipo de proyección crea una sensación de profundidad y es el estándar para la mayoría de aplicaciones 3D interactivas.

**Parámetros clave:**
- **FOV (Field of View)**: Ángulo de visión, típicamente entre 60-75 grados.
- **Aspect Ratio**: Relación entre el ancho y alto del viewport (generalmente el tamaño de la ventana).
- **Near Plane**: Distancia mínima desde la cámara donde comienza la renderización.
- **Far Plane**: Distancia máxima desde la cámara donde termina la renderización.

La matriz de proyección en perspectiva transforma el frustum (forma de pirámide truncada) en un cubo unitario para la rasterización.

![demo](demo.gif)

### 🔹 Proyección Ortográfica

La proyección ortográfica no tiene en cuenta la profundidad para escalar los objetos. Los objetos mantienen su tamaño independientemente de la distancia a la cámara, creando una vista sin perspectiva que es útil para diseño técnico, diagramas y vistas arquitectónicas.

**Parámetros clave:**
- **Left/Right**: Límites horizontales del volumen de visualización.
- **Top/Bottom**: Límites verticales del volumen de visualización.
- **Near/Far**: Límites de profundidad del volumen de visualización.

La matriz de proyección ortográfica transforma un volumen rectangular en un cubo unitario para la rasterización.



## 🔹 Código Relevante

Este fragmento muestra cómo implementamos la proyección de un punto 3D al espacio de pantalla 2D:

```javascript
// Componente para la coordenada 3D seleccionada
const CoordinatePoint = ({ position, camera }) => {
  const meshRef = useRef();
  const [screenPosition, setScreenPosition] = useState({ x: 0, y: 0 });
  
  useFrame(() => {
    if (meshRef.current && camera) {
      // Clonar la posición del mundo
      const worldPos = meshRef.current.position.clone();
      
      // Proyectar punto 3D a coordenadas normalizadas de dispositivo (NDC)
      const screenPos = worldPos.clone().project(camera);
      
      // Convertir de NDC a coordenadas de pantalla en píxeles
      setScreenPosition({ 
        x: (screenPos.x * 0.5 + 0.5) * window.innerWidth, 
        y: -(screenPos.y * 0.5 - 0.5) * window.innerHeight 
      });
    }
  });
  
  return (
    <>
      {/* Esfera 3D en la posición del mundo */}
      <mesh ref={meshRef} position={position}>
        <sphereGeometry args={[0.3, 16, 16]} />
        <meshStandardMaterial color="red" />
      </mesh>
      
      {/* Línea desde el origen al punto */}
      <line>
        <bufferGeometry>
          <bufferAttribute
            attach="attributes-position"
            count={2}
            array={new Float32Array([0, 0, 0, ...position])}
            itemSize={3}
          />
        </bufferGeometry>
        <lineBasicMaterial color="red" />
      </line>
      
      {/* Marcador en posición de pantalla 2D */}
      <div
        className="screen-point"
        style={{
          position: 'absolute',
          left: `${screenPosition.x}px`,
          top: `${screenPosition.y}px`,
          pointerEvents: 'none'
        }}
      >
        <div className="marker">+</div>
        <div className="coords">
          World: ({position[0].toFixed(1)}, {position[1].toFixed(1)}, {position[2].toFixed(1)})
          <br/>
          Screen: ({screenPosition.x.toFixed(0)}, {screenPosition.y.toFixed(0)})
        </div>
      </div>
    </>
  );
};
```

## 🧩 Prompts Usados

### Prompt 1: Generación del código base con React Three Fiber

```
Crea una aplicación React usando React Three Fiber para visualizar y comparar cámaras virtuales en perspectiva y ortográficas. La aplicación debe:

1. Mostrar una escena 3D con varios objetos distribuidos a diferentes distancias
2. Permitir cambiar entre una PerspectiveCamera y una OrthographicCamera mediante botones
3. Mostrar en pantalla los parámetros actuales de la cámara (FOV, aspecto, near, far para perspectiva; left, right, top, bottom para ortográfica)
4. Implementar OrbitControls para manipular la vista de la cámara
5. Incluir un punto 3D especial que muestre sus coordenadas del mundo y su proyección en coordenadas de pantalla
6. Visualizar el frustum de la cámara actual
7. Usar una estructura modular y bien comentada
8. Incluir estilos CSS para una interfaz limpia y profesional
```

### Prompt 2: Generación del README detallado

```
Crea un README.md completo para un taller titulado "Proyecciones 3D: Cómo ve una Cámara Virtual". 
El README debe incluir:
1. Título, fecha y equipo de trabajo similar al ejemplo compartido
2. Objetivo del taller claramente definido
3. Lista de conceptos aprendidos con emojis de verificación
4. Herramientas y entornos utilizados (React, Three.js, React Three Fiber)
5. Estructura del proyecto
6. Explicación detallada de la diferencia entre proyección en perspectiva y ortográfica
7. Secciones para GIFs de demostración que muestren:
   - Vista general del visualizador
   - Comparación visual entre cámara perspectiva y ortográfica
   - Visualización del frustum de la cámara
   - Proyección de coordenadas 3D a 2D
8. Un fragmento relevante de código comentado
9. La lista de prompts utilizados para generar el código
10. Una reflexión final sobre la transformación de coordenadas 3D a 2D mediante matrices
Utiliza un formato atractivo con emojis apropiados para cada sección.
```

### Prompt 3: Optimización del sistema de proyección de coordenadas

```
Mejora el sistema de proyección de coordenadas 3D a 2D en React Three Fiber para que:
1. Muestre claramente la línea desde el origen hasta el punto 3D seleccionado
2. Visualice tanto las coordenadas del mundo 3D como las coordenadas de pantalla 2D
3. Actualice las coordenadas en tiempo real durante la manipulación de la cámara
4. Utilice un estilo visual distintivo para el punto y sus etiquetas
5. Explique brevemente en un comentario cada paso de la transformación de proyección
```

## 💬 Reflexión Final: De 3D a 2D mediante Matrices

El proceso de transformación de coordenadas 3D a coordenadas 2D de pantalla es el corazón de cualquier sistema de gráficos por computadora. Este proceso, conocido como pipeline de renderizado, se puede resumir en los siguientes pasos clave:

1. **Transformación de Modelo**: Convierte las coordenadas del objeto (modelo) al espacio del mundo mediante matrices de traslación, rotación y escala.

2. **Transformación de Vista**: Transforma las coordenadas del mundo al espacio de la cámara, donde el origen es la posición de la cámara y el eje Z negativo es la dirección de visión.

3. **Transformación de Proyección**: Aplica una matriz de proyección (perspectiva u ortográfica) para transformar el volumen de visión (frustum) en un cubo unitario normalizado.

4. **División de Perspectiva**: En proyección perspectiva, divide las coordenadas X, Y, Z por la componente W para lograr el efecto de perspectiva (objetos más lejanos parecen más pequeños).

5. **Transformación de Viewport**: Convierte las coordenadas normalizadas de dispositivo (NDC) en coordenadas de pantalla en píxeles.

Lo fascinante es que todo este proceso se puede representar matemáticamente como una serie de multiplicaciones de matrices 4×4. La potencia de este enfoque es que podemos encapsular transformaciones complejas en operaciones matriciales eficientes:

```
P_screen = P_model × M_model × M_view × M_projection × M_viewport
```

Este taller me permitió no solo visualizar este proceso abstracto, sino también experimentar interactivamente con los parámetros que afectan cada etapa. Comprender estas transformaciones es fundamental para cualquier desarrollo en gráficos 3D, realidad virtual, o videojuegos.

A través de la implementación práctica con React Three Fiber, pude observar cómo el cambio de una matriz de proyección afecta radicalmente la percepción de profundidad y escala en una escena. La proyección en perspectiva crea una experiencia visual más natural y cercana a la visión humana, mientras que la proyección ortográfica ofrece vistas precisas sin distorsión por distancia, ideal para aplicaciones técnicas.

Este conocimiento es aplicable no solo en desarrollo de videojuegos y experiencias 3D interactivas, sino también en campos como la visualización científica, el diseño CAD, la arquitectura digital y la realidad aumentada.