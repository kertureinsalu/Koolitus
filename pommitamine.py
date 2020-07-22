ruudustik1 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik2 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik3 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik4 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik5 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik6 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik7 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik8 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik9 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik10 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}

väljakKogu1 = {
    "0" : ruudustik1,
    "1" : ruudustik2,
    "2" : ruudustik3,
    "3" : ruudustik4,
    "4" : ruudustik5,
    "5" : ruudustik6,
    "6" : ruudustik7,
    "7" : ruudustik8,
    "8" : ruudustik9,
    "9" : ruudustik10
}

ruudustik11 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik12 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik13 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik14 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik15 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik16 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik17 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik18 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik19 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}
ruudustik20 = {"1" : " ", "2" : " ", "3" : " ", "4" : " ", "5" : " ", "6" : " ", "7" : " ", "8" : " ", "9" : " ", "10" : " "}

väljakKogu2 = {
    "0" : ruudustik11,
    "1" : ruudustik12,
    "2" : ruudustik13,
    "3" : ruudustik14,
    "4" : ruudustik15,
    "5" : ruudustik16,
    "6" : ruudustik17,
    "7" : ruudustik18,
    "8" : ruudustik19,
    "9" : ruudustik20
}
legend1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
legend2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def printVäljak1(väljakKogu1):
    print (" ", end= "|")
    for x in range (len(legend1)):
        print (legend1[x], end= "|")
    print ("")
    counter = 0
    for x in väljakKogu1.values():
        print ("-"*22)
        print (legend2[counter], end= "")
        print ("", end= "|")
        for y in x.values():
            print (y, end= "|")
        print("")
        counter += 1

def printVäljak2(väljakKogu2):
    print (" ", end= "|")
    for x in range (len(legend1)):
        print (legend1[x], end= "|")
    print ("")
    counter = 0
    for x in väljakKogu2.values():
        print ("-"*22)
        print (legend2[counter], end= "")
        print ("", end= "|")
        for y in x.values():
            print (y, end= "|")
        print("")
        counter += 1

def laevadePaigutamine1(väljakKogu1):
    print ("Paiguta ühene laev")
    rida = input("Vali rida")
    asukoht = input("Vali asukoht")
    väljakKogu1[rida] = asukoht
    printVäljak1(väljakKogu1)
    return laevadePaigutamine1(väljakKogu1)

print ("Tere tulemast laevadepommitamise mängu.")
print ("Igal mängijal on kokku kümme laeva.")
print ("Neli ühe ruudulist laeva, kolm kaheruudulist laeva, kaks kolmeruudulist laeva ja üks neljaruuduline laev.")
print ("Laevade paigutamine toimub suurimaist väiksemateni sinu valitud ruutudele.")
print ("\n")
print ("Mängija 1")
printVäljak1(väljakKogu1)
print ("\n")
print ("Mängija 2")
printVäljak2(väljakKogu2)

laevadePaigutamine1(väljakKogu1)

 

