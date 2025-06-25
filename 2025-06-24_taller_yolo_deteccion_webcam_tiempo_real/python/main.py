from ultralytics import YOLO
import cv2
import time
import numpy as np

class ObjectDetector:
    def __init__(self, model_path='yolov8n.pt', conf_threshold=0.5):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.fps_history = []
        
    def draw_stats(self, frame, fps, inference_time):
        # Draw FPS and inference time
        cv2.putText(frame, f'FPS: {fps:.1f}', (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f'Inference: {inference_time*1000:.1f}ms', 
                   (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Draw average FPS
        if self.fps_history:
            avg_fps = sum(self.fps_history) / len(self.fps_history)
            cv2.putText(frame, f'Avg FPS: {avg_fps:.1f}', (10, 110),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    def process_frame(self, frame):
        # Start timing
        start_time = time.time()
        
        # Run inference
        results = self.model(frame, stream=True)
        
        # Calculate inference time
        inference_time = time.time() - start_time
        
        # Process results
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Get box coordinates
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Get class name and confidence
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                name = self.model.names[cls]
                
                if conf > self.conf_threshold:
                    # Draw box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    
                    # Draw label
                    label = f'{name} {conf:.2f}'
                    cv2.putText(frame, label, (x1, y1-10),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Calculate FPS
        fps = 1.0 / inference_time
        self.fps_history.append(fps)
        if len(self.fps_history) > 30:  # Keep last 30 frames
            self.fps_history.pop(0)
            
        # Draw performance stats
        self.draw_stats(frame, fps, inference_time)
        
        return frame

    def run(self):
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            # Process frame
            processed_frame = self.process_frame(frame)
            
            # Show result
            cv2.imshow('YOLO Detection', processed_frame)
            
            # Break if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = ObjectDetector()
    detector.run()