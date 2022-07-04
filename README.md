# CrudeSymbolOCR

Quite a lot of mistakes while making symmbols are made from wrong pin definition...
( ask how i know )

So I trid to create a really crude ocr in order create kicad symbols.

## Example
- get a datasheet ( ex https://www.ti.com/lit/ds/symlink/cc1352r.pdf )
- Create a csv with the pinout
  - find the pinout table
  - screenshot the text you want, make it the highest quality with anything but the text
  - save the screenshots in the input file
  - run ocr_csv.py
- Clean the csv (./output/pinout.csv)
  - open the csv with libreOffice
  - check the data
  - remove empty rows
  - save the csv file
- Create the symbol
  - run csv_kicad
- Import the symbol in kicad
  - in the symbol editor
  - go to the lib you want
  - file > import symbol > the symbol you juste created
- Enjoy !
  - ( in theory this method should be faster and less error prone than a manual one, we'll see )



## install on Ubuntu

sudo apt-get update && sudo apt-get install tesseract-ocr
sudo -m python3 pip install opencv-python pytesseract numpy pandas

## license

None yet