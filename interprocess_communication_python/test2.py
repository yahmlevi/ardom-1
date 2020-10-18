import persistqueue
import time
import threading
import sys


class TelnetStream(threading.Thread):
    
    def __init__(self, u_id, path):
        threading.Thread.__init__(self)

        self.u_id = u_id

        self.q_in = persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name=self.u_id, timeout=0.5)    
        self.q_out = persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name="my_file_name", timeout=0.5)
        
        print("TelnetStream {} initialized".format(self.u_id))
    
    def run(self):
        i = 0
        while True:
            try:
                i = i + 1
                self.q_out.put("TelnetStream {} - {}".format(self.u_id, i) )

                while not self.q_in.empty():
                    print(self.q_in.get())
                    time.sleep(0.5)
                
            except:
                ex = sys.exc_info()[0]
                print("Exeption in TelnetStream {}\n\n{}".format(self.u_id, ex))

            time.sleep(0.5)