#List Comprehension
remainder5 = [x**2 % 5 for x in range(1, 101)]

print(remainder5)

newList = set(remainder5)
print()
print(newList)

remainder11 = [x**2 % 11 for x in range(1, 101)]

newList = set(remainder11)
print()
print(remainder11)

print(newList)