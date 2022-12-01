from data_base import Database
from main_menu import menu, intro

my_db = Database()

while True:
    intro()
    user_input = input("Please enter your command:")
    if user_input == "help":
        menu()
    elif user_input == "add_complaint":
        name = input("Hello. Please enter your name: ")
        complaint = input("Please describe your issue: ")
        my_db.add_complaint(name, complaint)
    elif user_input == "select_complaint":
        while True:
            try:
                user_id = int(input("Please enter the id: "))
                my_db.select_compliant(user_id)
            except ValueError as err:
                print(err)
    elif user_input == "modify_status":
        while True:
            try:
                user_id = int(input("Please enter the id: "))
                my_db.modify_status_solved(user_id)
            except ValueError as err:
                print(err)
    elif user_input == "select_complaint_by_status":
        while True:
            try:
                my_status = int(input("Please enter the status: "))
                if my_status in [0, 1]:
                    my_db.select_complaint_by_status(my_status)
                    break
                else:
                    print("Status must be 0 or 1!")
            except ValueError as err:
                print(err)
    elif user_input == "select_all":
        my_db.select_all_complaints()
    elif user_input == "exit":
        print("Goodbye!")
        break
    else:
        print("Incorrect command. Please use 'help' to see the available commands")
