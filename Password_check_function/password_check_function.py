from check_for_characters import *

user_input = input("Passowrd: ")
user_password = list(user_input)


def check_password(password):
    if all([check_numbers(password), check_alfabet(password), check_special_characters(password),
            check_if_upper(password), check_length(password)]):
        print("Correct!")
    else:
        print("Incorrect password!")


check_password(user_input)
