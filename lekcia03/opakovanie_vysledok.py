"""
OPAKOVANIE
        Uloha:
                urob vybuchujuci program.
                1.) Na zaciatku ta program privita
                2.) o 2 sekundy si od teba vypyta cislo, ktore predstavuje cas, za ktory ma vybuchnut bomba
                3.) Zacne odpocitavat... Ak si zadal napr. 5, bude kazdu sekundu odpocitavat 5, 4, 3,...
                4.) Ked sa odpocet dostane na nulu vykresli sa vybuch, ktory je napisany nizsie
                Bonus: urob bombu ktora sa moze pokazit. pravdepodobnost na pokazenie bude 1 ku 5, (pouzi import random)
"""
from time import sleep

print("Vybuchujuci program. Nastav si vlastnu bombu")
sleep(1)
while True:
    try:
        bomb_timer = int(input("Napis za kolko sekund ma vybuchnut bomba"))
    except ValueError:
        print("To co si zadal nie je cele cislo!!")
    else:
       break

for current_second in range(bomb_timer):
    sleep(1)
    print(bomb_timer - current_second)

#TOTO JE VYBUCH
sleep(1)
print("    ..-^~~~^-..  ")
print("  .~           ~. ")
print(" (;:           :;) ")
print("  (:           :)  ")
print("    ':._   _.:'  ")
print("        | |    ")
print("      (=====)  ")
print("        | |   ")
print("        | |  ")
print("        | |  ")
print("     ((/   \)) ")
print("BOOOOOOOOOOOOOOOOOOOM")
