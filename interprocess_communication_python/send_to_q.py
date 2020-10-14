import time
import threading
import queue

class telnet_stream(threading.Thread):
    
    def __init__(self, info, queue):
        threading.Thread.__init__(self)
        self.info = info
        self.q = queue
        self.running = True
    
    def run(self):
        i = 0
        while self.running:
            i += 1
            msg = self.info["name"] + " " + str(i)
            self.q.put(msg)
            time.sleep(1)
            
    def stop(self):
        self.running = False

        


# class QueuePrinter(threading.Thread):
    
#     def __init__(self, queue):
#         threading.Thread.__init__(self)
#         self.q = queue

#         self.running = True

#     def run(self):
#         while True:
#             if not q.empty():
#                 item = q.get()
#                 print(item)
            
#             if stop_threads: 
#                 break

#             else:
#                 print("queue empty")
#                 time.sleep(2)

    

# if __name__ == '__main__':
#     q = queue.Queue()
#     stop_threads = False

#     info1 = {"name": "one"}
#     a = telnet_stream(info1, q)

#     info2 = {"name": "two"}
#     b = telnet_stream(info2, q)

#     info3 = {"name": "three"}
#     c = telnet_stream(info3, q)

#     printer = QueuePrinter(q)

#     a.start()
#     b.start()
#     c.start()
#     printer.start()
#     time.sleep(15) 
#     stop_threads = True
#     a.join()
#     b.join()
#     c.join()
#     printer.join()


        
