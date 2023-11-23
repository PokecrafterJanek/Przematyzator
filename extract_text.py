import os
import pytesseract
import cv2

folder = os.path.dirname(os.path.abspath(__file__))

tesseract_path = os.path.join(folder, 'tesseract')

pytesseract.pytesseract.tesseract_cmd = tesseract_path

folder_path = 'files/temp/pictures'

image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)

    image = cv2.imread(image_path)

    print(pytesseract.image_to_string(image, lang='pl'))