import os
import json
from pprint import pprint
import xlsxwriter

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0


directory_list = list()
names_list = list()

for root, dirs, files in os.walk("C:\\WORK\\TEST_DATA\\Data_SET\\DATA_FOR_STAT\\clear_json", topdown=False):
    for name in files:
        names_list.append(name)
        directory_list.append(os.path.join(root, name))

for idx, i in enumerate(directory_list):
        with open(i) as f:
            data = json.load(f)
            os.path.splitext(i)
            # print('Go throw element: ', idx)
            # pprint(data["volume_parameters"]["chest"])
            # pprint(data["volume_parameters"]["waist"])
            # pprint(data["volume_parameters"]["hips"])
            worksheet.write(row, col, i)
            worksheet.write(row, col + 1, data["volume_parameters"]["chest"])
            worksheet.write(row, col + 2, data["volume_parameters"]["waist"])
            worksheet.write(row, col + 3, data["volume_parameters"]["hips"])
            row += 1

workbook.close()




