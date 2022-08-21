"""
In jungla:
Esti cu cortul in jungla singur si auzi niste animale in intuneric prin apropiere
Bazat pe sunet determina ce animale sunt
Task:
Ti se da sunetele facute de animalele din intuneric, evalueaza fiecare sunet
pentru a determina ce animal este:
Leii fac "Grr" , Tigri fac "Rawr", Serpii fac "Sss" iar pasarile fac "Cirip"

Input:
Un string ce reprezinta sunetele ce le auzi cu spatiu intre ele
Output:
Un string ce reprezinta animalele ce le auzi cu spatiu intre ele
(nota sunetele se pot repeta)

Ex:
Rawr Cirip Sss Sss
Tigru Pasare Sarpe Sarpe
"""

sunete_animale = {
    "Leu": "grr",
    "Tigru": "rawr",
    "Sarpe": "sss",
    "Pasare": "cirip"
}

user_input = input(
    "Va rog introduceti unul din urmatoarele sunete pentru a vedea ce animal este: grr,rawr,sss,cirip \n")

user_input_list = user_input.split(" ")
animale = ""
for sunet_input in user_input_list:
    for sound_key in sunete_animale:
        if sunete_animale[sound_key] == sunet_input:
            animale += sound_key + " "

print(animale)
