'''
import subprocess
iplist = list(range(1,254))
ip_list = ["192.168.0."+str(iplist[i]) for i in range(0,253)]
for i, ip in enumerate(iplist):
    p = subprocess.Popen('ping '+ip_list[i],stdout=subprocess.PIPE)
    # the stdout=subprocess.PIPE will hide the output of the ping command
    #p.wait()
    if p.poll():
        print( ip_list[i]+" is down")
    else:
        print( ip_list[i]+" is up")
'''

import ipaddress, subprocess
myIpAddress = input('Enter an IP Address with a CIDR >>> ') #192.168.0.1/24
myAdd = ipaddress.ip_interface(myIpAddress)
myNet = ipaddress.ip_network(myAdd, strict = False) # False lets you enter any ip address in the /24 ip address block.
for i in myNet:
    canPing = subprocess.call('ping -n 2 -w 500 %s' % str(i))
    if canPing == 0:
        print('I can ping %s.' % str(i))
    if canPing == 1:
        print('%s is not responding' % str(i))

print("...END...")
