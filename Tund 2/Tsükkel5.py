import random
nimi = input("Sisesta oma nimi")
nimekiri = []
punktid = 0
kontroll = True
while kontroll == True:
    punktid = 0
    for x in range (1):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        tehe = x*y
        print (x, "*", y)
        sisestus = int(input("Vastus"))
        if sisestus == tehe:
            punktid = punktid + 1
            print ("Õige vastus!")
        else:
            print ("Vale vastus!")
    sisestus = input("Uuesti jah/ei")
    nimekiri.append(punktid)
    if sisestus == "jah":
        continue
    else:
        kontroll = False
print (nimi, "Sinu punktide tulemus on", nimekiri)
