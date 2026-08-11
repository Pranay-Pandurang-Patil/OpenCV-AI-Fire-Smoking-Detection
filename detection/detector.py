from detection.fire_detector import detect as fire_detect
from detection.smoking_detector import detect as smoking_detect


def detect(mode, image):

    if mode == "fire":

        result, count = fire_detect(image)

        return result, count

    elif mode == "smoking":

        result, count = smoking_detect(image)

        return result, count

    else:

        raise ValueError(
            "Invalid Detection Mode"
        )