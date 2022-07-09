import os
from openpyxl import Workbook
from openpyxl import load_workbook
# openpyxl is python library to read/write excel

dest_wb = Workbook()

# dir where my excel files are. The combined file will also be saved here. 
dir_containing_files = "/home/hus/Documents"

# os.walk() returns current_path, directories in current_path, files in current_path
for root, dirs, filenames in os.walk(dir_containing_files):
    for file in filenames:
        if file.endswith('.xlsx'):
            # file is with extension. Get rid of extension as file_name
            file_name = file.split('.')[0]
            file_path = os.path.abspath(os.path.join(root, file))

            dest_wb.create_sheet(file_name)
            dest_ws = dest_wb[file_name]

            source_wb = load_workbook(file_path)
            # This assumes there is only one tab
            source_sheet = source_wb.active
            for row in source_sheet.rows:
                for cell in row:
                    dest_ws[cell.coordinate] = cell.value

os.chdir(dir_containing_files)
dest_wb.remove(dest_wb['Sheet'])
dest_wb.save("total.xlsx")
