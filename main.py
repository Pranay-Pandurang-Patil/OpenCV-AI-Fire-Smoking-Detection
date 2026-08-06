import cv2
import time

from detection.detector import detect
from utils.image_loader import load_image

print("\n====== AI Safety Monitoring System ======\n")

print("Detection Mode")
print("1. Fire")
print("2. Smoking")

choice = input("\nEnter Choice : ")

if choice == "1":
    mode = "fire"
elif choice == "2":
    mode = "smoking"
else:
    print("Invalid Choice")
    exit()

print("\nInput Type")
print("1. Image")
print("2. Video")
print("3. Webcam")

source = input("\nEnter Choice : ")

# -------------------------
# IMAGE
# -------------------------

if source == "1":

    path = input("\nEnter Image Path : ")

    img = load_image(path)

    result, count = detect(mode, img)

    cv2.putText(
    result,
    f"Objects : {count}",
    (20, 90),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 255),
    2,
    )

    cv2.imshow("Detection", result)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

# -------------------------
# VIDEO
# -------------------------

elif source == "2":

    path = input("\nEnter Video Path : ")

    cap = cv2.VideoCapture(path)
    prev_time = 0

    cv2.namedWindow("Detection", cv2.WINDOW_NORMAL)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        result, count = detect(mode, frame)
        current_time = time.time()

        if prev_time == 0:
         fps = 0
        else:
           fps = 1 / (current_time - prev_time)

        prev_time = current_time

        cv2.putText(
    result,
    f"FPS : {int(fps)}",
    (20, 90),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 0),
    2,
        )
        cv2.putText(
    result,
    f"Objects : {count}",
    (20, 125),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 255),
    2,
)

        cv2.imshow("Detection", result)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()

# -------------------------
# WEBCAM
# -------------------------

elif source == "3":

    cap = cv2.VideoCapture(0)
    prev_time = 0

    cv2.namedWindow("Detection", cv2.WINDOW_NORMAL)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        result, count = detect(mode, frame)

        current_time = time.time()

        if prev_time == 0:
            fps = 0
        else:
            fps = 1 / (current_time - prev_time)

        prev_time = current_time

        cv2.putText(
    result,
    f"FPS : {int(fps)}",
    (20, 90),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 0),
    2,
        )
        cv2.putText(
    result,
    f"Objects : {count}",
    (20, 125),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 255),
    2,
)

        cv2.imshow("Detection", result)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()

else:

    print("Invalid Choice")