import winreg 

key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Windows")  
result = winreg.QueryValueEx(key, CSDVersion)
print(result[0])