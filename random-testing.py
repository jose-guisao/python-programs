import random

x = random.randrange(100)
#print(x)
iters=0
for i in range(9999):
  iters+=1
  i = random.randrange(1001)
  if x == i:
    print("Match found in ",iters," iterations . The number was ",i)
    break
  else:
    continue
#print("END", iters)

