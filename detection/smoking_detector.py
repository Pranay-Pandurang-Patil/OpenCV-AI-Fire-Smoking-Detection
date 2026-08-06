from ultralytics import YOLO

model = YOLO("models/smoking/best.onnx", task="detect")


def detect(image):

    results = model.predict(
        source=image,
        conf=0.5,
        verbose=False
    )

    result = results[0].plot()

    count = len(results[0].boxes)

    return result, count