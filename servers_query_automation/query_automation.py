import subprocess

# RUN POWERSHELL COMMAND FROM CMD
# https://superuser.com/questions/1080239/run-powershell-command-from-cmd


hostname_list = ['ardom-as8', 'ardom-adr9', 'ardom-at3']


# for hostname in hostname_list:
    
#     try:
#         #server_os_version_binary = subprocess.check_output('systeminfo | findstr /B /C:"OS Name" \\ {}' .format(hostname), stderr=subprocess.STDOUT, shell=True)
#         server_os_version_binary = subprocess.check_output('systeminfo | findstr /B /C:"OS Name"', stderr=subprocess.STDOUT, shell=True)
#         server_os_version_str = server_os_version_binary.decode('ascii')
#         server_os_version = server_os_version_str[27:]
#     except:
#         print("could not get server's OS version")
#         break
    
#     switcher = { 
# 		"Microsoft Windows 10 Home": "get query", 
# 		"windows 7": "get query2", 
# 		"windows 99": "get query", 
# 	}

#     print(switcher.get(server_os_version, "nothing"))


server_os_version_binary = subprocess.check_output('systeminfo | findstr /B /C:"OS Name"', stderr=subprocess.STDOUT, shell=True)
server_os_version_str = server_os_version_binary.decode('ascii')
server_os_version = server_os_version_str[27:]
print(server_os_version_str[27:])
