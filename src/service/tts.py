import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from src.service.voice_upload import UploadVoice

from database import crud, supabase

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
def CreateSound(voiceid, text, filename): 
    fileName = filename+".mp3"
    audiofile = client.text_to_speech.convert(
        voice_id=voiceid,
        output_format="mp3_44100_128",
        text=text,
        language_code="en",
        model_id="eleven_multilingual_v2",
    )
    response = UploadVoice(audiofile, filename)
    return response
    

    