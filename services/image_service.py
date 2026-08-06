from detection.detector import detect


def process_image(mode, image):

    result, count = detect(mode, image)

    return result, count