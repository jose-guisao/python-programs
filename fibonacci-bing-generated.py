#Programa Python para generar la serie Fibonacci hasta el valor 'n'
n = int(input("Introduce el valor de 'n': "))
a = 0
b = 1
suma = 0
contador = 1
print("Serie Fibonacci: ", end = " ")
while (contador <= n):
  print(suma, end = " ")
  contador += 1
  a = b
  b = suma
  suma = a + b
