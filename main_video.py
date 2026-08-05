import cv2

from detection.fire_detector import detect

VIDEO_PATH = "videos/test.mp4"
OUTPUT_PATH = "outputs/fire/output.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))

cv2.namedWindow("Fire Video Detection", cv2.WINDOW_NORMAL)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    result = detect(frame)

    out.write(result)

    cv2.imshow("Fire Video Detection", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()

cv2.destroyAllWindows()