from ultralytics import YOLO
from config import FIRE_MODEL_PATH, CONFIDENCE

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