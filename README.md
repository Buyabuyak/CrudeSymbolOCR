# CrudeSymbolOCR

Quite a lot of mistakes while making symmbols are made from wrong pin definition...
( ask how i know )

So I tried to create a really crude ocr in order create kicad symbols.
But it was mostly not working, current ocr relies heavily on ditionnaries,
and pin names are not quite in them...

So the current version reads the selectable text from the pdf
and make the symbol from it, easy ! ( and accurate this time)
( the old ocr version is still there if you want to try it )

## Example

- get a datasheet ( ex https://www.ti.com/lit/ds/symlink/cc1352r.pdf )
- launch main.py

- Create the data
  - select the file
  - go to the page you want and select the table ( name / pin )
  - press on get table
  - select another table if necessary
- Edit/Check the data
  - gedit is opened as default
  - edit the data if you need to
  - if for some reason there's a letter/char in the pin numbers column, it will ne be ordered properly on the symbol
- Enjoy !
  - Import the symbol in kicad

## install on Ubuntu

sudo  python3 -m pip install opencv-python pymupdf numpy pandas
git clone https://github.com/Buyabuyak/CrudeSymbolOCR

## license

Yep

## Special thanks to the devs at pymupdf for the lib and exemple !