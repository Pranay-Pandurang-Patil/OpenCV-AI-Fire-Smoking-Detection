from detection.fire_detector import detect as fire_detect
from detection.smoking_detector import detect as smoking_detect

import cv2


def detect(mode, image):

    if mode == "fire":

        result, count = fire_detect(image)

        cv2.rectangle(result, (0, 0), (result.shape[1], 60), (0, 0, 255), -1)

        cv2.putText(
            result,
            "FIRE DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )

        return result, count

    elif mode == "smoking":

        result, count = smoking_detect(image)

        cv2.rectangle(result, (0, 0), (result.shape[1], 60), (0, 140, 255), -1)

        cv2.putText(
            result,
            "SMOKING DETECTED",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )

        return result, count

    else:

        raise ValueError("Invalid Detection Mode")