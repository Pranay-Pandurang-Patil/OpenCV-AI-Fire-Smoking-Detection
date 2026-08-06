from utils.image_loader import load_image

from services.image_service import process_image
from services.video_service import process_video
from services.webcam_service import process_webcam

import cv2

print("\n====== AI Safety Monitoring System ======\n")

print("Detection Mode")
print("1. Fire")
print("2. Cigarette Smoking")

choice = input("\nEnter Choice : ")

mode = "fire" if choice == "1" else "smoking"

print("\nInput Type")
print("1. Image")
print("2. Video")
print("3. Webcam")

source = input("\nEnter Choice : ")

# ---------------- IMAGE ---------------- #

if source == "1":

    path = input("\nEnter Image Path : ")

    img = load_image(path)

    result, count = process_image(mode, img)

    cv2.imshow("Detection", result)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

# ---------------- VIDEO ---------------- #

elif source == "2":

    path = input("\nEnter Video Path : ")

    frames = process_video(mode, path)

    for frame in frames:

        cv2.imshow("Detection", frame)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

# ---------------- WEBCAM ---------------- #

elif source == "3":

    process_webcam(mode)

else:

    print("Invalid Choice")