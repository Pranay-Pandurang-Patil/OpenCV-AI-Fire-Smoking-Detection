import cv2

from detection.fire_detector import detect

cap = cv2.VideoCapture(0)

cv2.namedWindow("Live Fire Detection", cv2.WINDOW_NORMAL)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    result = detect(frame)

    cv2.imshow("Live Fire Detection", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()