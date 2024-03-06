import os
path = os.getcwd()
print(path)
datafilepath = 'C:\\Users\\admin\\Downloads\\'
filename = "SPR12DC22-DB1-cmds-output-file-for-testing.txt"

deviceMarker = " "
mylines = []
with open(datafilepath+filename,'r') as f:
  for line in f:
    if "sh cdp ne" in line.rstrip('\n'): #encontrar donde esta sh cdp en el file
      #print(line.rstrip('\n')) # error no esta display la info del cdp
      deviceMarker = line.split('#')[0] # sacar el nombre del switch y usarlo como marker
      #continue
      if line.split('#')[0] == deviceMarker:
        #print(line.rstrip('\n'))
        mylines.append(line.rstrip('\n').split('#')[0])
        continue
      else:
        mylines.append(line.rstrip('\n').split('#')[0])      
        continue
    else:
      mylines.append(line.rstrip('\n'))

for item in mylines:
  print(item)

print("--END--")
  
