import React, { useRef, useState } from 'react'
import { Canvas, useFrame, extend, useThree } from '@react-three/fiber'
import { shaderMaterial } from '@react-three/drei'
import * as THREE from 'three'

// Vertex y Fragment shaders como strings
const vertexShader = `
  varying vec2 vUv;
  void main() {
    vUv = uv;
    vec3 pos = position;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
  }
`

const fragmentShader = `
  precision mediump float;
  uniform float uTime;
  uniform vec2 uMouse;
  varying vec2 vUv;

  void main() {
    // Coordenadas relativas al centro
    vec2 center = vUv - 0.5;
    float dist = length(center - uMouse);
    
    // Animación tipo energía/líquido
    float glow = sin(uTime * 3.0 + dist * 10.0) * 0.5 + 0.5;
    vec3 color = mix(vec3(0.1, 0.3, 0.9), vec3(0.8, 0.2, 1.0), glow);

    // Brillo reactivo al mouse
    float pulse = 1.0 - smoothstep(0.0, 0.3, dist);
    gl_FragColor = vec4(color + pulse * 0.3, 1.0);
  }
`

// Crear el shader material
const LiquidMaterial = shaderMaterial(
  { uTime: 0, uMouse: new THREE.Vector2(0.5, 0.5) },
  vertexShader,
  fragmentShader
)

extend({ LiquidMaterial })

// Componente para la esfera animada
function LiquidSphere() {
  const matRef = useRef()
  const { viewport, mouse } = useThree()

  useFrame(({ clock }) => {
    if (matRef.current) {
      matRef.current.uTime = clock.getElapsedTime()
      matRef.current.uMouse.set(mouse.x * 0.5 + 0.5, mouse.y * 0.5 + 0.5)
    }
  })

  return (
    <mesh>
      <sphereGeometry args={[1.2, 64, 64]} />
      <liquidMaterial ref={matRef} />
    </mesh>
  )
}

// Componente para partículas vibrantes
function ParticleSystem({ count = 200 }) {
  const meshRef = useRef()
  const colors = new Float32Array(count * 3)
  const positions = new Float32Array(count * 3)

  // Inicializa posiciones aleatorias y colores base
  for (let i = 0; i < count; i++) {
    const i3 = i * 3
    positions[i3 + 0] = (Math.random() - 0.5) * 6
    positions[i3 + 1] = (Math.random() - 0.5) * 6
    positions[i3 + 2] = (Math.random() - 0.5) * 6

    colors[i3 + 0] = 1.0
    colors[i3 + 1] = 1.0
    colors[i3 + 2] = 1.0
  }

  useFrame(({ clock }) => {
    const t = clock.getElapsedTime()
    const colorAttr = meshRef.current.geometry.attributes.color

    for (let i = 0; i < count; i++) {
      const i3 = i * 3
      const r = Math.abs(Math.sin(t + i * 0.1))
      const g = Math.abs(Math.cos(t + i * 0.2))
      const b = Math.abs(Math.sin(t + i * 0.3 + 1.0))
      colorAttr.array[i3 + 0] = r
      colorAttr.array[i3 + 1] = g
      colorAttr.array[i3 + 2] = b
    }

    colorAttr.needsUpdate = true
  })

  return (
    <points ref={meshRef}>
      <bufferGeometry>
        <bufferAttribute
          attach="attributes-position"
          count={count}
          array={positions}
          itemSize={3}
        />
        <bufferAttribute
          attach="attributes-color"
          count={count}
          array={colors}
          itemSize={3}
        />
      </bufferGeometry>
      <pointsMaterial
        size={0.19}
        vertexColors
        sizeAttenuation
        transparent
        opacity={0.85}
      />
    </points>
  )
}


// Escena principal
export default function App() {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 60 }}>
      <ambientLight />
      <directionalLight position={[2, 2, 2]} />
      <LiquidSphere />
      <ParticleSystem />
    </Canvas>
  )
}
