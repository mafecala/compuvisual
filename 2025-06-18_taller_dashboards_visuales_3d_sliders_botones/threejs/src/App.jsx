// App.jsx
import React, { useRef, useState } from 'react'
import { Canvas, useFrame } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { useControls } from 'leva'
import * as THREE from 'three'

function Box() {
  const meshRef = useRef()
  const [autoRotate, setAutoRotate] = useState(false)
  const [materialType, setMaterialType] = useState('Standard')

  const { scale, color, rotate, material } = useControls({
    scale: { value: 1, min: 0.1, max: 3, step: 0.1 },
    color: '#ff0000',
    rotate: {
      label: 'Auto Rotate',
      value: false,
      onChange: (value) => setAutoRotate(value),
    },
    material: {
      options: ['Standard', 'Phong'],
      onChange: (val) => setMaterialType(val),
    }
  })

  // Luz control
  const { lightColor, intensity, position } = useControls('Light', {
    lightColor: '#ffffff',
    intensity: { value: 1, min: 0, max: 5, step: 0.1 },
    position: { value: { x: 5, y: 5, z: 5 }, step: 0.5 }
  })

  useFrame(() => {
    if (autoRotate && meshRef.current) {
      meshRef.current.rotation.y += 0.01
    }
  })

  const materialProps = { color }

  const MaterialComponent =
    materialType === 'Phong' ? <meshPhongMaterial {...materialProps} /> : <meshStandardMaterial {...materialProps} />

  return (
    <>
      <pointLight
        position={[position.x, position.y, position.z]}
        intensity={intensity}
        color={lightColor}
      />
      <mesh ref={meshRef} scale={scale}>
        <boxGeometry args={[1, 1, 1]} />
        {MaterialComponent}
      </mesh>
    </>
  )
}

export default function App() {
  return (
    <Canvas camera={{ position: [3, 3, 3] }}>
      <ambientLight />
      <Box />
      <OrbitControls />
    </Canvas>
  )
}
