import os
# to save the dataset that we created from data processing
import pickle

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

print("Processing images from:", DATA_DIR)
# Process each image in the data directory
for dir_name in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_name)):
        data_aux = []
        img = cv2.imread(os.path.join(DATA_DIR, dir_name, img_path))
        # Convert the BGR image to RGB before processing.
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x)
                data_aux.append(y)
                    
            # print(data_aux)
            data.append(data_aux)
            labels.append(dir_name)

            

f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
print("Data saved to data.pickle")