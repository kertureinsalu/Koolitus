import Kõrvalfunktsioonid

sisestusInt1 = int(input("Sisesta esimene number"))
sisestusInt2 =int(input("Sisesta teine number"))
pakkumine = input("+ - * /")
if pakkumine == "+":
    Kõrvalfunktsioonid.liitmine(sisestusInt1, sisestusInt2)    
elif pakkumine == "-":
    Kõrvalfunktsioonid.lahutamine(sisestusInt1, sisestusInt2)
elif pakkumine == "*":
    Kõrvalfunktsioonid.korrutamine(sisestusInt1, sisestusInt2)
elif pakkumine == "/":
    Kõrvalfunktsioonid.jagamine(sisestusInt1, sisestusInt2)
else:
    print ("ei leidnud")
