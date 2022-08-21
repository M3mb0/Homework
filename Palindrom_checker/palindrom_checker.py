user_input = input("Enter the word: ")

my_palindrome = ""
how_many_times_each_letter_is_repeating = {}
odd_list = []
even_list = []


def check_elements(my_string):
    if not my_string.isalpha():
        print("Only letters are allowed")
        return False
    elif not my_string.islower():
        print("Only lower case letters are allowed")
        return False
    return True


def check_for_palindrome(my_string):
    for letter in my_string:
        if letter not in how_many_times_each_letter_is_repeating:
            how_many_times_each_letter_is_repeating[letter] = 1
        else:
            how_many_times_each_letter_is_repeating[letter] += 1

    for key, value in how_many_times_each_letter_is_repeating.items():
        if value % 2 == 0:
            even_list.append(key * (value // 2))
        else:
            odd_list.append(key * value)


def print_palindrome():
    global my_palindrome
    for element in range(0, len(even_list)):
        if len(even_list) == 1 and len(odd_list) <= 1:
            my_palindrome = even_list[element] + odd_list[element] + even_list[element]
            print("Yes")
            print(f'The palindrome is: {my_palindrome}')
        elif len(even_list) >= 2 and len(odd_list) <= 1:
            my_palindrome_list = even_list[0::] + odd_list[0::] + even_list[::-1]
            my_palindrome = ''.join(my_palindrome_list)
            print("Yes")
            print(f'The palindrome is: {my_palindrome}')
            break


while not check_elements(user_input):
    break
else:
    check_for_palindrome(user_input)
    if len(odd_list) >= 2:
        print("No")
    else:
        print_palindrome()
