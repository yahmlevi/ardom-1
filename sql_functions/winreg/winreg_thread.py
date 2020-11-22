import threading
import winreg
import time


class FirstThread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
        self.string_data = "test-string"
        for i in range(0, 10000):
            self.string_data += "test-string"
        self.winreg_path = "Software\Yahm\Tests\AnotherFive"
        self.sub_key = "test sub-key6"

        try:
            access_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.winreg_path, 0, winreg.KEY_SET_VALUE)
            winreg.CloseKey(access_key)
        except:
            winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.winreg_path)
        

    def run(self):
        i = 0 

        while True:
            i += 1
            try:
                access_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.winreg_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(access_key, self.sub_key, 0, winreg.REG_SZ, self.string_data)
                winreg.CloseKey(access_key)
                print("PUT in winreg from ThreadOne")
                time.sleep(1)

            except:
                print("can't PUT in WINREG - ThreadOne")
                time.sleep(1)

            print("ThreadOne index {}" .format(i))

            if i > 5:
                    print("ThreadOne BREAK")
                    break
