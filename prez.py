import pandas as pd
from functools import reduce
from fpdf import FPDF
import pprint


def get_info(input_dict):
    return list(input_dict.values())


df = pd.read_excel('/home/yuxuan/Downloads/Presidents database.xlsx', dtype=str, index_col=None, sheet_name=None)

prez_info = []
for prez_num in range(1, 3):
    temp_info = []
    for sheet_name in df:
        temp_info.append(df[sheet_name][df[sheet_name]['Prez Number'] == str(prez_num)].to_dict())
    prez_info.append((prez_num, temp_info))

# print(prez_info)

for prez, info in prez_info:
    first = True
    print(prez)
    pprint.pprint(info)
    print()
    for prez_dict in info:
        for column_name, prez_info in prez_dict.items():
            if first and column_name == 'Prez Number':
                print(column_name + ':', get_info(prez_info))
                first = False
            if column_name != 'Prez Number':
                print(column_name + ':', get_info(prez_info))








# pdf = FPDF(format='letter')
# pdf.add_page()
# pdf.set_font("Arial", 'B', 24)
# pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
# pdf.output("tutorial.pdf")

# print(df['List']['Prez Number'] == '1')

