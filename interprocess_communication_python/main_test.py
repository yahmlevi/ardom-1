from test2 import TelnetStream
from test import Hub
import time
from persistqueue import FIFOSQLiteQueue

if __name__ == '__main__':

     path = "D:\\projects\\ardom-1\\interprocess_communication_python"
     q = FIFOSQLiteQueue(path=path, multithreading=True)

     stream_thread = TelnetStream(path, q)
     receiver_thread = Hub(path, q)

     stream_thread.start()
     receiver_thread.start()
     
     time.sleep(15)

     stream_thread.join()
     receiver_thread.join()
     