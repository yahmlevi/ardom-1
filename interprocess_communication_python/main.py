from get_from_q import QueuePrinter
from send_to_q import telnet_stream
import queue
import time


if __name__ == '__main__':
    q = queue.Queue()

    info1 = {"name": "one"}
    a = telnet_stream(info1, q)

    info2 = {"name": "two"}
    b = telnet_stream(info2, q)

    info3 = {"name": "three"}
    c = telnet_stream(info3, q)

    printer = QueuePrinter(q)

    a.start()
    b.start()
    c.start()
    printer.start()
  
    time.sleep(15) 
  
    a.join()
    b.join()
    c.join()
    printer.join()


        
