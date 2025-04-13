# Actividad en Python

  ![Animación de un triángulo rotando, trasladándose y creciendo en tamaño](../python/animation.gif)

## Descripción
Proyecto en **Jupyter Notebook** que aplica transformaciones geométricas a un triángulo:
- **Traslación**
- **Rotación**  
- **Escala**

Usando multiplicación de matrices con `numpy` y visualización con `matplotlib`.

##  Características
- Usa matrices de transformación
- Hace una animación y genera un GIF
- Control de parámetros

## Cómo ejecutar

1.  Instalar requisitos:

`pip install numpy matplotlib pillow`    
    
2.  Ejecuta el Jupyter Notebook:

` jupyter notebook transformaciones.ipynb`

## Personalización

Se pueden modificar estos parámetros en el notebook:

    tx, ty = 3, 2          # traslación
    angulo = 60             # rotación en grados
    escala_inicial = 0.5    # escala
    escala_final = 1.5      

# Three.js con React Three Fiber

  ![Animación de un cubo rotando, trasladándose y cambiando de tamaño](../threejs/threejs-demostracion.gif)

## Descripción
Proyecto con **Vite** y **React Three Fiber**. Un cubo rota sobre su propio eje, sigue una trayectoria senoidal y escala con una función temporal. 

Adicionalmente, la escena puede navergarse con controles. (Desplazamiento, zoom y rotación)

##  Características
Este proyecto se inició con el **template básico de Vite + React**, que incluye:
- Hot Module Replacement (HMR)
- Configuración inicial de ESLint
- Estructura estándar de Vite
- Generado con:
` npm create vite@latest proyecto --template react `

**Los controles son los siguientes:**

*Click izquierdo:* Rotar la cámara
*Click derecho:* Trasladar la cámara
*Rueda del mouse:* Zoom

## Cómo ejecutar

1.  Instalar requisitos:

`npm install three @react-three/fiber @react-three/drei`    

2.  Iniciar el servidor de desarrollo:

`  npm run dev ` 

NOTA: Verifica que estés en la carpeta correcta (cubo 3d)
    
3.  Abrir en el navegador:
  
 http://localhost:5173

## Personalización

En **Box.jsx**:

Se pueden modificar estos parámetros en el notebook para cambiar el movimiento del círculo:

    useFrame((state)  =>  {
    
    const  time = state.clock.elapsedTime
    
    boxRef.current.rotation.y  +=  0.01  //rota sobre su propio eje
    
    boxRef.current.position.x = Math.sin(time) *  2  //se traslada en trayectoria senoidal
    
    const  scale = Math.sin(time) *  0.3  +  1  //cambia su escala en función .del tiempo
    
    boxRef.current.scale.set(scale, scale, scale)
    
    })    
Se pueden modificar estos parámetros en el notebook para cambiar la apariencia del círculo:

    return (
    
    <mesh  ref={boxRef}>
    
    <boxGeometry  args={[1, 1, 1]}  />
    
    <meshStandardMaterial  color="hotpink"/>
    
    </mesh>
    
    )

