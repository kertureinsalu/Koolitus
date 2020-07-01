import random

avamine = open("Näitefail.txt", "w")

for x in range (10):
    avamine.write(str(random.randint(0, 10)) + "\n")
    
avamine.close()

nimekiri = []
avamine2 = open("Näitefail.txt", "r")
print (avamine2.readline())
for x in avamine2:
    print(x)
    x = x.strip()
    nimekiri.append(x)
avamine2.close()

print (nimekiri)