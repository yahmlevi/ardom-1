import time
import threading
import queue

class telnet_stream(threading.Thread):
    
    #def __init__(self, info, tn):
    def __init__(self, info):
        threading.Thread.__init__(self)
        self.info = info
        #self.sessionfileinput = info["sessionfolder"] + "\\" + "input.txt"
        #self.sessionfileoutput = info["sessionfolder"] + "\\" + "output.txt"
        #self.tn = tn
        self.running = True

    def run(self, q):
        i = 0
        while self.running:
            i += 1
            q.put(i)
            time.sleep(2)


    def print_get_from_q(self, q):
        while True:
            if not q.empty():
                item = q.get()
                print(item)
            else:
                print("queue empty")
                time.sleep(2)

    def stop(self):
        self.running = False



if __name__ == '__main__':
    q = queue.Queue()
    a = threading.Thread(target=telnet_stream.run, args=(q,))
    b = threading.Thread(target=telnet_stream.print_get_from_q, args=(q,))
    a.start()
    b.start()
    telnet_stream.stop()
    a.join()
    b.join()
        
