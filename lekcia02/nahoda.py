from random import randint, shuffle, choice
print (randint(1, 10))
poradie = ["Andrej", "Beno", "Cyril", "Dano", "Emil", "Fero"]
shuffle(poradie)
for meno in poradie:
    print (meno)
print ("Toto je totalny blbec: ", choice(poradie))
