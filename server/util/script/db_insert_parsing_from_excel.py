from openpyxl import load_workbook
import sys

cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z', 'AA', 'AB']
rows = 1
wb = load_workbook('temp.xlsx')
sheets = wb.get_sheet_names()
for sheet in sheets:
    sheet_ranges = wb[sheet]
    while True:
        check = 0
        rows = rows + 1
        for field in cols:
            sys.stdout.write(str(sheet_ranges[field + str(rows)].value) + " ")
            if sheet_ranges[field + str(rows)].value != None:
                check += 1
        if check == 0:
            break
        print()
        print()
        print(rows)
        print()
        print()

