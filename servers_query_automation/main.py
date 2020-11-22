import subprocess
import os
import platform

ip_list = [192.168.68.105, 190.165.67.104]

powershell_script_path = "D:\\projects\\ardom-1\\servers_query_automation\\get_os_type.ps1"


# TODO
# for item in ip_list:
#   - execute bash script that connects to pc via ssh
#   - transfer all scripts we need to remote pc with scp
#   - execute all scripts and put response in known place at remote pc
#   - execute script to get response from known place in remote pc via ssh  

p = subprocess.Popen(["powershell.exe", powershell_script_path],)

#print(p)
#print(p.communicate())