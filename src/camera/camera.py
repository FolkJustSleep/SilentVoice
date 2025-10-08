# import necessary libraries
import os
import cv2
import datetime

def find_available_cameras():
    available_cameras = []
    for i in range(10):  # Check first 10 camera indices
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            ret, _ = cap.read()
            if ret:
                available_cameras.append(i)
            cap.release()
    return available_cameras

def capture_images(number_of_classes=3, dataset_size=25, camera_index=0):
    # Find available cameras if not specified
    if camera_index is None:
        available_cameras = find_available_cameras()
        if not available_cameras:
            print("Error: No cameras found!")
            return False
        camera_index = available_cameras[0]  # Use first available camera
        print(f"Available cameras: {available_cameras}")
        print(f"Using camera index: {camera_index}")
    
    # Get project root directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    DATA_PATH = os.path.join(project_root, 'data')
    
    # create data directory if it doesn't exist
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)
        print(f"Created data directory: {DATA_PATH}")

    # file naming variables
    file_prefix = "image"
    file_extension = ".jpg"

    # initialize camera
    capture = cv2.VideoCapture(camera_index)

    # check camera is open?
    if not capture.isOpened():
        print(f"Error: Cannot open camera {camera_index}")
        return False
    else:
        print(f"Camera {camera_index} opened successfully")

    try:
        # create subdirectories for each class
        for i in range(number_of_classes):
            class_dir = os.path.join(DATA_PATH, str(i))
            if not os.path.exists(class_dir):
                os.makedirs(class_dir)
                print(f"Created directory for class {i}: {class_dir}")

        # loop for each class
        for class_num in range(number_of_classes):
            print(f"\n=== Collecting data for class {class_num} ===")
            
            # wait for user to get ready
            while True:
                ret, frame = capture.read()
                if not ret:
                    print("Error: Failed to read from camera")
                    return False
                    
                cv2.putText(frame, f'Ready for class {class_num}? Press "Q"!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.imshow('Data Collection', frame)
                if cv2.waitKey(25) == ord('q'):
                    break

            # capture images for current class
            counter = 0
            while counter < dataset_size:
                ret, frame = capture.read()
                if not ret:
                    print("Error: Failed to read from camera")
                    break
                
                # show progress on frame
                progress = ((counter + 1) / dataset_size) * 100
                cv2.putText(frame, f'Class {class_num}: {counter + 1}/{dataset_size} ({progress:.1f}%)', 
                           (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.imshow('Data Collection', frame)
                cv2.waitKey(25)
                
                # create filename with timestamp
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]  # microseconds to milliseconds
                filename = f"{file_prefix}_class{class_num}_{timestamp}_{counter:04d}{file_extension}"
                
                # save image
                file_path = os.path.join(DATA_PATH, str(class_num), filename)
                cv2.imwrite(file_path, frame)
                
                # show progress in console
                print(f"Capturing image {counter + 1}/{dataset_size} for class {class_num} - Progress: {progress:.1f}%")
                
                counter += 1
                
            print(f"Completed collecting {dataset_size} images for class {class_num}")

        print(f"\n Data collection completed successfully!")
        print(f"Images saved to: {DATA_PATH}")
        return True

    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # disable camera
        capture.release()
        cv2.destroyAllWindows()
        print("Camera released and windows closed")

if __name__ == "__main__":
    # Run the capture function when script is executed directly
    success = capture_images()
    if success:
        print("Image capture completed successfully!")
    else:
        print("Image capture failed!")