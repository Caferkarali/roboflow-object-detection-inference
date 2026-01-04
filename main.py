import requests
import json
from roboflow import Roboflow

# =================CONFIGURATION=================
# Please replace the placeholders below with your actual Roboflow credentials
API_KEY = "YOUR_ROBOFLOW_API_KEY"
WORKSPACE_NAME = "YOUR_WORKSPACE_NAME"
PROJECT_NAME = "YOUR_PROJECT_NAME"
MODEL_VERSION = 1
IMAGE_PATH = "path/to/your/image.jpg"


# ===============================================

def test_connection(url="https://detect.roboflow.com/"):
    """Tests the connection to the Roboflow API."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Connection successful!")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        return False


def main():
    # 1. Test Connection
    if not test_connection():
        print("Cannot connect to Roboflow API. Please check your internet connection.")
        return

    # 2. Load the Model
    try:
        print(f"Loading model: {PROJECT_NAME} (Version: {MODEL_VERSION})...")
        rf = Roboflow(api_key=API_KEY)
        workspace = rf.workspace(WORKSPACE_NAME)
        project = workspace.project(PROJECT_NAME)
        model = project.version(MODEL_VERSION).model
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Failed to load model. Check your API Key and Project details. Error: {e}")
        return

    # 3. Make Prediction
    try:
        print(f"Analyzing image: {IMAGE_PATH}...")
        # confidence=20 means 20% threshold, overlap=30 means 30% IOU threshold
        prediction = model.predict(IMAGE_PATH, confidence=20, overlap=30).json()

        predictions = prediction['predictions']

        if predictions:
            # Print the top prediction
            top_prediction = predictions[0]
            predicted_class = top_prediction['class']
            confidence = top_prediction['confidence']

            print("\n--- Result ---")
            print(f"Predicted Class: {predicted_class}")
            print(f"Confidence Score: {confidence:.2f}")
            print(f"Total Objects Detected: {len(predictions)}")
        else:
            print("\nNo objects detected with the current confidence threshold.")
            # Optional: Print full JSON for debugging
            # print(json.dumps(prediction, indent=4))

    except Exception as e:
        print(f"Prediction failed: {e}")
        print("Please ensure the image path is correct and the file exists.")


if __name__ == "__main__":
    main()