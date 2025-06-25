from ultralytics import YOLO
import cv2
import numpy as np

class YOLODetector:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')
        self.person_count = 0

    def detect(self, frame):
        results = self.model(frame, stream=True)
        annotated_frame = frame.copy()
        
        self.person_count = 0
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Get box coordinates
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Get class name and confidence
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                name = self.model.names[cls]
                
                if name == 'person':
                    self.person_count += 1
                
                # Draw box and label
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_frame, f'{name} {conf:.2f}', 
                          (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 
                          0.5, (0, 255, 0), 2)
        
        # Add person count to frame
        cv2.putText(annotated_frame, f'Personas: {self.person_count}', 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0, 255, 0), 2)
                   
        return annotated_frame