import xlsxwriter

'''Example of writing one cell to excel
'''

workbook = xlsxwriter.Workbook('file.xlsx')
worksheet = workbook.add_worksheet()

# Cell Formatting
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Title', bold)

workbook.close()