import random

käigud = ["kivi", "paber", "käärid"]
game = True
while game == True:
    kasutaja = 3
    while kasutaja > 3 or kasutaja < 0:
        kasutaja = int(input("Kas kivi(0), käärid(1) või paber(2)?"))
    käik = käigud[kasutaja]
    kasutaja2 = käigud[random.randint(0, 2)]
    if (käik == "kivi" and kasutaja2 == "käärid") or (käik == "käärid" and kasutaja2 == "paber") or (käik == "paber" and kasutaja2 == "kivi"):
        print ("Mängija võitis")
    elif kasutaja == kasutaja2:
        print ("Viik")
    else:
        print ("Arvuti võitis")
    soov = input("Kas soovid uuesti (y/n)")
    if soov == "y":
        continue
    if soov == "n":
        game = False

