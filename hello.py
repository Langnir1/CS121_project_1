import random

x = random.randint(1, 100)
keepGoing = True

print("hello world")

name = input("What is your name?: ")
print(f"Good day {name}! I hope your day, nay, your week is of the utmost smooth sailing.")

question = input("Want to play a quick game? (please input either 'yes' or 'no' ) ") 

if question == "yes":
    while (keepGoing):
        guess = input("Take a guess from 1 to 100: ")
        guess = int(guess)
        if guess == x:
            print("Conragulations you win!")
            keepGoing = False
        if guess > x:
            print("Your guess is too high, try again!")
        if guess < x:
            print("Your guess is too low, try again!")

elif question == "no":
    print("Fair enough. Fare thee well!")
else:
    print("I'll take that as a no?")
