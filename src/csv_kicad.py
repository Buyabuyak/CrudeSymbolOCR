import os
import pandas as pd

# creates a human dictionnary for pin electrical type
type_dict = {"input": ["input", "I", "Input"],
"output": ["output", "O", "Output"],
"bidirectional": ["bidirectional", "I/O"],
"tri_state": ["tri_state"],
"passive": ["passive"],
"free": ["free"],
"unspecified": ["unspecified"],
"power_in": ["power_in"],
"power_out": ["power_out"],
"open_collector": ["open_collector"],
"open_emitter": ["open_emitter"],
"unconnected": ["unconnected"],
}

# creates a lookup table, aka normal python dictionnary, from the human one
lookup = dict((number, name) for name, numbers in type_dict.items() for number in numbers)

# function to check if input exists in the dict, else return default
def typeMatch(input):
  try:
    return(lookup[input])
  except:
    return("unspecified")

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

param = """      (pin {type} line (at 0 {pos:.2f} 0) (length 2.54)
        (name "{name}" (effects (font (size 1.27 1.27))))
        (number "{number}" (effects (font (size 1.27 1.27))))
      )"""


df = pd.read_csv(csv_file, delimiter=' ')   # read the csv file
sorted = df.sort_values("Number")           # sort the file according to the pin number column

with open(sym_file, 'w') as symfile:
    symfile.write(start)
    i = 0
    for index, _ in sorted.iterrows():      # write the data for each pin
        symfile.write(param.format(pos=-i,
                                  name=sorted.at[index, "Name"],
                                  number=sorted.at[index, "Number"],
                                  type=typeMatch(sorted.at[index, "ElectricalType"])))
        i = i + 2.54
    symfile.write(end)