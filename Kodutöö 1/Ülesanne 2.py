import random

nimekiri = []
counter = 1000
while counter > 0:
    nimekiri.append(random.randint(0, 100))
    counter = counter - 1

miinimum = 0
loendur = 0
for number in nimekiri:
    if number <= miinimum:
        if number == miinimum:
            loendur = loendur + 1
        else:
            loendur = 1
            miinimum = number
    else:
        continue
print ("Väikseim number on", miinimum, "ja seda esines", loendur, "korda.")