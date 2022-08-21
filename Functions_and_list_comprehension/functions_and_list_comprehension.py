# Create a list with elements from 0 to 100 using list comprehension

my_list = [x for x in range(0, 101)]
print(my_list)

# Given the list  lst1=[1,2,3,4,5] create an identical list from the first list using list comprehension.

lst1 = [1, 2, 3, 4, 5]
lst2 = [x for x in lst1.copy()]
print(lst2)

# Given a list lst1=[2, 4, 6, 8, 10, 12, 14], using list comprehension, construct a new  list from the squares of
# each element in the list lst1.

lst3 = [2, 4, 6, 8, 10, 12, 14]
lst4 = [x ** 2 for x in lst3]
print(lst4)

# Given a list of numbers original_list = [2,3.75,.04,59.354,6,7.7777,8,9], create a new list without float numbers
# using list comprehension

original_list = [2, 3.75, 0.4, 59.354, 6, 7.7777, 8, 9]
lst = [int(x) for x in original_list]
print(lst)


# Create a function to reverse a my_string_vowels.

def revers_string(x):
    return x[::-1]


string = revers_string("nohtyP")
print(string)


# Create a function that accepts a my_string_vowels and calculate the number of upper case letters.

def upper_case_letters(x):
    y = 0
    for i in x:
        if i.isupper():
            y += 1
    return y


my_string = "Ana aRE mErE"

print(upper_case_letters(my_string))


# Create a function that squares up a list of numbers and returns the new list with the numbers squared

def square_my_list(x):
    return [i ** 2 for i in x]


my_list1 = [2, 3, 4, 5, 6]
square = square_my_list(my_list1)
print(square)
print(square_my_list(my_list1))


# Create a function that removes all vowels from a my_string_vowels given as argument and returns the new
# my_string_vowels.
# 1st.solution

def vowels_remove(string2):
    vowels = ["a", "e", "i", "o", "u"]
    result = [letter for letter in string2 if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)


my_string1 = "Ana are mere, Maria are BMW, nu plange Ana"
vowels_remove(my_string1)


# 2nd sollution

def vowels_remove(my_string_vowels):
    vowels = ["a", "e", "i", "o", "u"]
    result = [letter for letter in my_string_vowels if letter.lower() not in vowels]
    return ''.join(result)


my_string1 = "Ana are mere, Maria are BMW, nu plange Ana"
no_vowels = vowels_remove(my_string1)
print(no_vowels)
print(vowels_remove(my_string1))
