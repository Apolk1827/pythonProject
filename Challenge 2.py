tips = int(input("How much would you like to tip?"))
total = 0
bigtip = 0
while tips != 0:
    total = total + tips
    if tips > bigtip:
        bigtip = tips
    tips = int(input("Enter tip here."))
total = total * 0.01
print("Total tips: ${}" .format(total))
print("Your largest tip was {}!" .format(bigtip))
