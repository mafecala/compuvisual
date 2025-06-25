import { useState, useEffect } from 'react'

export function useWebSocket(url) {
  const [data, setData] = useState(null)

  useEffect(() => {
    const socket = new WebSocket(url)

    socket.onmessage = (event) => {
      setData(JSON.parse(event.data))
    }

    socket.onerror = (error) => {
      console.error('WebSocket error:', error)
    }

    return () => {
      socket.close()
    }
  }, [url])

  return { data }
}