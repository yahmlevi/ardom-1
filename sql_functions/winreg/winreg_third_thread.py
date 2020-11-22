import threading
import winreg
import time


class ThirdThread(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
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
                access_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.winreg_path, 0, winreg.KEY_QUERY_VALUE)
                val_from_reg = winreg.QueryValueEx(access_key, self.sub_key)
                winreg.CloseKey(access_key)
                print("value from registry - {}. ThreadThree" .format(val_from_reg))
                time.sleep(1)

            except:
                print("can't GET in WINREG - ThreadThree")
                time.sleep(1)
            
            print("ThreadThree index {}" .format(i))
            
            if i > 5:
                    print("ThreadThree BREAK")
                    break
  
