# Print "Salutare" 5 times using while loops

x = 0

while x < 5:
    print("Salutare")
    x += 1

# Print every letter from the my_string_vowels "Hello" on a new income except for "e" and "o" using wille loops.

my_string = "Helloaeorroem"
x = 0

while x < len(my_string):
    if my_string[x] == "e" or my_string[x] == "o":
        x += 1
        continue
    print(my_string[x])
    x += 1

# Print the letters from the my_string_vowels "Hello" on a new income until we find the letter "l" then stop printing

my_string = "Hello"
x = 0

while x < len(my_string):
    if my_string[x] == "l":
        break
    else:
        print(my_string[x])
        x += 1

# Retrive from the user using the input() method 5 numbers and print the average.


my_list = []
X = 0

while x <= 4:
    userinput = int(input("Enter a number: "))
    my_list.append(userinput)
    print(my_list)
    x += 1

avg = sum(my_list) / len(my_list)
print("Average: ", avg)

# Pop all elements from the list fruitlist = ["MAngo", "Apple", "Orange", "Guava"] using while loop

fruitlist = ["Mango", "Apple", "Orange", "Guava"]

x = 0

while x < len(fruitlist):
    pop_fruits = fruitlist.pop()
    print(fruitlist)
    print(pop_fruits)
x += 1

# Printing the ele in a tuple using while loop

my_tuple = ("Fruits", "Vegetables", "Healt", "Happiness")
x = 0
while x < len(my_tuple):
    print(my_tuple[x])
    print(type(my_tuple))
    x += 1

# Write a program that will tell if a dictionary is empty or not

my_dict = {
    "Sport": "Football",
    "Hobby": "Travel"
}

x = 0

if len(my_dict) > x:
    print(my_dict)
else:
    print("Dictionary is empty")


# Write a program that will compute the factorial of a number imputed by the user(using while loops)

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


my_number = int(input("Enter a number: "))
print(factorial(my_number))

# The user will input 5 numbers (one at a time) print the min and the max values:

my_list = []
x = 0

while x <= 4:
    userinput = int(input("Enter your number: "))
    my_list.append(userinput)
    print(my_list)
    x += 1

print("The bigest numeber is: ", max(my_list))
print("The smallest number is: ", min(my_list))

# Finding the sum of numbers in a list using while loop

user_input = int(input("Enter a number: "))
if user_input < 0:
    print("Enter a positive number")
else:
    my_sum = 0
    while user_input > 0:
        my_sum += user_input
        user_input -= 1
    print("The result is", [my_sum])
    print(type([my_sum]))
