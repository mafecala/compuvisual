import React, { useRef } from 'react'
import { Canvas, useFrame, extend } from '@react-three/fiber'
import { shaderMaterial } from '@react-three/drei'
import * as THREE from 'three'

// Shaders como strings normalesbb
const vertexShader = `
  varying vec3 vPosition;
  varying vec3 vNormal;

  void main() {
    vPosition = position;
    vNormal = normal;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`

const fragmentShader = `
  precision mediump float;

  uniform float uTime;
  varying vec3 vPosition;
  varying vec3 vNormal;

  void main() {
    vec3 light = normalize(vec3(0.5, 1.0, 0.3));
    float lightIntensity = dot(normalize(vNormal), light);

    float quant = step(0.5, lightIntensity);
    vec3 toonColor = mix(vec3(0.1, 0.2, 0.8), vec3(1.0, 0.8, 0.3), quant);

    float gradient = smoothstep(-1.0, 1.0, vPosition.y);
    vec3 baseColor = mix(vec3(0.0), toonColor, gradient);

    float pulse = sin(uTime * 2.0) * 0.5 + 0.5;
    vec3 finalColor = baseColor * pulse;

    gl_FragColor = vec4(finalColor, 1.0);
  }
`

// Crear el shader material
const CustomMaterial = shaderMaterial(
  { uTime: 0 },
  vertexShader,
  fragmentShader
)

extend({ CustomMaterial })

// Componente con animación
const AnimatedSphere = () => {
  const ref = useRef()
  useFrame(({ clock }) => {
    ref.current.uTime = clock.getElapsedTime()
  })

  return (
    <mesh>
      <sphereGeometry args={[1, 64, 64]} />
      <customMaterial ref={ref} />
    </mesh>
  )
}

export default function App() {
  return (
    <Canvas camera={{ position: [0, 0, 4], fov: 50 }}>
      <ambientLight />
      <directionalLight position={[2, 2, 2]} />
      <AnimatedSphere />
    </Canvas>
  )
}
