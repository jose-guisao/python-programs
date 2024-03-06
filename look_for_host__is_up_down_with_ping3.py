from ping3 import ping, verbose_ping
import time
ip_list = open('ips_local.txt','w')
subNetwork = input("Enter SubNetwork for test :")
numberOfHosts = input("Enter number of host to test :")
fourOctect = list(range(1,int(numberOfHosts)))
ipAddress = [subNetwork[0:-1]+str(line) for line in fourOctect]

for ip in ipAddress:
##  time.sleep(.125)
  ip = ip.strip('\n')
  response = ping(ip,1)
  print(response,' ',ip)
  #ip_list.write(response,' ',ip)
  print('End')
