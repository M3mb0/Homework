# Write a program that finds and prints the largest number from a list of lists

list1 = []


def largest_number(my_list_of_lists):
    for number in my_list_of_lists:
        if type(number) == list:
            largest_number(number)
        else:
            list1.append(number)
    return max(list1)


list_of_lists = [[23, 44], 65, [49, 89], 38, [34, 55]]

print(largest_number(list_of_lists))

# Write a program that will compute the factorial of a number imputed by the user (using for loops)

num = int(input("Introduceti numarul: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(factorial)

# Finding the sum of numbers in a list using for loop

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
suma = 0

for i in my_list:
    suma += i
print(suma)

# Get all values from the dictionary and add them to a list but don’t add duplicate (use for loops and do it without
# for loops)

data = {
    'jan': 47,
    'feb': 52,
    'march': 47,
    'April': 44,
    'May': 52,
    'June': 53,
    'july': 54,
    'Aug': 44,
    'Sept': 54
}

my_list = []
for item in data.values():
    print(item)
    my_list.append(item)
my_list = list(set(my_list))
print(my_list)
