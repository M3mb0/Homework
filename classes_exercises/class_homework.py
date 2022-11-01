from datetime import datetime


"""
 Scrie o clasa care repr. o Agenda (Notebook).
Atribute:
    - nr pagini (la contructor)
    - culoare (la constructor)
    - continut - lista de stringuri ["continut pagina", "continut pag."]

Metode:
    - scrie in Agenda
    - vezi nr de pag goale
    - vezi nr pag scrise
"""


class Notebook:
    """Notebook class keep track of your input and take 2 arguments"""

    def __init__(self, no_of_pages, color):
        self.no_of_pages = no_of_pages
        self.color = color
        self.content = []

    def write(self):
        """write method is used to write data in your agenda"""
        user = input('Enter the content: ')
        return self.content.append(user)

    def no_of_writen_pages(self):
        """this method is returning the number of writen pages"""
        if len(self.content) % 3 == 0:
            writen_pag = int(len(self.content) / 3)
        elif len(self.content) == 0:
            writen_pag = 0
        else:
            writen_pag = int(len(self.content) / 3) + 1
        return writen_pag

    def no_of_empty_pages(self):
        """this method is returning the number of empty pages"""
        empty_pages = self.no_of_pages - self.no_of_writen_pages()
        return empty_pages


# my_agenda = Notebook(3, 'red')
# COUNT = 1
# while COUNT < 7:
#     my_agenda.write()
#     COUNT += 1
#     if my_agenda.no_of_writen_pages() > my_agenda.no_of_pages:
#         break
# print(my_agenda.content)
# print(f'The number of writen pages is {my_agenda.no_of_writen_pages()}')
# print(f'The number of empty pages is {my_agenda.no_of_empty_pages()}')

"""
Scrie o clasa care repr. un Utilizator
Atr:
 - nume (c)
 - prenume(c)
 - telefon(c)
 - email(c)
 - activ - bool

Meth:
 - activate
 - deactivate
 - update_email - 1 param
 - update_phone - 1 param
 - print_user_info
 """


class User:
    """User class define a user and taking 4 arguments"""

    def __init__(self, name, first_name, phone_no, email):
        self.name = name
        self.first_name = first_name
        self.phone_no = phone_no
        self.email = email
        self.active = True

    def activate(self):
        """Activate the user"""
        self.active = True

    def deactivate(self):
        """Deactivate the user"""
        self.active = False

    def update_email(self, user):
        """Change email address"""
        if self.active:
            self.email = user + "@domain.com"

    def update_phone_no(self, user):
        """Change phone number"""
        if self.active:
            self.phone_no = user

    def print_user_info(self):
        """Print the user info"""
        if self.active:
            print(f"""Your info are:
    Name: {self.name}
    First name: {self.first_name}
    Phone number: {self.phone_no}
    Email: {self.email}
    """)
        else:
            print("Your account has been deactivated")


my_user = User("Cristian", "Ungureanu", "0777666555", "cristian@domain.com")
my_user.activate()
# my_user.print_user_info()
# my_user.update_email("ungureanu")
# my_user.update_phone_no("0799888777")
# my_user.print_user_info()
# my_user.deactivate()
# my_user.print_user_info()


"""3. Scrie o clasa UserManger
Atr:
 - users = lista de utilizatori activi
 Meth:
  - add_user(User)
  - get_user_by_email
  - remove_user
  - drop_all
  - create_default_user
"""


class UserManager:
    """UserManager class is used to add, remove or creating a default user"""

    def __init__(self):
        self.user_list = []

    def add_user(self, user):
        """Add the user to the list"""
        if user.active is True:
            self.user_list.append(user)

    def get_user_by_email(self):
        """Search for user by email and remove the user from the list if you want"""
        user_input = input("Please enter the email address of the user you are looking for: ")
        for user in self.user_list:
            if user.email == user_input:
                print(f"User found and his name is {user.name}.")
                us_input = input('If you want to remove the user press -r- '
                                 'if you press any other key the user will not be removed\n')
                if us_input == 'r':
                    self.remove_user(user)
            else:
                print("User not found")

    def remove_user(self, user):
        """Remove a certain object user"""
        return self.user_list.remove(user)

    def drop_all(self):
        """Clear the entire list"""
        return self.user_list.clear()

    @staticmethod
    def create_default_user():
        """Create a default user"""
        return User("User", "Name", "0700000000", "email@domain.com")


manager = UserManager()
manager.add_user(my_user)
manager.get_user_by_email()
print(len(manager.user_list))
manager.add_user(UserManager.create_default_user())
print(len(manager.user_list))
manager.get_user_by_email()
print(len(manager.user_list))
manager.drop_all()
print(len(manager.user_list))


"""
4. Scrie o clasa ce repr. o cursa aeriana
Atr:
 - aeroport_plecare  (c)
 - aeroport_sosire (c)
 - data_ora_plecare (c)
 - data_ora_sosire (c)
 - pret_per_loc (c)
Meth:
 - get_duration
 - get_price_tva (pret_per_loc + tva)
"""


class AirplaneTrip:
    """AirplaneTrip class returns the time you have to travel and the price of the trip
    and is taking 5 arguments"""

    def __init__(self, departure, arrival, departure_date_hour, arrival_date_hour, price):
        self.departure = departure
        self.arrival = arrival
        self.departure_date_hour = departure_date_hour
        self.arrival_date_hour = arrival_date_hour
        self.price = price

    def get_duration(self):
        """Return the duration of the trip"""
        return divmod((self.arrival_date_hour - self.departure_date_hour).total_seconds() / 60, 60)

    def get_price_tva(self):
        """Return the price of the trip ith TVA included"""
        return self.price + (self.price * 19) / 100


trip = AirplaneTrip("Romania", "United Kingdom", datetime(2022, 11, 1, 15, 30),
                    datetime(2022, 11, 1, 18, 45), 400)
# print(trip.get_duration())
# print(trip.get_price_tva())


"""
5. Scrie o clasa ce repr. un Bilet de avion
Atr:
 - nume posesor (c)
 - cursa -> de tip cursa aeriana definita mai sus (c)
 - loc (c)

Meth:
 - print_ticket -> printeaza info despre cursa si loc (nume, durata, pret, loc)
"""


class AirplaneTicket:
    """AirplaneTicket class defines a ticket and is taking 4 arguments"""

    def __init__(self, name, type_of_trip, seat, my_trip):
        self.name = name
        self.type_of_trip = type_of_trip
        self.seat = seat
        self.trip = my_trip

    def print_ticket(self):
        """Prints the user ticket and takes one argument"""
        print(f"Hello {self.name}.\nYour trip from {self.trip.departure} to {self.trip.arrival} "
              f"will depart at "
              f"{self.trip.departure_date_hour} and you will arrive on {self.trip.arrival_date_hour}.\n"
              f"The {self.type_of_trip} costs {self.trip.get_price_tva()} RON and it will last for "
              f"{int(self.trip.get_duration()[0])} hours and {int(self.trip.get_duration()[1])} minutes\n"
              f"Your seat is {self.seat}")


ticket = AirplaneTicket("Cristi", "airplane", "C3", trip)
ticket.print_ticket()
