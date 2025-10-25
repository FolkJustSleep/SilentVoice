import cv2
import pickle
import mediapipe as mp
import numpy as np
if __name__ == "__main__":
    from service.camera import find_available_cameras
else: 
    from src.service.camera import find_available_cameras   

def classify_model():
    # Initialize MediaPipe Hands.
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(
        static_image_mode=True,
        min_detection_confidence=0.5)
    model_dict = pickle.load(open("./model_100pic.p", "rb"))
    model = model_dict['model']

    available_cameras = find_available_cameras()
    if not available_cameras:
        print("Error: No cameras found!")
        exit()
    camera_index = available_cameras[0]  # Use first available camera
    print(f"Available cameras: {available_cameras}")
    print(f"Using camera index: {camera_index}")
    webcam = cv2.VideoCapture(camera_index)
    data_labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
    try:
        while True:
            data_aux = []

            ret, frame = webcam.read()

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)
        #draw hand landmarks on the frame
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style()
                        )
                for hand_landmarks in results.multi_hand_landmarks:
                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y
                            data_aux.append(x)
                            data_aux.append(y)

                predicted_class = model.predict([np.asanyarray(data_aux)])

                predicted_char = data_labels_dict[int(predicted_class[0])]
                print(predicted_char)
                    
            cv2.imshow("Webcam", frame)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"Error: {e}")
        webcam.release()
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
        print("Interrupted by user")
        webcam.release()
        cv2.destroyAllWindows()
    finally:
        webcam.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    classify_model()