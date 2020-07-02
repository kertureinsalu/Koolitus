def sisestaja(sõna):
    nimekiri = []
    for x in sõna:
        nimekiri.append(x)
    return nimekiri

def tühiSisestaja(spikkerNimekiri):
    nimekiri = []
    for x in range(len(spikkerNimekiri)):
        nimekiri.append("_")
    return nimekiri

sõna = input("Sisesta sõna")
spikkerNimekiri = sisestaja(sõna)
tühiNimekiri = tühiSisestaja(spikkerNimekiri)

elu = 10
mäng = True
while mäng == True:
    print(tühiNimekiri)
    counter = 0
    täht = input("Paku täht")
    for y in spikkerNimekiri:
        if täht == y:
            tühiNimekiri[counter] = täht
        counter = counter + 1




