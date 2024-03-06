#Read cisco text file and print
import time
st = time.time()
filelist = []
f=open('Cisco-SPC02TCa19-DB1-DIAGS FILES-01.TXT','r')
for line in f.readlines():
  filelist.append(line.rstrip('\n'))

et = time.time()

elapsed_time = et - st

print('Execution time: ',elapsed_time, 'seconds')
