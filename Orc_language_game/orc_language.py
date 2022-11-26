"""
Ai 2 prieteni ce vorbesc orca intre ei.Limba orca sunt aceleasi cuvinte
ca in limba romana doar ca se ia prima litera a fiecarui cuvant si se pune
la sfarsitul cuvantului in urma caruia se adauga un ay
drum = rumday
Input:
Un string ce reprezinta o propozite in limba romana
Output:
Un string ce reprezinta traducerea in limba orca
"""


def translator():
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'n', 'y', 'z']
    my_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    list_limba_orca = []
    limba_romana = input("")
    list_limba_romana = limba_romana.split(" ")
    for cuvant in list_limba_romana:
        if len(cuvant) == 1:
            cuvant_tradus = cuvant + "ay"
            list_limba_orca.append(cuvant_tradus)
        elif cuvant[-1] in alfabet:
            if cuvant[0] == cuvant[0].upper():
                cuvant_tradus = cuvant[1].upper() + cuvant[2:] + cuvant[0].lower() + "ay"
                list_limba_orca.append(cuvant_tradus)
            else:
                cuvant_tradus = cuvant[1:] + cuvant[0] + "ay"
                list_limba_orca.append(cuvant_tradus)
        elif cuvant[-1] in my_numbers:
            list_limba_orca.append(cuvant)
        else:
            if cuvant[0] == cuvant[0].upper():
                cuvant_tradus = cuvant[1].upper() + cuvant[2:len(cuvant) - 1] + cuvant[0].lower() + "ay" + cuvant[-1]
                list_limba_orca.append(cuvant_tradus)
            else:
                cuvant_tradus = cuvant[1:len(cuvant) - 1] + cuvant[0] + "ay" + cuvant[-1]
                list_limba_orca.append(cuvant_tradus)
    limba_orca = ""
    for cuvant in list_limba_orca:
        limba_orca += cuvant + " "
    return limba_orca


while True:
    try:
        print(translator())
    except IndexError:
        print("Va rog sa nu introduceti mai mult de un spatiu intre cuvinte!")
