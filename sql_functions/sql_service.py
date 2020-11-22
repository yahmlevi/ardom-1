import threading
import persistqueue
from sql_functions import SQLFunctions
import os
import time


class SQLService(threading.Thread):

    def __init__(self, queues_path):
        threading.Thread.__init__(self)
        self.sql_functions = SQLFunctions()
    
        # create requests queue
        q_in_path = queues_path + '\\input'
        if not os.path.isdir(q_in_path):
            self.q_in = persistqueue.FIFOSQLiteQueue(path=q_in_path, multithreading=True, auto_commit=True, db_file_name="input")
            #self.q_in.task_done()
        self.q_in =  persistqueue.FIFOSQLiteQueue(path=q_in_path, multithreading=True, auto_commit=True, db_file_name="input")
        
        # create response queue
        q_out_path = queues_path + '\\output'
        if not os.path.isdir(q_in_path):
            self.q_out = persistqueue.FIFOSQLiteQueue(path=q_out_path, multithreading=True, auto_commit=True, db_file_name="output")
            #self.q_in.task_done()
        self.q_out =  persistqueue.FIFOSQLiteQueue(path=q_out_path, multithreading=True, auto_commit=True, db_file_name="output")


    def run(self):

        while True:  
            #if not self.q_in.empty():
            time.sleep(0.5)
            request = self.q_in.get()
            print(request)

            if request:
                requested_function = request['function']
                thread_uid = request['thread_uid']

                if requested_function == 'GET':
                    uid = request['uid']
                    result = self.sql_functions.get(uid)
                    self.q_out.put(result)
                
                if requested_function == 'PUT':
                    print('PUT FUNC')
                
                if requested_function == 'UPDATE':
                    print('UPDATE FUNC')
                
                if requested_function == 'CLEAR':
                    print('CLEAR FUNC')
                
                if requested_function == 'DEL':
                    print('DEL FUNC')
                
        
        # while True:
        #     try:
        #         self.q.put(rows)
        #         continue
        #     except:
        #         print("can't put output")

