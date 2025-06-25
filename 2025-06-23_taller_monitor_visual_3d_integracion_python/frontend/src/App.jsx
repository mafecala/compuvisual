import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { HandVisualizer } from './components/HandVisualizer'

function App() {
    return (
        <div style={{ width: '100vw', height: '100vh', background: '#000' }}>
            <Canvas
                camera={{ position: [0, 0, 2] }}
                style={{ background: '#111' }}
            >
                <HandVisualizer />
                <OrbitControls />
            </Canvas>
        </div>
    )
}

export default App