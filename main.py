import cv2
from database.supabase import CreateConnection
from src.service.camera import capture_images
import src.service.Result as Result
from src.service.tts import CreateSound
# from src.train_models import train_model
# from src.data_processing import dataprocessing
from src.classify_model import classify_model

db = CreateConnection()


if __name__ == "__main__":
    print("Welcome to the AI Project CLI")
    while(True):
        input_text = input("Start Program (datacollect/crud/voice/model/no): ")
        if input_text.lower() == "no":
            break
        elif input_text.lower() == "crud":
            print("Starting CRUD operations...")
            while True:
                input_function = input("Function (insert, getbyid, getall, update, delete): ")
                if input_function == "insert":
                    text = input("Enter text: ")
                    audio_name = input("Enter audio name: ")
                    response, message = Result.InsertResult(db, text, audio_name)
                    print(response)
                    print(message)
                elif input_function == "getbyid":
                    id = input("Enter ID: ")
                    response, message = Result.GetResultByID(db, id)
                    print(response)
                    print(message)
                elif input_function == "getall":
                    response, message = Result.GetAllResults(db)
                    print(response)
                    print(message)
                elif input_function == "update":
                    id = input("Enter ID: ")
                    new_audio_name = input("Enter new audio name: ")
                    new_text = input("Enter new text: ")
                    response, message = Result.UpdateResult(db, id, new_text, new_audio_name)
                    print(response)
                    print(message)
                elif input_function == "delete":
                    id = input("Enter ID: ")
                    response, message = Result.DeleteResult(db, id)
                    print(response)
                    print(message)
                elif input_function == "exit":
                    break
                else:
                    print("Invalid function")
        elif input_text.lower() == "datacollect":
            print("Starting camera data collection...")
            success = capture_images()
            if success:
                print("Camera data collection completed!")
            else:
                print("Camera data collection failed!")
        elif input_text.lower() == "voice":
            id = input("Enter Voice ID: ")
            text = input("Enter Text: ")
            fileName = input("Enter File Name: ")
            response = CreateSound(id,text,fileName)
            print(response)
        elif input_text.lower() == "model":
            print("Starting model")
            classify_model()
        else:
            print("Invalid input (camera/crud/no)")
    cv2.destroyAllWindows()