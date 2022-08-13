import cv2
from pytesseract import pytesseract
import re
import os

input_dir = './input/'
output_dir = './output/'
csv_file = 'pinout.csv'

custom_config = r'-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_ --psm 6 lang=d'

with open(output_dir + csv_file, 'w') as f:

    for files in os.listdir(input_dir):
        print(input_dir + files)

        image = cv2.imread(input_dir + files)
        cv2.imshow("raw", image)
        cv2.waitKey(0)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", image)
        cv2.waitKey(0)

        # image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        # cv2.imshow("thres ", image)
        # cv2.waitKey(0) 

        cv2.destroyAllWindows()

        original = pytesseract.image_to_string(image, config=custom_config)

        filtered = re.sub(r'\n\s*\n','\n',original,re.MULTILINE)
        print(filtered[:-1])
        f.write(filtered[:-1] + '\n')