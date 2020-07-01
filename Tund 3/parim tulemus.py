sõnastik = {
    "Timo" : 65,
    "Karin" : 89,
    "Tanel" : 51,
    "Laura" : 98,
    "Katarina" : 77
    }

parimNimi = 0
parimTulemus = 0

for x, y in sõnastik.items():
    if y > parimTulemus:
        parimNimi = x
        parimTulemus = y
    else:
        continue
print ("Parim tulemus oli", parimNimi, "ja ta sai", parimTulemus, "punkti")
