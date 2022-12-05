"""The main script which is reading , inserting and modifies the data from the table created with the help
 of Database class"""


import sqlite3
from datetime import datetime

from data_base import Database
from main_menu import menu, intro, clear_screen

my_db = Database()

while True:
    intro()
    user_input = input("Please enter your command:")
    if user_input == "help":
        clear_screen()
        menu()
    elif user_input == "add_complaint":
        while True:
            try:
                clear_screen()
                name = input("Hello. Please enter your name: ")
                email = input("Please enter your email: ")
                complaint = input("Please describe your issue: ")
                date = str(datetime.now().strftime("%Y-%b-%d %H:%M"))
                my_db.add_complaint(name, email, complaint, date)
                break
            except sqlite3.IntegrityError as err:
                print(err)
    elif user_input == "solve_complaint":
        while True:
            try:
                clear_screen()
                user_id = int(input("Please enter the id: "))
                my_db.solve_complaint(user_id)
                break
            except ValueError as err:
                print(err)
    elif user_input == "select_complaint_by_status":
        while True:
            try:
                clear_screen()
                my_status = int(input("Please enter the status: "))
                if my_status in [0, 1]:
                    my_db.select_complaint_by_status(my_status)
                    break
                else:
                    print("Status must be 0 or 1!")
            except ValueError as err:
                print(err)
    elif user_input == "select_all":
        clear_screen()
        my_db.select_all_complaints()
    elif user_input == "exit":
        clear_screen()
        print("Goodbye!")
        break
    else:
        clear_screen()
        print("Incorrect command. Please use 'help' to see the available commands")
