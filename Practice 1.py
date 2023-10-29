import openpyxl

files = ["1111.xlsx", "2222.xlsx", "3333.xlsx"]
data = []

for i in files:
    wb = openpyxl.load_workbook(files)
    sheet = wb.active
    for row in sheet.iter_rows(values_only=True):
        data.extend(row)

data.sort(reverse=True)

for row in data:
    print(row)