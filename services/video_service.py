import cv2
import tempfile
import os

from detection.detector import detect


def process_video(mode, video_path):

    cap = cv2.VideoCapture(video_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_file.name,
        fourcc,
        fps,
        (width, height)
    )

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        result, count = detect(mode, frame)

        out.write(result)

    cap.release()
    out.release()

    return output_file.name