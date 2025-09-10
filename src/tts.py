import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from  model.voice import Voice
from database import crud, supabase
db = supabase.CreateConnection()
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
    
    with open("myfile.mp3", "wb") as f:
        for chunk in audiofile:
            f.write(chunk)# ใช้ 'wb' เพราะเป็น binary

    print("บันทึกไฟล์เรียบร้อยแล้ว")

def SearchVoice(): 
    try: 
        voices = client.voices.search(include_total_count=True,)
    except Exception as e:
        print(f"Error occurred while searching for voices: {e}")
        return None
    # voicesValue: list[Voice] = []  
    for voice in voices.voices:
        print(voice)
        print(f"Voice ID: {voice.voice_id}, Name: {voice.name}, Preview URL: {voice.preview_url}\n")
        # voice_obj = {
        #     "id": voice.voice_id,
        #     "name": voice.name,
        #     "preview_url": voice.preview_url
        # }
        # response, msg = crud.Create(db, "voicelist", voice_obj)
        # print(response)
        # print(msg)

if __name__ == "__main__":
    SearchVoice()