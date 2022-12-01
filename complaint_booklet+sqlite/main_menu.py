

def menu():
    print("""HELP PANEL

    Please use the following commands:
    
    add_complaint - use this command for adding a complaint (requires name and the complaint)
    select_complaint - use this command for searching a complaint by id (requires the id)
    modify_status - use this command for changing complaint status in solved (requires the id)
    select_complaint_by_status  - use this command for searching the solved or unresolved complaints
                                  (requires to enter 1 or 0. 
                                  0 = not solved 1 = solved)
    select_all - use this command for displaying all complaints
    exit - use this command to exit""")


def intro():
    print("""Welcome to our COMPLAINT BOOKLET.
    
    For start working please enter your command
    For seeing the commands please type: help
    To exit please type: exit""")
