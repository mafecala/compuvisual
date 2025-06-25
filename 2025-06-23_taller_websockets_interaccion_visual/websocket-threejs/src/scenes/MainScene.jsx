import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import WebSocketObject from '../components/WebSocketObject'

export default function MainScene() {
  return (
    <Canvas camera={{ position: [0, 0, 10] }}>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
      <WebSocketObject />
      <OrbitControls />
    </Canvas>
  )
}