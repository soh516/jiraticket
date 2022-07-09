import os
from openpyxl import Workbook
from openpyxl import load_workbook

dest_wb = Workbook()

dir_containing_files = "/home/hus/Documents"

for root, dir, filenames in os.walk(dir_containing_files):
    for file in filenames:
        file_name = file.split('.')[0]
        file_path = os.path.abspath(os.path.join(root, file))

        dest_wb.create_sheet(file_name)
        dest_ws = dest_wb[file_name]

        source_wb = load_workbook(file_path)
        source_sheet = source_wb.active
        for row in source_sheet.rows:
            for cell in row:
                dest_ws[cell.coordinate] = cell.value

os.chdir(dir_containing_files)
dest_wb.remove(dest_wb['Sheet'])
dest_wb.save("total.xlsx")
