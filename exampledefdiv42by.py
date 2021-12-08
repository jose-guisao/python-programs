#This example use try/except to catch an error

def div42by_err(divideby):
    return 42 / divideby

def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('Error: You try to divide by zero')


for i in range(-2,5):
    print(div42by(i))

[print(div42by(i)) for i in range(-2,3)]


