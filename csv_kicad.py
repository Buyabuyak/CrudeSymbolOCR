import os
import pandas as pd

output_dir = './output/'
csv_file = 'pinout.csv'
sym_file = 'symbol.kicad_sym'

start = """(kicad_symbol_lib (version 20211014) (generator symbolOCR)
  (symbol "test" (in_bom yes) (on_board yes)
    (property "Reference" "U" (id 0) (at 0 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Value" "test" (id 1) (at 0 0 0)
      (effects (font (size 1.27 1.27)))
    )
    (property "Footprint" "" (id 2) (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (property "Datasheet" "" (id 3) (at 0 0 0)
      (effects (font (size 1.27 1.27)) hide)
    )
    (symbol "test_1_1" """

end = """
    )
  )
)
"""

param = """      (pin input line (at 0 {pos:.2f} 0) (length 2.54)
        (name "{name}" (effects (font (size 1.27 1.27))))
        (number "{number}" (effects (font (size 1.27 1.27))))
      )"""


df = pd.read_csv(output_dir + csv_file, header=None)
sorted = df.sort_values(1)

with open(output_dir + sym_file, 'w') as symfile:
    symfile.write(start)
    i = 0
    for index, row in sorted.iterrows():
        symfile.write(param.format(pos=i, name=row[0], number=row[1]))
        i = i - 2.54
    symfile.write(end)
















# with open(output_dir + sym_file, 'w') as symfile:

#     symfile.write(start)

#     i = 0

#     with open(output_dir + csv_file, mode ='r') as csvfile:
#         csvReader = csv.reader(csvfile)
#         for lines in csvReader:
#             symfile.write(param.format(pos=i, name=lines[0], number=lines[1]))
#             i = i - 2.54
    
#     symfile.write(end)