import cv2
import pytesseract

def perform_ocr(image_path):
    image = cv2.imread(image_path)
    plate_text = pytesseract.image_to_string(image)
    return plate_text