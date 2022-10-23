import random
from itertools import combinations
from collections import Counter


def cool_sequence():
    while True:
        try:
            user = int(input('Please enter the length of the list numbers: '))
            user_sequence = int(input('Please enter the length of the sequence you want to check: '))
            if user_sequence <= user:
                list_of_numbers = [random.randrange(1, 9) for _ in range(user)]
                print(list_of_numbers)
                list_combinations(list_of_numbers, user_sequence)
                print('-' * 40 + 'Version 2' + '-' * 40)
                cool(list_of_numbers, user_sequence)
                break
            else:
                print('The sequence needs to be smaller or equal with the length of the list')
                continue
        except ValueError:
            print('Please enter numbers only')


def list_combinations(my_list, user):
    lst = []
    my_comb = combinations(my_list, user)
    for lists in list(my_comb):
        if sorted(lists) == list(range(min(lists), max(lists) + 1)):
            x = max(lists)
            lst.append(x)
    if len(lst) > 0:
        print(f'It\'s a cool sequence and the biggest number is {max(lst)}')
    else:
        not_cool(my_list)


def not_cool(my_list):
    distinct_elements = [no for no, counter in Counter(my_list).items() if counter == 1]
    print(f'Is not a cool sequence and the number of distinct elements is {len(distinct_elements)}')


def cool(my_list, user):
    lst = [my_list[0:user]]
    for i in lst:
        if sorted(i) == list(range(min(i), max(i) + 1)):
            print(f'This is a cool sequences and the biggest number is {max(i)}')
        else:
            not_cool(i)
