"""
Esti pe un vas de croaziera care ancoreaza langa o plaja superba.Exita o barcuta
mica ce va duce pasageri pe plaja.Te pui la rand .
Cat timp trebuie sa astepti stiind ca pe barcuta intra 20 de oameni iar un drum dureaza 10 minute.
Task:
Determina timpul de astptare daca stii numarul de persoane in fata ta
Input :
un numar intreg ce reprezinta numarul total de perosane aflate in fata ta
Output:
un numar intreg ce reprezinta numarul de minute ce trebuie sa astepti
ex:
Input:25
Ouptut:10
"""

while True:
    try:
        no_of_riders = int(input("How many riders are waiting to cross in front of me? "))
    except ValueError:
        print("ERROR!!!Please enter numbers only!")
    else:
        one_way = 10
        one_trip = one_way * 2
        max_riders = 20
        if no_of_riders <= max_riders:
            print(f"You can board")
        else:
            print(f"You have to wait {one_trip * int((no_of_riders / max_riders))} min")