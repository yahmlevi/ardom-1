import persistqueue
import threading
import time
import sys
import os

class Hub(threading.Thread):
    
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
        self.q =  persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name="my_file_name1")


    def run(self):
        while True:  
            if not self.q.empty():
                print(self.q.get())
                time.sleep(0.5)
            else:
                pass
                #print('test')
                #os.execv(sys.executable, ['python'] + sys.argv)
