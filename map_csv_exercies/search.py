"""display the addresses that host more than 3 institutions and the names of the hosted institutions."""

import csv
from collections import Counter

institution = []
address = []

with open("lista_ep_portal_01102022.csv", encoding="utf8") as f:
    reader = csv.reader(f.readlines(), delimiter=";")
    for line in reader:
        institution.append(line[2])
        address.append(str(line[4].split(",")[0:4]))

repeated_address = [item for item, count in Counter(address).items() if count > 2]

for item in repeated_address:
    print(item)
    for element in address:
        if element == item:
            print(institution[address.index(element)])
            address[address.index(element)] = ""
