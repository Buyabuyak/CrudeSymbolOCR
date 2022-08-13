import os

# yup, that's not a good way to make it work,
# but for the moment I just want to test it...

os.system('python3 ./src/wxTableExtract.py')
os.system('gedit ./pinout.csv')
os.system('python3 ./src/csv_kicad.py')