import cv2
from typing import Any
import face_recognition
class FaceDetected :
    
    def __init__(self) -> None:
        # Initialize variables
        face_locations = []
        pass
    
    
    def detectedAttributes(self,video_capture:Any):
        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = frame[:, :, ::-1]

            # Find all the faces in the current frame of video
            self.face_locations = face_recognition.face_locations(rgb_frame)

            # Display the results
            for top, right, bottom, left in self.face_locations:
                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
