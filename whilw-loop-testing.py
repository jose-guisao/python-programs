import keyboard
import time
import random


def funct_iter(x):
  iters=0
  for i in range(9999):
    iters+=1
    i = random.randrange(1001)
    if x == i:
      print("Match found in ",iters," iterations . The number was ",i)
      return
    else:
      continue

def funct_iter2():
  x = random.randrange(1001)
  funct_iter(x)

while(True):
  keyboard.wait('space')
  funct_iter2()
  if keyboard.is_pressed('esc'):
    break

print("END")
