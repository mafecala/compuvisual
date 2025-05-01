import React, { Suspense, useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import { useLoader } from '@react-three/fiber';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader';
import * as THREE from 'three';

const Model = ({ mode }) => {
  const obj = useLoader(OBJLoader, '/magnolia.obj');

  React.useEffect(() => {
    obj.traverse((child) => {
      if (child.isMesh) {
        // Limpiar hijos previos
        child.clear();

        // Material base
        const baseMaterial = new THREE.MeshStandardMaterial({
          color: 'pink',
          roughness: 0.7,
          wireframe: mode === 'wireframe'
        });

        child.material = baseMaterial;

        // Modo puntos (vértices)
        if (mode === 'points') {
          const pointsMaterial = new THREE.PointsMaterial({
            color: 'blue',
            size: 0.05,
          });
          const points = new THREE.Points(child.geometry, pointsMaterial);
          child.add(points);
        }

        // Modo edges (aristas)
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
  }, [obj, mode]);

  return <primitive object={obj} scale={0.5} />;
};

export { Model };

const App = () => {

  // Estado que guarda el modo actual de visualización (caras, wireframe, edges o points)
  const [mode, setMode] = useState('faces'); // 🎨 Modo por defecto: caras sólidas

  // Lista de modos disponibles para recorrer cíclicamente
  const modes = ['faces', 'wireframe', 'edges', 'points'];

  // Función que pasa al siguiente modo de la lista cuando se hace clic en el botón
  const nextMode = () => {
    const currentIndex = modes.indexOf(mode);        // Busca el índice del modo actual
    const nextIndex = (currentIndex + 1) % modes.length; // Calcula el siguiente índice de forma cíclica
    setMode(modes[nextIndex]); // Cambia el modo actual
  };

  return (
    // Contenedor de pantalla completa para que el Canvas ocupe todo
    <div style={{ height: '100vh', width: '100vw' }}>
      
      {/* Botón para cambiar de vista */}
      <button
        onClick={nextMode} // Al hacer clic, cambia de modo
        style={{
          position: 'absolute', // Lo posicionamos sobre el canvas
          top: '20px',
          left: '20px',
          zIndex: 1, // Asegura que esté encima del Canvas
          padding: '10px 20px',
          fontSize: '16px',
          backgroundColor: '#ff69b4', // Rosado
          border: 'none',
          borderRadius: '10px',
          color: 'white',
          cursor: 'pointer',
          boxShadow: '0 0 10px rgba(0,0,0,0.2)' // Sombra
        }}
      >
        Cambiar vista: {mode} {/* Muestra el modo actual como texto */}
      </button>

      {/* Canvas 3D donde se renderiza la escena */}
      <Canvas camera={{ position: [10, 10, 10], fov: 50 }}>
        {/* Luz ambiental (ilumina todo suavemente) */}
        <ambientLight intensity={0.5} />

        {/* Luz direccional (como el sol) */}
        <directionalLight position={[10, 10, 5]} intensity={1} />

        {/* Controles de cámara: pan, zoom y rotación */}
        <OrbitControls enablePan enableZoom enableRotate />

        {/* Suspense permite cargar el modelo asincrónicamente */}
        <Suspense fallback={null}>
          {/* Mostramos el modelo con el modo actual */}
          <Model mode={mode} />
        </Suspense>
      </Canvas>
    </div>
  );
};

// Exportamos el componente para usarlo en main.jsx
export default App;