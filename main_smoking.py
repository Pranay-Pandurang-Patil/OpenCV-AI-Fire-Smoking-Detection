import cv2

from utils.image_loader import load_image
from detection.smoking_detector import detect

IMAGE_PATH = "images/test.png"

img = load_image(IMAGE_PATH)

result = detect(img)

screen_width = 1280
screen_height = 720

h, w = result.shape[:2]

scale = min(screen_width / w, screen_height / h)

display = cv2.resize(result, (int(w * scale), int(h * scale)))

cv2.namedWindow("Smoking Detection", cv2.WINDOW_NORMAL)
cv2.imshow("Smoking Detection", display)

cv2.imwrite("outputs/smoking/result.png", result)

cv2.waitKey(0)
cv2.destroyAllWindows()