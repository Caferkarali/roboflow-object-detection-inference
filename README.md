# 👁️ Roboflow Object Detection Inference Script

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Roboflow](https://img.shields.io/badge/API-Roboflow-purple)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview
This project demonstrates how to integrate **Roboflow's Inference API** into a Python application. It connects to a custom-trained computer vision model hosted on Roboflow and performs object detection on local images.

The script handles API connection testing, model loading, and parsing the JSON prediction response to display the detected class and confidence score.

## 🚀 Features
* **Connection Check:** Validates internet connection to Roboflow servers before execution.
* **Model Integration:** Loads custom models dynamically using Workspace and Project names.
* **Inference:** Runs object detection on local image files.
* **Result Parsing:** Extracts and displays the most relevant prediction data (Class & Confidence).

## 🛠 Prerequisites

To run this script, you need:
1.  A **Roboflow** account.
2.  A trained project/model on Roboflow.
3.  Your **Private API Key**.

## 💻 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/roboflow-object-detection-inference.git
    cd roboflow-object-detection-inference
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration:**
    Open `main.py` and update the configuration section with your credentials:
    ```python
    API_KEY = "YOUR_ROBOFLOW_API_KEY"
    WORKSPACE_NAME = "your-workspace-name"
    PROJECT_NAME = "your-project-name"
    IMAGE_PATH = "test_image.jpg"
    ```

    *> **Note:** Never commit your actual API Key to public repositories.*

4.  **Run the script:**
    ```bash
    python main.py
    ```

## 📊 Sample Output
```text
Connection successful!
Loading model: construction-safety (Version: 1)...
Model loaded successfully.
Analyzing image: site.jpg...

--- Result ---
Predicted Class: Helmet
Confidence Score: 0.89
Total Objects Detected: 3
