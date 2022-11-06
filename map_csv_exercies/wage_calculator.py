"""Printing a list of wages from a csv f and calculate the NET income"""

import csv


def calculate_net_wage(income):
    """Calculate the NET income"""

    return income - (income * 45) / 100


list_of_wages = []
list_of_net_wages = []
with open(r"C:\Users\ravva\PycharmProjects\Homework\map_csv_exercies\employee.csv") as fin:
    reader = csv.reader(fin.readlines())
    for wage in reader:
        list_of_wages.append(int(wage[3]))
        net_wage = calculate_net_wage(int(wage[3]))
        list_of_net_wages.append(net_wage)

net_wage = map(calculate_net_wage, list_of_wages)
print(list(net_wage))
print(f"The biggest brut income is {max(list_of_wages)} and the smallest brut income is {min(list_of_wages)}.\n"
      f"The biggest net income is {max(list_of_net_wages)} and the smallest net income is {min(list_of_net_wages)}")

# same as net wage but instead of the function we use lambda
net = map(lambda income: income - (income * 45) / 100, list_of_wages)
print(list(net))
