import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from src.service.voice_upload import UploadVoice


load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
def CreateSound(voiceid, text, filename): 
    if not voiceid:
        return {"audiofile": None, "error": "No voice ID provided"}
    if not text:
        return {"audiofile": None, "error": "No text provided"}
    fileName = filename+".mp3"
    try: 
        if text == 'a' or text == 'A':
            text = "Ae"
        audiofile = client.text_to_speech.convert(
            voice_id=voiceid,
            output_format="mp3_44100_128",
            text=text,
            language_code="en",
            model_id="eleven_multilingual_v2",
        )
        response = UploadVoice(audiofile, fileName)
        print("Upload response:", response)
        return {"audiofile": audiofile, "error": None}
    except Exception as e:
        return {"audiofile": None, "error": str(e)}