import time
import threading
import queue


class QueuePrinter(threading.Thread):
    
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.q = queue

        self.running = True

    def run(self):
        while self.running:
            if not self.q.empty():
                item = self.q.get()
                print(item)
            else:
                print("queue is empty - waiting 2 sec")
                time.sleep(2)

    def stop(self):
        self.running = False