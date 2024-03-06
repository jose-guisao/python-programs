import os
import re
path = os.getcwd()
print(path)
datafilepath = 'C:\\Users\\admin\\Downloads\\'
filename = "SPR12DC22-DB1-cmds-output-file-for-testing.txt"
pattern1 = re.compile("sh cdp ne")
deviceMarker = " "
mydata = []
with open(datafilepath+filename,'r') as f:
  for line in f:
    mydata.append(line.rstrip('\n'))
    if "sh ip arp" in line.rstrip(): #encontrar donde esta sh cdp en el file
      print(line.rstrip()) # error no esta display la info del cdp
      deviceMarker = line.split('#')[0] # sacar el nombre del switch y usarlo como marker
      continue

    if line.split('#')[0] == deviceMarker:
      print(line.rstrip())
    else:
      #print(line.rstrip())
      continue
print(len(mydata))    
print("--END--")
  
for i in mydata:
  print(i)
