"""A text module who prints the menu and intro and contains 3 functions

Function:
----------
    menu:
        prints the help command
    intro:
        prints the intro message
    clear_screen:
        clears the screen in the terminal after each step

Other imports:
----------
    time:
        used in clear_screen function to clear the screen with a delay
    os:
        used in clear_screen function to clear the screen
"""

import os
import time


def menu():
    """Function takes no arguments and prints the command panel"""
    print("""\n\tHELP PANEL

    Please use the following commands:
    
    add_complaint - use this command for adding a complaint (requires name and the complaint)
    solve_complaint - use this command for changing complaint status in solved (requires the id)
    select_complaint_by_status  - use this command for searching the solved or unresolved complaints
                                  (requires to enter 1 or 0. 
                                  0 = not solved 1 = solved)
    select_all - use this command for displaying all complaints
    exit - use this command to exit\n""")


def intro():
    """Function takes no arguments and prints the intro message and takes no arguments"""
    print("""\n\tWelcome to our COMPLAINT BOOKLET.
    
    For start working please enter your command
    For seeing the commands please type: help
    To exit please type: exit\n""")


def clear_screen():
    """Clears the screen when is called with a delay of 1 second and takes no arguments"""
    time.sleep(1)
    os.system('cls')
