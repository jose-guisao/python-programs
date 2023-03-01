#Esta funcion no prueba si el numero n es mayor que cero

def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)

#Esta version hace la prueba del numero n es mayor que 0
def countdown2(n):
  print(n)
  if n > 0:
    countdown2(n - 1)
  return

#Esta es otra forma de hacer el codigo

def countdown3(n):
  while n >= 0:
    print(n)
    n -= 1

#Funcion para n factorial

def factorial(n):
  print(f"factorial() called with n = {n}")
  return_value = 1 if n <= 1 else n * factorial(n - 1)
  print(f"-> factorial({n}) return {return_value}")
  return return_value

#Ejmplo de funcion primera clase

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))

print(greet_bob(be_awesome))
##n = int(input('Enter a number greater than zero :'))
##countdown3(n)
##factorial(n)
