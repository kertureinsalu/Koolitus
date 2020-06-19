sisestus = input("Kas ruut või kolmnurk?")
kontroll = True
while kontroll == True:
    if sisestus == "ruut":
        number = int(input("Sisesta ruudu külg"))
        pindala = number**2
        print (pindala)
        kontroll = False
    elif sisestus == "kolmnurk":
        number1 = int(input("Sisesta kolmnurga esimene külg"))
        number2 = int(input("Sisesta kolmnurga teine külg"))
        pindala = (number1*number2)/2
        print (pindala)
        kontroll = False
    else:
        sisestus = input("Kas ruut või kolmnurk?")
        kontroll = True
