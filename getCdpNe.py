import os.path
import re
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

save_path = "C:\\Users\\admin\OneDrive\\Documents\\python-programs\\" #Cisco-SPC02TCa19-DB1-DIAGS FILES-01.TXT
#Cisco-SPC12TCa19-DB1-DIAGS FILES-01.TXT
name_of_file1 = input("Name of the INPUT file :")
name_of_file2 = save_path + name_of_file1 + "_OUTPUT"
fileTimeStamp = name_of_file1 + "-" + timestr
completeName = os.path.join(save_path,fileTimeStamp + ".log")
mylines = []
linenum = 0
pattern1 = re.compile("sh device-tracking database")
pattern2 = re.compile("sh ip arp")
pattern3 = re.compile("some text")

with open (save_path+name_of_file1, 'rt') as myfile, open(name_of_file2,'w') as f:
  for line in myfile:
    linenum +=1
    if pattern1.search(line) != None:
      mylines.append(line.rstrip('\n').split('#')[0])
    if pattern2.search(line) != None:
      mylines.append(line.rstrip('\n'))
    if pattern3.search(line) != None:
      mylines.append(line.rstrip('\n'))
    
  for item in mylines:
    f.write(item+'\n')

print("..END of 1st part..")

deviceID = " "
mylines2 = []
with open(name_of_file2,'+r') as myfile2:
  for line in myfile2:
    if "sh cdp ne" in line.rstrip('\n'):
      print(line.rstrip('\n'))
      if deviceID == line.rstrip('\n').split('#')[0]:
        continue
      else:
        deviceID = line.rstrip('\n').split('#')[0]
        mylines2.append(line.rstrip('\n'))
        continue
    else:
      mylines2.append(line.rstrip('\n'))

for item in mylines2:
  print(item)

print("..END of 2nd part..")

