import React, { useRef, useState, useEffect } from 'react';
import { Canvas, useFrame, useThree } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import * as THREE from 'three';
import './App.css';

const Boxes = () => {
  const colors = ['red', 'green', 'blue', 'orange', 'purple'];
  const elements = [];

  for (let x = -10; x <= 10; x += 5) {
    for (let z = -10; z <= 10; z += 5) {
      const height = Math.random() * 2 + 1;
      elements.push(
        <mesh key={`${x}-${z}`} position={[x, height / 2, z]}>
          <boxGeometry args={[1, height, 1]} />
          <meshStandardMaterial color={colors[Math.floor(Math.random() * colors.length)]} />
        </mesh>
      );
    }
  }

  return <>{elements}</>;
};

const CameraFrustumHelper = ({ camera }) => {
  const helperRef = useRef();

  useEffect(() => {
    if (camera && camera.isCamera) {
      helperRef.current = new THREE.CameraHelper(camera);
      camera.parent?.add(helperRef.current);
    }

    return () => {
      if (helperRef.current) {
        camera.parent?.remove(helperRef.current);
      }
    };
  }, [camera]);

  return null;
};

const Scene = ({ cameraType }) => {
  const perspectiveRef = useRef();
  const orthoRef = useRef();
  const pointRef = useRef();
  const { size, set } = useThree();

  const activeCamera = cameraType === 'perspective' ? perspectiveRef : orthoRef;

  useEffect(() => {
    if (activeCamera.current) {
      set({ camera: activeCamera.current });
    }
  }, [cameraType, set]);

  return (
    <>
      {/* Cámaras */}
      <perspectiveCamera
        ref={perspectiveRef}
        fov={75}
        aspect={size.width / size.height}
        near={0.1}
        far={100}
        position={[10, 10, 10]}
      />
      <orthographicCamera
        ref={orthoRef}
        left={-size.width / 100}
        right={size.width / 100}
        top={size.height / 100}
        bottom={-size.height / 100}
        near={0.1}
        far={100}
        position={[10, 10, 10]}
      />

      <OrbitControls />

      {/* Luces */}
      <ambientLight intensity={0.4} />
      <directionalLight position={[10, 10, 10]} intensity={1} />

      {/* Helpers */}
      <gridHelper args={[20, 20]} />
      <axesHelper args={[5]} />
      <CameraFrustumHelper camera={activeCamera.current} />

      {/* Objetos */}
      <Boxes />

      {/* Punto rojo en escena */}
      <mesh ref={pointRef} position={[0, 2, 0]}>
        <sphereGeometry args={[0.2, 16, 16]} />
        <meshStandardMaterial color="red" />
      </mesh>
    </>
  );
};

export default function App() {
  const [cameraType, setCameraType] = useState('perspective');

  return (
    <div className="App">
      <div className="controls">
        <button
          className={cameraType === 'perspective' ? 'active' : ''}
          onClick={() => setCameraType('perspective')}
        >
          Perspective Camera
        </button>
        <button
          className={cameraType === 'orthographic' ? 'active' : ''}
          onClick={() => setCameraType('orthographic')}
        >
          Orthographic Camera
        </button>
      </div>
      <Canvas>
        <Scene cameraType={cameraType} />
      </Canvas>
    </div>
  );
}
