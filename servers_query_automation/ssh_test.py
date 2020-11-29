# GREAT SSH ARTICLE https://www.hanselman.com/blog/how-to-ssh-into-a-windows-10-machine-from-linux-or-windows-or-anywhere

import paramiko

ip='192.168.0.72'
port=22
username='Yahm'
password='211367909'

ip_ama = '192.168.0.32'
username_ama = 'מרב'
password_ama = '?7690'
print(username_ama)
cmd='dir'

# connect to remote pc
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip_ama, port, username_ama, password_ama)

# 
stdin,stdout,stderr = ssh.exec_command(cmd)
outlines = stdout.readlines()
resp=''.join(outlines)
print(resp)
