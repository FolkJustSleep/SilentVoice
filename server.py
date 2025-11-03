from fastapi import FastAPI

from src.service.tts import CreateSound
from model.voice import InputVoice
from model.input_image import InputImage
from src.service.classify_model import predict_class
from model.respons import ResponseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["POST"],  # Allows all methods
    allow_headers=["content-type: application/json"],  # Allows all headers
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI server!"}

@app.post("/tts")
async def read_tts(input_voice: InputVoice):
    result = await CreateSound(input_voice.voiceid, input_voice.text, input_voice.filename)
    if result["error"]:
        return ResponseModel(status="400", message="Error creating TTS", data=result["error"])
    return ResponseModel(status="200", message="TTS created successfully", data=result)

@app.post("/predict")
async def read_predict(input_image: InputImage):
    image = input_image.image
    result= predict_class(image)
    if result["error"]:
        return ResponseModel(status="400", message="Error in prediction", result=result["error"])
    return ResponseModel(status="200", message="Prediction successful", result=result["result"])