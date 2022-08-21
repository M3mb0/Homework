

def login(user, password):
    file = open('auth.txt', 'r')  # user,passwor
    for line in file:
        data = line.split(',')
        user_name = data[0]
        user_password = data[1]
        if user == user_name and password == user_password:
            file.close()
            return True
    file.close()
    return False

def must_login(is_user_loged_in):
    if is_user_loged_in:
        print("You are already logged in!")
        return True
    else:
        print("You need to log in!")
        user_name = input('Please insert username: ')
        user_password = input('Please insert password: ')
        if login(user_name, user_password):
            print("User has logged in!")
            return True
        else:
            print("Try again, username/password incorrect!")
            return False

def logout(is_user_loged_in):
    if is_user_loged_in:
        print("You have been logged out!")
        return False