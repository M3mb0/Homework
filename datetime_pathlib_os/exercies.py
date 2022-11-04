"""Scrie o functie care afiseaza un mesaj de salut. Mesajul de salut trebuie sa contina numele utilzatorului
curent (se obtine cu modulul os) si cati GB (cu doua zecimale) ocupa directorul home.
Ex: Salut mdinu! Spatiu utilizat de tine: 4.55 GB"""

import os
from pathlib import Path
from datetime import datetime


def hello():
    """Returns the `directory` size in gigabytes."""

    user_root = Path.home()
    size = 0
    for path in user_root.glob("**/*"):
        size += path.stat().st_size

    print(f"Hi {os.getlogin()}! Home directory occupies: {round(size / 10 ** 9, 2)} GB.")


hello()


"""Afiseaza cate ore au trecut din acest an."""

beginning_of_the_year = datetime(2022, 1, 1)
today = datetime.now()

hours_past = divmod((today - beginning_of_the_year).total_seconds() / 60, 60)[0]
print(f"From this year has past {hours_past} hours")


"""Afiseaza cate zile au trecut de la nasterea ta."""

my_birthday = datetime(1986, 6, 6, 3)
days_past = divmod((today - my_birthday).total_seconds() / 3600, 24)[0]
print(f"From my birthday has past {days_past} days")
