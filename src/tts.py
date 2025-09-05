import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from  model.voice import Voice

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
def CreateSound(voiceid, text): 
    audiofile = client.text_to_speech.convert(
        voice_id=voiceid,
        output_format="mp3_44100_128",
        text=text,
        language_code="en",
        model_id="eleven_multilingual_v2",
    )
    return audiofile

def searchVoice(): 
    try: 
        voices = client.voices.search(include_total_count=True,)
    except Exception as e:
        print(f"Error occurred while searching for voices: {e}")
        return None
    for voice in voices.voices:
        voice_obj = Voice(
            id=voice.voice_id,
            name=voice.name,
            preview_url=voice.preview_url
        )
        print(voice_obj)

if __name__ == "__main__":
    searchVoice()