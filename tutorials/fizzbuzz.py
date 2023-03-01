# https://blog.codinghorror.com/why-cant-programmers-program/
# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

print('FizzBuzz', '\n')
for i in range(1, 100):
    if (i % 3) == 0:
        if (i % 15) == 0:
            print('FizzBuzz')
            continue
        print('Fizz')
        continue
    else:
        if (i % 5) == 0:
            print('Buzz')
            continue
        else:
            if (i % 15) == 0:
                print('FizzBuzz')
                continue
    print(i)
print('\n', 'end')

# Otro ejercicio, N factorial


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


print('N factorial')
print(factorial(5))
print(factorial(1))
print(factorial(23))
print('end')
