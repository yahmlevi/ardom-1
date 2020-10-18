import persistqueue
import time
import threading


class TelnetStream(threading.Thread):
    
    def __init__(self, path):
        threading.Thread.__init__(self)
        self.q = persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name="my_file_name1", timeout=0.5)    
        
    def run(self):
        i = 0
        while True:
            i = i + 1
            self.q.put(i)
            time.sleep(0.5)


