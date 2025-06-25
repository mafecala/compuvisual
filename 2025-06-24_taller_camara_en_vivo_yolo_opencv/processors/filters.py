import cv2
import numpy as np

class ImageFilters:
    @staticmethod
    def grayscale(frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    @staticmethod
    def binary(frame, threshold=127):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        return binary
    
    @staticmethod
    def canny_edges(frame, threshold1=100, threshold2=200):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, threshold1, threshold2)