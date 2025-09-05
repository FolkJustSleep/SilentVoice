import database.crud as crud
from datetime import datetime
import repository.Result_repo as result_repo

def InsertResult(db, text, audio_name):
    data = {
        "text": text,
        "audio_name": audio_name,
        "updated_at": datetime.now().isoformat(),
    }
    response, message =  result_repo.InsertResult(db, data)
    return response, message

def GetResultByID(db, id):
    response, message = result_repo.GetResultByID(db, id)
    return response, message


def GetAllResults(db):
    response, message = result_repo.GetAllResults(db)
    return response, message

def UpdateResult(db, id, new_text, new_audio_name):
    data = {
        "text": new_text,
        "audio_name": new_audio_name,
        "updated_at": datetime.now().isoformat(),
    }
    response, message = result_repo.UpdateResult(db, id, data)
    return response, message

def DeleteResult(db, id):
    response, message = result_repo.DeleteResult(db, id)
    return response, message