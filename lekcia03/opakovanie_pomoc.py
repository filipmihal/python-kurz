# napiseme ktory subur chceme otvorit, r znamena read teda chcem subor citat
file = open('ascii_art.txt', 'r')
# precitame obsah suboru
obrazok = file.read()
# vypiseme obsah suboru
print (obrazok)