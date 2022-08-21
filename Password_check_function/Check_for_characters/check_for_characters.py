from characters import *

def check_numbers(password):
    for element in password:
        if element in numbers:
            return True
    else:
        print("Number is missing!")


def check_alfabet(password):
    for element in password:
        if element in alphabet:
            return True
    else:
        print("Letter is missing!")


def check_special_characters(password):
    for element in password:
        if element in special_characters:
            return True
    else:
        print("Special character is missing!")


def check_if_upper(password):
    for element in password:
        if element.isupper():
            return True
    else:
        print("One upper case is required!")


def check_length(password):
    if len(password) >= 8:
        return True
    else:
        print("Password must have at least 8 elements!")