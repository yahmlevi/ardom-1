import persistqueue
import threading
import time

class Hub(threading.Thread):
    
    def __init__(self, path):
        threading.Thread.__init__(self)
        self.q =  persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name="my_file_name1", timeout=0.5)  
        
    def run(self):
        while True:  
            if not self.q.empty():
                print(self.q.get())
                time.sleep(0.5)
