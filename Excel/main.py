import csv

import xlsxwriter

'''Example for reading csv and writing to Excel
'''

lines_list = []


with open('fakedata.csv', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    #Write header names to keys list
    keys = csv_reader.fieldnames
    for row in csv_reader:
        # print(row)  # Each row is an OrderedDict where keys are column names
        lines_list.append(row)

print(lines_list)

#Prepare Excel File
workbook = xlsxwriter.Workbook('csv_output.xlsx')
worksheet = workbook.add_worksheet()

#write headers
for key_index,key in enumerate(keys):
    worksheet.write(0,key_index,key)

#write Values
item: dict[str]
for index, item in enumerate(lines_list):
    key: str
    for key_index, key in enumerate(keys):
        worksheet.write(index+1,key_index,item[key])


workbook.close()