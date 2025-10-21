import os
# to save the dataset that we created from data processing

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

# Initialize MediaPipe Hands.
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=True,
    min_detection_confidence=0.5)

# Directory containing the images
DATA_DIR = './data'

# data that will be used for training
data = []
# category for each image
labels = []


# Process each image in the data directory
for dir_name in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_name))[:1]:
        data_aux = []
        img = cv2.imread(os.path.join(DATA_DIR, dir_name, img_path))
        # Convert the BGR image to RGB before processing.
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks.
                mp_drawing.draw_landmarks(
                    img_rgb,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
        # Show the image with the hand landmarks
        plt.figure() 
        plt.imshow(img_rgb)  
        
plt.show()
