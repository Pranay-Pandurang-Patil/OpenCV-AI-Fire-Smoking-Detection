from pathlib import Path
from urllib.request import urlretrieve

from ultralytics import YOLO

from config import SMOKING_MODEL_PATH, CONFIDENCE


MODEL_URL = (
    "https://raw.githubusercontent.com/"
    "alihassanml/Smoking-detection-yolo11/"
    "main/best.onnx"
)


def download_model():

    model_path = Path(SMOKING_MODEL_PATH)

    if not model_path.exists():

        model_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        print("Downloading smoking detection model...")

        urlretrieve(
            MODEL_URL,
            model_path
        )

        print("Smoking detection model downloaded.")


download_model()

model = YOLO(
    SMOKING_MODEL_PATH,
    task="detect"
)


def detect(image):

    results = model.predict(
        source=image,
        conf=CONFIDENCE,
        verbose=False
    )

    result = results[0].plot()

    count = len(results[0].boxes)

    return result, count