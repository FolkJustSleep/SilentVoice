from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2, base64, numpy as np, pickle, mediapipe as mp

app = Flask(__name__)
CORS(app)  # ✅ อนุญาตให้ frontend (Streamlit/HTML) เรียก API ได้

# โหลดโมเดล
model_dict = pickle.load(open("./model.p", "rb"))
model = model_dict["model"]
labels = {i: chr(65 + i) for i in range(26)}  # A–Z

# ตั้งค่า Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.5)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        img_data = base64.b64decode(data["image"])
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
                return jsonify({"result": predicted_char})

        return jsonify({"result": None})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# ✅ ส่วนนี้แหละที่คุณถามถึง
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
