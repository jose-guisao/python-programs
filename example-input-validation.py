#This example do an input validation

print("How many dogs you have?")
numDogs = input()
if int(numDogs) < 0:
    print("You enter a negative number?... Try again...")
    exit()

try:
    if int(numDogs) >= 4:
        print("That is a lot of dogs.")
    else:
        print("That is not that many cats.")
except ValueError:
    print("You did not enter a number")
