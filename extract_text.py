import os
import pytesseract
import cv2
import re
from difflib import SequenceMatcher

def extract():
    folder = os.path.dirname(os.path.abspath(__file__))

    tesseract_path = os.path.join(folder, 'tesseract/tesseract.exe').replace('\\', '/')

    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    folder_path = 'files/temp/pictures'

    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

    language = input('Give language abbreviation: ')

    contents = []

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)

        image = cv2.imread(image_path)

        contents.append(pytesseract.image_to_string(image, lang = language))

    get_data(contents)

def check_difference(str1, str2):
    seq_matcher = SequenceMatcher(None, str1, str2)
    similarity = seq_matcher.ratio()

    difference = (1 - similarity) * 100

    return difference

def get_data(contents):
    pattern = re.compile('[^a-zA-Z0-9]')

    purged = []

    for x in contents:
        purged.append(re.sub(pattern, '', x))

    toRemove = []

    for x in range(len(purged) - 1, 0, -1):
        if check_difference(purged[x], purged[x - 1]) < 90:
            toRemove.append(x - 1)

    for x in toRemove:
        contents.pop(x)

    output_path = "files/output.txt"

    with open(output_path, 'w') as file:
        for item in contents:
            file.write("%s\n" % item)