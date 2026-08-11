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

        temp_model_path = model_path.with_suffix(".pt")

        urlretrieve(
            MODEL_URL,
            temp_model_path
        )

        print("Fire detection model downloaded.")

        print("Exporting fire model to ONNX...")

        temp_model = YOLO(temp_model_path)

        temp_model.export(
            format="onnx"
        )

        exported_model = temp_model_path.with_suffix(".onnx")

        exported_model.rename(
            model_path
        )

        temp_model_path.unlink()

        print("Fire ONNX model ready.")


download_model()


model = YOLO(
    FIRE_MODEL_PATH,
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