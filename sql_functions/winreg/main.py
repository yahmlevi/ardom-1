import winreg_thread
import winreg_second_thread
import winreg_third_thread
import time

if __name__ == '__main__':

     first_thread = winreg_thread.FirstThread()
     second_thread = winreg_second_thread.SecondThread()
     third_thread = winreg_third_thread.ThirdThread()

     first_thread.start()
     second_thread.start()
     third_thread.start()
     
     first_thread.join()
     second_thread.join()
     third_thread.join()