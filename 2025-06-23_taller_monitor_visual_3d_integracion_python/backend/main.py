import cv2
import mediapipe as mp
import numpy as np
import asyncio
import websockets
import json
from mediapipe.framework.formats import landmark_pb2
import time

class VisionProcessor:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.cap = cv2.VideoCapture(0)

    def process_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None

        # Convert to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        data = {
            'hands': [],
            'timestamp': time.time()
        }

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                hand_data = []
                for landmark in hand_landmarks.landmark:
                    hand_data.append({
                        'x': landmark.x,
                        'y': landmark.y,
                        'z': landmark.z
                    })
                data['hands'].append(hand_data)

        return data

    def cleanup(self):
        self.cap.release()
        self.hands.close()

async def websocket_server(websocket, path):  # Added path parameter back
    vision_processor = VisionProcessor()
    print(f"New client connected from {websocket.remote_address}")
    try:
        while True:
            try:
                data = vision_processor.process_frame()
                if data:
                    await websocket.send(json.dumps(data))
                await asyncio.sleep(1/30)  # 30 FPS
            except websockets.exceptions.ConnectionClosed:
                print(f"Client {websocket.remote_address} disconnected")
                break
            except Exception as e:
                print(f"Error processing frame: {e}")
                break
    finally:
        vision_processor.cleanup()
        print(f"Cleaning up resources for {websocket.remote_address}")

async def websocket_handler(websocket):  # Removed path parameter
    vision_processor = VisionProcessor()
    print(f"New client connected from {websocket.remote_address}")
    try:
        while True:
            try:
                data = vision_processor.process_frame()
                if data:
                    await websocket.send(json.dumps(data))
                await asyncio.sleep(1/30)  # 30 FPS
            except websockets.exceptions.ConnectionClosed:
                print(f"Client {websocket.remote_address} disconnected")
                break
            except Exception as e:
                print(f"Error processing frame: {e}")
                break
    finally:
        vision_processor.cleanup()
        print(f"Cleaning up resources for {websocket.remote_address}")

async def main():
    try:
        server = await websockets.serve(
            websocket_handler,  # Changed function name
            "localhost",
            8765
        )
        print("Vision server running on ws://localhost:8765")
        await asyncio.Future()  # run forever
    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    asyncio.run(main())