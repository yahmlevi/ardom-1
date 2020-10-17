import persistqueue
import time
import threading


class TelnetStream(threading.Thread):
    
    def __init__(self, path, queue):
        threading.Thread.__init__(self)
        #self.q = persistqueue.SQLiteQueue(path, auto_commit=True)
        self.q = queue

    
    def run(self):
        while True:
            try:
                self.q.put("yahm11")
                time.sleep(2)
            except KeyboardInterrupt:
                break