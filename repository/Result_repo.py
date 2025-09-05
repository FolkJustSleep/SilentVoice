from datetime import datetime
from database import crud

def InsertResult(db, data):
    response, message =  crud.Create(db, "Result", data)
    return response, message

def GetResultByID(db, id):
    response, message = crud.GetByID(db, "Result", "*", id)
    return response, message


def GetAllResults(db):
    response, message = crud.GetAll(db, "Result", "*")
    return response, message

def UpdateResult(db, id, data):
    response, message = crud.Update(db, "Result", data, id)
    return response, message

def DeleteResult(db, id):
    response, message = crud.Delete(db, "Result", id)
    return response, message