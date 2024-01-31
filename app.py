import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']
cell = sheet.cell(1,1)

for row in range(1, sheet.max_row + 1):
    sheet.cell(row,3)