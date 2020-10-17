#import persistqueue
import threading

class Hub(threading.Thread):
    
    def __init__(self, path, queue):
        threading.Thread.__init__(self)
        #self.q = persistqueue.SQLiteQueue(path, auto_commit=True)
        self.q = queue

    def run(self):
        if not self.q.empty():
            print(self.q.get())

