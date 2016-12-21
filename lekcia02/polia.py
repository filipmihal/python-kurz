#urobenie si zoznamu
import time
zoznam = ["pes", "macka", "fero", "opica", "zajac"]
cislo = 0
#kym je cislo mensie ako 5
while cislo < 5:
    print(zoznam[1])
    time.sleep(2)
    cislo += 1
print(zoznam[1:3])
hrdinovia = ["Indiana Jones", "Spiderman", "Captain America", "Hulk",
"Iron Man", "Thor"]

print(hrdinovia[0], " je maxi hrdina!")

for chlap in hrdinovia:
	print(chlap," je hrdina!")


