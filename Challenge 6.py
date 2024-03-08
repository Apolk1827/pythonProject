print("How much do you want to invest?")
totalI = int(input("Amount of money: "))
total = totalI
total = total + .06 * total
years = 1
while total < totalI * 2:
    if total == totalI * 2:
        print("It took () years.".format(years))
    elif total < totalI * 2:
        total = total + .06 * total
        years = years + 1
        print("Your total as of this year is (), it has been () years.".format(total, years))
