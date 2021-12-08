# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name +', Iam thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)
# print(secretNumber)
for guessesTaken in range(1, 7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your number is too low.")
    elif guess > secretNumber:
        print('Your guess is to high.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guess my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))



