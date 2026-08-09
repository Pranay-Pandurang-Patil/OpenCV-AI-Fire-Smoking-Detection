import cv2

from detection.detector import detect


def process_webcam_frame(mode, frame):

    result, count = detect(
        mode,
        frame
    )

    return result, count