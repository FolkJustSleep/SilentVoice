from src.Display import Display_message 
from src.camera.camera import capture_images

if __name__ == "__main__":
    while(True):
        input_text = input("Start Program (yes/no/camera): ")
        if input_text.lower() == "no":
            break
        elif input_text.lower() == "yes":
            Display_message("Helloworld")
        elif input_text.lower() == "camera":
            Display_message("Starting camera data collection...")
            success = capture_images()
            if success:
                Display_message("Camera data collection completed!")
            else:
                Display_message("Camera data collection failed!")
        else: 
            Display_message("Invalid input (yes/no/camera)")