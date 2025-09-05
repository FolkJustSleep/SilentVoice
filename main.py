from src.Display import Display_message 
from database.supabase import CreateConnection
from src.camera.camera import capture_images
import src.service.Result as Result

db = CreateConnection()


if __name__ == "__main__":
    while(True):
        input_text = input("Start Program (camera/crud/no): ")
        if input_text.lower() == "no":
            break
        elif input_text.lower() == "crud":
            Display_message("Helloworld")
            while True:
                input_function = input("Function (insert, getbyid, getall, update, delete): ")
                if input_function == "insert":
                    text = input("Enter text: ")
                    audio_name = input("Enter audio name: ")
                    response, message = Result.InsertResult(db, text, audio_name)
                    print(response)
                    Display_message(message)
                elif input_function == "getbyid":
                    id = input("Enter ID: ")
                    response, message = Result.GetResultByID(db, id)
                    print(response)
                    Display_message(message)
                elif input_function == "getall":
                    response, message = Result.GetAllResults(db)
                    print(response)
                    Display_message(message)
                elif input_function == "update":
                    id = input("Enter ID: ")
                    new_audio_name = input("Enter new audio name: ")
                    new_text = input("Enter new text: ")
                    response, message = Result.UpdateResult(db, id, new_text, new_audio_name)
                    print(response)
                    Display_message(message)
                elif input_function == "delete":
                    id = input("Enter ID: ")
                    response, message = Result.DeleteResult(db, id)
                    print(response)
                    Display_message(message)
                elif input_function == "exit":
                    break
                else:
                    Display_message("Invalid function")
        elif input_text.lower() == "camera":
            Display_message("Starting camera data collection...")
            success = capture_images()
            if success:
                Display_message("Camera data collection completed!")
            else:
                Display_message("Camera data collection failed!")
        else:
            Display_message("Invalid input (camera/crud/no)")
