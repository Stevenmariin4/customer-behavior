import cv2
import face_recognition

from controllers.FaceDetected import FaceDetected

class Program:
    video_capture:any
    def __init__(self) -> None:
        self.video_capture= []
        pass
    
    
    def initProgram(self):
        # Get a reference to webcam 
        self.video_capture = cv2.VideoCapture(0)
        face = FaceDetected()
        face.detectedAttributes(self.video_capture)
        # Release handle to the webcam
        self.video_capture.release()
        cv2.destroyAllWindows()
        
        

program = Program()        
program.initProgram()