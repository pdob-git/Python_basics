import csv
import xlsxwriter

'''Example for reading csv and writing to excel
'''

lines_list = []
keys = []


with open('fakedata.csv', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    #Write header names to keys list
    keys = csv_reader.fieldnames
    for row in csv_reader:
        # print(row)  # Each row is an OrderedDict where keys are column names
        lines_list.append(row)

# print(lines_list)

#Prepare excel File
workbook = xlsxwriter.Workbook('file.xlsx')
worksheet = workbook.add_worksheet()

#write headers
for key_index,key in enumerate(keys):
    worksheet.write(0,key_index,key)

#write Values
for index, item in enumerate(lines_list):
    for key_index, key in enumerate(keys):
        worksheet.write(index+1,key_index,item[key])


workbook.close()