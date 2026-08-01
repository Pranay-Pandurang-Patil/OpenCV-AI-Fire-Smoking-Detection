import cv2

from config import IMAGE_PATH, OUTPUT_FIRE
from utils.image_loader import load_image
from detection.fire_detector import detect

# Load Image
img = load_image(IMAGE_PATH)

# Detect Fire
result = detect(img)

# -----------------------------
# Resize for Display
# -----------------------------
screen_width = 1280
screen_height = 720

h, w = result.shape[:2]

scale = min(screen_width / w, screen_height / h)

new_w = int(w * scale)
new_h = int(h * scale)

display = cv2.resize(result, (new_w, new_h))

# -----------------------------
# Create Resizable Window
# -----------------------------
cv2.namedWindow("Fire Detection", cv2.WINDOW_NORMAL)

cv2.imshow("Fire Detection", display)

# Save Original Quality Image
cv2.imwrite(OUTPUT_FIRE, result)

cv2.waitKey(0)
cv2.destroyAllWindows()