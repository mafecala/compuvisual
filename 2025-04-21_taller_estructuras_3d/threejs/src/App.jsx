import React, { Suspense } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import { useLoader } from '@react-three/fiber';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader';
import * as THREE from 'three';

const Model = () => {
  const obj = useLoader(OBJLoader, '/magnolia.obj');
  
  //asignar material
  React.useEffect(() => {
    obj.traverse((child) => {
      if (child.isMesh) {
        child.material = new THREE.MeshStandardMaterial({ 
          color: 'pink',
          roughness: 0.7
        });
      }
    });
  }, [obj]);

  return <primitive object={obj} scale={0.5} />;
};

const App = () => {
    return (
      // Contenedor principal que ocupa toda la pantalla
      <div style={{ 
        height: '100vh', // 100% del alto de la ventana
        width: '100vw'   // 100% del ancho de la ventana
      }}>

      <Canvas
       // position: [x, y, z] coordenadas de posición
        // fov: campo de visión en grados (50°)
        camera={{ position: [10, 10, 10], fov: 50 }}
      >
        {/* luces */}
        <ambientLight intensity={0.5} />
        <directionalLight position={[10, 10, 5]} intensity={1} />
        
        <OrbitControls 
          enablePan={true}    // Permite desplazar
          enableZoom={true}   // Permite zoom
          enableRotate={true} // Permite rotar
        />

        
        <Suspense fallback={null}>
          <Model />
        </Suspense>
      </Canvas>
    </div>
  );
};

export default App;