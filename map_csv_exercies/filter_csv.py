"""Extract in a csv f all the secondary schools from another csv f"""

import csv


# lst = []

def scoli_gimnaziale(line):
    school = line[0].split(";")
    if "SCOALA GIMNAZIALA" in school[2] and "Comuna" in line[1]:
        return True
    return False


with open(r"C:\Users\ravva\PycharmProjects\Homework\map_csv_exercies\schools.csv", encoding="utf8") as fin:
    reader = csv.reader(fin.readlines())
    lst = list(filter(scoli_gimnaziale, reader))
    # for row in reader:
    #     school = row[0].split(";")
    #     if "SCOALA GIMNAZIALA" in school[2] and "Comuna" in row[1]:
    #         lst.append(row)

with open(r"C:\Users\ravva\PycharmProjects\Homework\map_csv_exercies\secondary_schools.csv",
          "w", encoding="utf8", newline="") as fout:
    writer = csv.writer(fout)
    writer.writerows(lst)
# print(lst)
