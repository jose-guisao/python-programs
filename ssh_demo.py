#!/usr/bin/env python

import sys, paramiko, getpass

if len(sys.argv) < 3:
    print("args missing")
    sys.exit(1)

hostname = sys.argv[1]
#password = sys.argv[2]
command = sys.argv[2]
password = getpass.getpass()
username = "pi"
port = 22
nbytes = 512
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
    client.connect(hostname, port=port, username=username, password=password)
    trans = paramiko.Transport(hostname, port)
    trans.connect(username=username, password=password)
    session = trans.open_channel("session")
    session.exec_command('ls -ls')
    exit_status = session.recv_exit_status()
    stdout_data = []
    stderr_data = []
    while session.recv_ready():
        stdout_data.append(session.recv(nbytes))
        stdout_data = b"".join(stdout_data)

    while session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
        stderr_data = "".join(stderr_data)

    print("exit status", exit_status)
    print("output")
    print(stdout_data)
    print("error")
    print(stderr_data)
    #stdin, stdout, stderr = client.exec_command(command)
    #print(stdout.read()),

finally:
    client.close()