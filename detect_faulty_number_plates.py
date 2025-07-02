import cv2
import pytesseract
import re
import os

# Set tesseract path if needed, e.g.:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def is_faulty_plate(plate_text):
    # Example: Indian number plate pattern (customize as needed)
    pattern = r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$'
    return not re.match(pattern, plate_text.replace(" ", ""))

def detect_number_plate(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Could not read image: {image_path}")
        return None, None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Use thresholding to help OCR
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # OCR to extract text
    text = pytesseract.image_to_string(thresh, config='--psm 8')
    plate_text = ''.join(filter(str.isalnum, text)).upper()
    return plate_text, is_faulty_plate(plate_text)

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            plate_text, faulty = detect_number_plate(image_path)
            if plate_text:
                print(f"Image: {filename} | Plate: {plate_text} | Faulty: {faulty}")
            else:
                print(f"Image: {filename} | Plate not detected.")

if __name__ == "__main__":
    # Update this path to your images folder
    images_folder = "number_plate_images"
    process_folder(images_folder)
