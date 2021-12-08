#!/usr/bin/env python
"""Return the ssh output with password connection and Linux commands"""
import paramiko
import getpass
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass()
conn = client.connect('192.168.5.150', port='22', username='pi', password=password)
# Obtain session
session = client.get_transport().open_session()
print("| Retcode: "+str(session)+"|")

stdin, stdout, stderr=client.exec_command('sudo hostname;w')
save_stdout = stdout.readlines()
retcode = stdout.channel.recv_exit_status()

stdin, stdout, stderr=client.exec_command('ls -ls;')
save_stdout2 = stdout.readlines()
# print(save_stdout,save_stdout2)
for line in save_stdout2:
    print(line)