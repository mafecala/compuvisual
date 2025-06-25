import { useEffect, useState, useRef } from 'react'
import { useFrame } from '@react-three/fiber'

export function HandVisualizer() {
    const [handData, setHandData] = useState([])
    const points = useRef([])

    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8765')
        
        ws.onopen = () => {
            console.log('Connected to WebSocket server')
        }

        ws.onmessage = (event) => {
            const data = JSON.parse(event.data)
            if (data.hands && data.hands.length > 0) {
                setHandData(data.hands[0])
            }
        }

        ws.onerror = (error) => {
            console.error('WebSocket error:', error)
        }

        return () => ws.close()
    }, [])

    useFrame(() => {
        // Update points positions in animation frame
        handData.forEach((point, index) => {
            if (points.current[index]) {
                points.current[index].position.set(
                    (point.x - 0.5) * 2,
                    -(point.y - 0.5) * 2,
                    point.z
                )
            }
        })
    })

    return (
        <group>
            {Array(21).fill(0).map((_, i) => (
                <mesh key={i} ref={el => points.current[i] = el}>
                    <sphereGeometry args={[0.02]} />
                    <meshStandardMaterial color="hotpink" />
                </mesh>
            ))}
            <ambientLight intensity={0.5} />
            <pointLight position={[10, 10, 10]} />
        </group>
    )
}