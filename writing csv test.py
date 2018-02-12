# this will write only names
import csv
ifile = open('./datasets/train.csv', 'r')
reader = csv.reader(ifile)


name = []
c=0
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "saving csv data"

for i in reader:
    name.append(i[3])
    c=c+1
print(len(name))
for i in range(1,len(name)):
    ws.cell(row=i, column=1, value=name[i])
    print(name[i])

wb.save('csv_data_save.xlsm')
ifile.close()
print('Operation Successful')