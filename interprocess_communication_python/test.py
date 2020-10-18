import persistqueue
import threading
import time
import sys

class Hub(threading.Thread):
    
    def __init__(self, path, stream_uid_list):
        threading.Thread.__init__(self)

        self.telnet_stream_q_in_list = []
        for u_id in stream_uid_list:
            q_in =  persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name=u_id, timeout=0.5)  
            self.telnet_stream_q_in_list.append(q_in)

        self.q = persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name="my_file_name", timeout=10.0)
        print("Hub is ready")

    def run(self):
        while True:

            try:    
                if not self.q.empty():
                    print(self.q.get())
                
                for q_in in self.telnet_stream_q_in_list:
                    # print("Putting value in queue ")
                    q_in.put("Some value")

            except:
                ex = sys.exc_info()[0]
                print ("Exception in Hub - {}".format(ex))
                time.sleep(1.2)
                
            time.sleep(0.5)


