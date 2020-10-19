import persistqueue
import time
import threading
import os 
import sys


class TelnetStream(threading.Thread):

    
    def __init__(self, path):
        threading.Thread.__init__(self)
        if not os.path.isdir(path):
            self.q =  persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name="my_file_name1")  
            self.q.task_done()
            print('was here')
            print('was here')
            print('was here')
            print('was here')
            print('was here')
        
        self.q = persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name="my_file_name1")    

    def run(self):
        i = 0
        while True:
            i = i + 1
            try:
                self.q.put('yahm')
                time.sleep(0.5)
            except:
                print('cant put')

