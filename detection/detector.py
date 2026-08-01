from config import DETECTION_MODE


def detect(image):

    if DETECTION_MODE == "smoking":
        print("Smoking Detection Mode")

    elif DETECTION_MODE == "fire":
        print("Fire Detection Mode")

    elif DETECTION_MODE == "smoke":
        print("Smoke Detection Mode")

    else:
        print("Unknown Mode")

    return image