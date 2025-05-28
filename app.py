import cv2
import mediapipe as mp
import numpy as np
import os

class PoseDetector:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Load overlay images if they exist
        self.specs = None
        self.smoke = None
        self.actor = None
        
        if os.path.exists('images/spects.png'):
            self.specs = cv2.imread('images/spects.png', cv2.IMREAD_UNCHANGED)
            self.specs = cv2.resize(self.specs, (80, 80))
        
        if os.path.exists('images/cigar.png'):
            self.smoke = cv2.imread('images/cigar.png', cv2.IMREAD_UNCHANGED)
            self.smoke = cv2.resize(self.smoke, (40, 40))
        
        if os.path.exists('images/shahrukh.png'):
            self.actor = cv2.imread('images/shahrukh.png', cv2.IMREAD_UNCHANGED)
        
    def overlay_image(self, background, overlay, x, y):
        """Overlay an image with transparency on the background"""
        if overlay is None:
            return background
            
        h, w = overlay.shape[:2]
        if x < 0 or y < 0 or x + w > background.shape[1] or y + h > background.shape[0]:
            return background
            
        # Extract the alpha channel
        alpha = overlay[:, :, 3] / 255.0
        alpha = np.expand_dims(alpha, axis=-1)
        
        # Convert overlay to BGR
        overlay_rgb = overlay[:, :, :3]
        
        # Blend the images
        background[y:y+h, x:x+w] = (1 - alpha) * background[y:y+h, x:x+w] + alpha * overlay_rgb
        
        return background

    def process_frame(self, frame):
        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)
        
        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame and detect poses
        results = self.pose.process(rgb_frame)
        
        if results.pose_landmarks:
            # Draw the pose landmarks
            self.mp_draw.draw_landmarks(
                frame,
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )
            
            # Get nose position
            nose = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.NOSE]
            h, w, _ = frame.shape
            nose_x, nose_y = int(nose.x * w), int(nose.y * h)
            
            # Add specs if available
            if self.specs is not None:
                specs_x = nose_x - 35
                specs_y = nose_y - 50
                frame = self.overlay_image(frame, self.specs, specs_x, specs_y)
            
            # Add smoke if available
            if self.smoke is not None:
                smoke_x = nose_x - 35
                smoke_y = nose_y + 10
                frame = self.overlay_image(frame, self.smoke, smoke_x, smoke_y)
        
        return frame

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    # Initialize pose detector
    detector = PoseDetector()
    
    print("Press 'q' to quit")
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
            
        # Process frame
        processed_frame = detector.process_frame(frame)
        
        # Display the frame
        cv2.imshow('Pose Detection', processed_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 