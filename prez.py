import pandas as pd
from functools import reduce
from fpdf import FPDF
import pprint


def get_info(input_dict, col_name):
    return list(input_dict[0][col_name].values())


df = pd.read_excel('/home/yuxuan/Downloads/Presidents database.xlsx', dtype=str, index_col=None, sheet_name=None)

# for sheet_name in df:
#     # print(df[sheet_name].columns)
#     df[sheet_name]['Prez Number'] = pd.to_numeric(df[sheet_name]['Prez Number'], errors='coerce')

# print(df.keys())
# first = True
# for sheet_name in df:
#     if first:
#         out = df[sheet_name]
#         first = False
#     else:
#         out = pd.merge(out, df[sheet_name], on=['Prez Number'], how='outer')
# print(out)
# print(pd.merge(df['List'], df['Nicknames'], on=['Prez Number'], how='outer'))
prez_info = []
for prez_num in range(1, 3):
    temp_info = []
    for sheet_name in df:
        temp_info.append(df[sheet_name][df[sheet_name]['Prez Number'] == str(prez_num)].to_dict())
    prez_info.append((prez_num, temp_info))

# print(prez_info)

for prez, info in prez_info:
    print(prez)
    pprint.pprint(info)
    print()
    print(str(prez) + '. ' + get_info(info, 'Name')[0])
    print('Date Born:', get_info(info, 'Date Born')[0])
    print('Date Died:', get_info(info, 'Date Died')[0])
    print('Age at death:', get_info(info, 'Age at death')[0])
    print('Burial location:', get_info(info, 'Burial location')[0])
    print('Burial city:', get_info(info, 'Burial city')[0])
    print('Burial state:', get_info(info, 'Burial state')[0])

    print('Party:', get_info(info, 'Party')[0])
    print('Date start:', get_info(info, 'Date Start')[0])
    print('Date end:', get_info(info, 'Date End')[0])
    print('State born:', get_info(info, 'State Born')[0])
    print('Age at inauguration:', get_info(info, 'Age at inauguration')[0])
    print('Office before presidency:', get_info(info, 'Office before presidency')[0])
    







# pdf = FPDF(format='letter')
# pdf.add_page()
# pdf.set_font("Arial", 'B', 24)
# pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
# pdf.output("tutorial.pdf")

# print(df['List']['Prez Number'] == '1')

