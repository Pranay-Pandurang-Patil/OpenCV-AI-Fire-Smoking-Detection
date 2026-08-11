from pathlib import Path


# ==========================
# Project Root
# ==========================

BASE_DIR = Path(__file__).resolve().parent


# ==========================
# Image
# ==========================

IMAGE_PATH = BASE_DIR / "images" / "test.png"


# ==========================
# Models
# ==========================

FIRE_MODEL_PATH = BASE_DIR / "models" / "fire" / "best.onnx"

SMOKING_MODEL_PATH = BASE_DIR / "models" / "smoking" / "best.onnx"


# ==========================
# Output
# ==========================

OUTPUT_FIRE = BASE_DIR / "outputs" / "fire" / "result.png"

OUTPUT_SMOKING = BASE_DIR / "outputs" / "smoking" / "result.png"


# ==========================
# Detection Mode
# ==========================

DETECTION_MODE = "fire"

# fire
# smoking


# ==========================
# Detection Settings
# ==========================

CONFIDENCE = 0.50