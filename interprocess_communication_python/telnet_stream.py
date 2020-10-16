import time
import threading
import queue

# A SIDE
class Telnet_Stream(threading.Thread):
    
    def __init__(self, info, queue_in, queue_out):
        threading.Thread.__init__(self)
        self.info = info
        self.q_in = queue_in
        self.q_out = queue_out
        self.running = True
    
    def run(self):
        i = 0
        while self.running:
            # send data
            i += 1
            msg = 'A SIDE: thread name - ' + self.info["uid"] + ", index-" + str(i)
            self.q_out.put(msg)
            
            if not self.q_in.empty():
                # receive data
                received_item = self.q_in.get()
                print("A SIDE: Received value '{}' from '{}'".format(received_item, self.info["uid"]))
                #print("A SIDE: IN QUEUE from '{}' got:".format(self.info['uid']), received_item)

            time.sleep(2)
            
    def stop(self):
        self.running = False

        


# class QueuePrinter(threading.Thread):
    
#     def __init__(self, queue):
#         threading.Thread.__init__(self)
#         self.q_out = queue

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


        
