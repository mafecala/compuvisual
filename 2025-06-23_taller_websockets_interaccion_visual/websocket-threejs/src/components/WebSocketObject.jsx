import { useEffect, useRef } from 'react'
import { useFrame } from '@react-three/fiber'
import { useWebSocket } from '../hooks/useWebSocket'

export default function WebSocketObject() {
  const meshRef = useRef()
  const { data } = useWebSocket('ws://localhost:8765')

  useFrame(() => {
    if (meshRef.current && data) {
      meshRef.current.position.x = data.x
      meshRef.current.position.y = data.y
      meshRef.current.material.color.set(data.color)
      // Add rotation for more dynamic effect
      meshRef.current.rotation.x += 0.01
      meshRef.current.rotation.y += 0.01
    }
  })

  return (
    <mesh ref={meshRef}>
      {/* Adjust sphere parameters: radius, width segments, height segments */}
      <sphereGeometry args={[1.5, 64, 64]} />
      <meshPhysicalMaterial 
        metalness={0.5}
        roughness={0.1}
        clearcoat={1.0}
      />
    </mesh>
  )
}