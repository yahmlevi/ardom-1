import test2 
import test
import time
from persistqueue import FIFOSQLiteQueue

if __name__ == '__main__':

     path = "D:\\projects\\ardom-1\\interprocess_communication_python\\data"
     
     stream_thread = test2.TelnetStream("One",  path)
     time.sleep(0.5)

     stream_thread1 = test2.TelnetStream("Two", path)
     time.sleep(0.5)

     stream_thread2 = test2.TelnetStream("Three", path)
     time.sleep(0.5)

     receiver_thread = test.Hub(path, ["One", "Two", "Three"])
     time.sleep(0.5)
     
     stream_thread.start() 
     stream_thread1.start()
     stream_thread2.start()
     receiver_thread.start()
     
     stream_thread.join()
     stream_thread1.join()
     stream_thread2.join()
     receiver_thread.join()
     