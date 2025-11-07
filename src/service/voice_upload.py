from database import supabase
from io import BytesIO

BUCKET = "voice-record"      
db = supabase.CreateConnection()

async def UploadVoice(byte_data: bytes, filename: str) :
    buffer = BytesIO()
    for chunk in byte_data:
        buffer.write(chunk)
    data = buffer.getvalue()
    try:
        response = db.storage.from_(BUCKET).upload(
                    path="voices/"+filename,
                    file=data,
                    file_options={
                        "cache-control": "3600",
                        "upsert": "false" 
                    }
                )
        print(f" Uploaded Success")
        return {"response": response, "error": None}
    except Exception as e:
        print(f" Upload Failed: {e}")
        response = {"error": str(e)}
        return {"response": response, "error": str(e)}
