from test2 import telnet_stream
from test import QueuePrinter
import queue 
import time

if __name__ == '__main__':
     q = queue.Queue()
     stop_threads = False

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
     stop_threads = True
     a.join()
     b.join()
     c.join()
     printer.join()
