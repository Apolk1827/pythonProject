import random
name = (input("What is your name?"))
compliments = random.randint(1, 5)
answer = "no"
while answer != "yes":
    if compliments == 1:
        print("I believe in you, {}!".format(name))
        answer = (input("Are you ready?"))
        if answer != "yes":
            compliments = random.randint(1, 5)
        if answer == "yes":
            print("Great! Get out there!")
    elif compliments == 2:
        print("You got this, {}!".format(name))
        answer = (input("Are you ready?"))
        if answer != "yes":
            compliments = random.randint(1, 5)
        if answer == "yes":
            print("Great! Get out there!")
    elif compliments == 3:
        print("omg slay, {}!!!!!!!!!!".format(name))
        answer = (input("Are you ready?"))
        if answer != "yes":
            compliments = random.randint(1, 5)
        if answer == "yes":
            print("Great! Get out there!")
    elif compliments == 4:
        print("Keep it up, {}!".format(name))
        answer = (input("Are you ready"))
        if answer != "yes":
            compliments = random.randint(1, 5)
        if answer == "yes":
            print("Great! Get out there!")
    elif compliments == 5:
        print("You are amazing, {}!".format(name))
        answer = (input("Are you ready?"))
        if answer != "yes":
            compliments = random.randint(1, 5)
        if answer == "yes":
            print("Great! Get out there!")
