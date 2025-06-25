import cv2
import numpy as np
from processors.filters import ImageFilters
from processors.yolo_detector import YOLODetector

class VideoProcessor:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.yolo = YOLODetector()
        self.filters = ImageFilters()
        self.current_filter = 'original'
        self.paused = False
        self.recording = False
        self.out = None
    
    def process_frame(self, frame):
        if self.current_filter == 'original':
            return self.yolo.detect(frame)
        elif self.current_filter == 'gray':
            return self.filters.grayscale(frame)
        elif self.current_filter == 'binary':
            return self.filters.binary(frame)
        elif self.current_filter == 'canny':
            return self.filters.canny_edges(frame)
    
    def run(self):
        while True:
            if not self.paused:
                ret, frame = self.cap.read()
                if not ret:
                    break
                
                # Process frame
                processed = self.process_frame(frame)
                
                # Show results
                cv2.imshow('Video', processed)
                
                # Record if active
                if self.recording and self.out:
                    self.out.write(processed)
            
            # Handle keyboard input
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('p'):
                self.paused = not self.paused
            elif key == ord('s'):
                cv2.imwrite('captura.jpg', processed)
            elif key == ord('r'):
                if not self.recording:
                    fourcc = cv2.VideoWriter_fourcc(*'XVID')
                    self.out = cv2.VideoWriter('output.avi', fourcc, 20.0, 
                                             (frame.shape[1], frame.shape[0]))
                    self.recording = True
                else:
                    self.recording = False
                    self.out.release()
                    self.out = None
            elif key == ord('1'):
                self.current_filter = 'original'
            elif key == ord('2'):
                self.current_filter = 'gray'
            elif key == ord('3'):
                self.current_filter = 'binary'
            elif key == ord('4'):
                self.current_filter = 'canny'
        
        self.cap.release()
        if self.out:
            self.out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    processor = VideoProcessor()
    processor.run()