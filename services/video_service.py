import cv2

from detection.detector import detect


def process_video_live(mode, video_path, frame_callback):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError("Unable to open video file.")

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30.0

    frame_count = 0
    total_objects = 0

    try:

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            # -----------------------------
            # YOLO DETECTION
            # -----------------------------

            result, count = detect(
                mode,
                frame
            )

            frame_count += 1
            total_objects += count

            # -----------------------------
            # SEND PROCESSED FRAME
            # TO STREAMLIT
            # -----------------------------

            frame_callback(
                result,
                count,
                frame_count,
                fps
            )

    finally:

        cap.release()

    return frame_count, total_objects