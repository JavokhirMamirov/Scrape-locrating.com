import openpyxl
import pandas as pd
# file1 = openpyxl.load_workbook('report.xlsx')
# file2 = openpyxl.load_workbook('report1100-.xlsx')

excel1 = pd.read_excel('report.xlsx')
excel2 = pd.read_excel('report1100-.xlsx')

excel_marged = pd.concat([excel1, excel2], ignore_index=True)

excel_marged.to_excel('all_report.xlsx', index=False)
