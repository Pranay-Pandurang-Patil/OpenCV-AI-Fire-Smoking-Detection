import os

# Allow trusted YOLO .pt checkpoints to be loaded
# with the normal PyTorch loader.
os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"

from pathlib import Path
from urllib.request import urlretrieve

from ultralytics import YOLO

from config import FIRE_MODEL_PATH, CONFIDENCE


MODEL_URL = (
    "https://raw.githubusercontent.com/"
    "luminous0219/fire-and-smoke-detection-yolov8/"
    "main/weights/best.pt"
)


def download_model():

    model_path = Path(FIRE_MODEL_PATH)

    if not model_path.exists():

        model_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        print("Downloading fire detection model...")

        urlretrieve(
            MODEL_URL,
            model_path
        )

        print("Fire detection model downloaded.")


download_model()


model = YOLO(FIRE_MODEL_PATH)


def detect(image):

    results = model.predict(
        source=image,
        conf=CONFIDENCE,
        verbose=False
    )

    result = results[0].plot()

    count = len(results[0].boxes)

    return result, count