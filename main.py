from src.Display import Display_message 

if __name__ == "__main__":
    while(True):
        input_text = input("Start Program : ")
        if input_text.lower() == "no":
            break
        if input_text.lower() == "yes":
            Display_message("Helloworld")
        else: 
            Display_message("Invalid input (yes/no)")