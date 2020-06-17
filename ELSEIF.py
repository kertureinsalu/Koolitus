sisestus = input("Kas ruut või kolmnurk?")
if sisestus == "ruut":
    number = float(input("sisesta ruudu külg"))
    pindala = number**2
    print (pindala)
elif sisestus == "kolmnurk":
    number1 = float(input("sisesta kolmnurga esimene külg"))
    number2 = float(input("sisesta kolmnurga teine külg"))
    pindala = (number1*number2)/2
    print (pindala)
else:
    print ("kujundit pole olemas")
    