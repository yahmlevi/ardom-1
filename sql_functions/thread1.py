import threading
import sql_functions
import persistqueue
import time
import os

class ThreadOne(threading.Thread):

    def __init__(self, queues_path):
        threading.Thread.__init__(self)
        # sql = sql_functions.SQLFunctions()
        

        # sql GET function queue implementaion
        q_in_path = queues_path + '\\input'
        if not os.path.isdir(q_in_path):
            print('making dir from thread')
            self.q_in =  persistqueue.FIFOSQLiteQueue(path=q_in_path, multithreading=True, auto_commit=True, db_file_name="input")  
            #self.q_in.task_done()
        self.q_in =  persistqueue.FIFOSQLiteQueue(path=q_in_path, multithreading=True, auto_commit=True, db_file_name="input")

        # data = {
        #     'function': 'test'
        # }

        # while True:
        #     try:
        #         self.q_in.put(data)
        #         time.sleep(0.5)
        #     except:
        #         print('didnt put data')
        

        # q_out_path = queues_path + '\\output'
        # if not os.path.isdir(q_out_path):
        #     self.q_out =  persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name="output")  
        #     self.q_out.task_done()

    def run(self):
        data = {
            'function': 'GET',
            'uid': 'one'
        }

        #while True:
        try:
            self.q_in.put(data)
            time.sleep(0.5)
                #break
        except:
            print('didnt put data')
            
        

       