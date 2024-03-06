#https://stackoverflow.com/questions/419163/what-does-if-name-main-do
print("before import")
import math

print("before function_a")
def function_a():
  print("Function A")

print("before function_b")
def function_b():
  print("Function B {}".format(math.sqrt(100)))

print("Before __name__ guard")

if __name__ == '__main__':
  function_a()
  function_b()

print("after __name__ guard")
