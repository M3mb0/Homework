import csv
from pdf_generator import generate


with open("employee.csv") as fin:
    reader = csv.reader(fin.readlines())
    for itm in reader:
        name = itm[0] + ' ' + itm[1]
        wage = int(itm[-2])
        days_off = int(itm[-1])
        generate(name, wage, days_off, "Cristi")
