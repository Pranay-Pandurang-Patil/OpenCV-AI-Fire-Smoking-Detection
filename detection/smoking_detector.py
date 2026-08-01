from ultralytics import YOLO

model = YOLO("models/smoking/best.onnx", task="detect")


def detect(image):

    results = model.predict(
        source=image,
        conf=0.5,
        verbose=False
    )

    return results[0].plot()