import pickle
import cv2, base64, numpy as np, pickle, mediapipe as mp

def load_model():
    model_dict = pickle.load(open("./model300pic.p", "rb"))
    model = model_dict["model"]
    return model

def get_labels():
    return {i: chr(65 + i) for i in range(26)}  # A–Z



def predict_class(image_data):
    model = load_model()
    labels = get_labels()
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.5)
    try:
        img_data = base64.b64decode(image_data)
        np_arr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        data_aux = []
        if results.multi_hand_landmarks:
            for lm in results.multi_hand_landmarks[0].landmark:
                data_aux.extend([lm.x, lm.y])
            if data_aux:
                predicted_class = model.predict([np.asarray(data_aux)])
                predicted_char = labels[int(predicted_class[0])]
                return {"result": predicted_char, "error": None}
        return {"result": None , "error": "No hand detected"}
    except Exception as e:
        print(f"Error in prediction: {e}")
        return {"result": None, "error": str(e)}