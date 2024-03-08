age = 913
print("How old do you think Yoda is?")
guess = int(input("Your guess: "))
guesses = 1

while guess != age:
    if guess < age:
        print("Higher!")
    elif guess > age:
        print("Lower!")
    guess = int(input("Your guess: "))
    guesses = guesses + 1
    if guesses <= 7:
        print("you suck")
print("Correct! You got it right in {} guesses!" .format(guesses))