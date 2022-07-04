from PIL import Image
from pytesseract import pytesseract
import re
import os

input_dir = './input/'
output_dir = './output/'
csv_file = 'pinout.csv'

if os.path.exists(output_dir + csv_file):
    os.remove(output_dir + csv_file) 

with open(output_dir + csv_file, 'a') as f:

    for files in os.listdir(input_dir):
        print(input_dir + files)
        img = Image.open(input_dir + files)
        original = pytesseract.image_to_string(img)
        filtered = re.sub(r'\n\s*\n','\n',original,re.MULTILINE)
        print(filtered[:-1])
        f.write(filtered[:-1] + '\n')