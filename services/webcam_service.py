import cv2

from detection.detector import detect


def process_webcam(mode):

    cap = cv2.VideoCapture(0)

    cv2.namedWindow("AI Safety Monitoring System", cv2.WINDOW_NORMAL)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        result, count = detect(mode, frame)

        cv2.imshow("AI Safety Monitoring System", result)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()