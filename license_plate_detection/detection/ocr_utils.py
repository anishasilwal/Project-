# detection/ocr_utils.py

import cv2
import pytesseract

def perform_ocr(image_path):
    """
    This function takes an image path as input and returns the detected text using OCR.
    """
    image = cv2.imread(image_path)
    plate_text = pytesseract.image_to_string(image)
    return plate_text
