import threading
import sql_functions
import persistqueue
import time
import os

class ThreadOne(threading.Thread):

    def __init__(self, queues_path):
        threading.Thread.__init__(self)
<<<<<<< HEAD
        
        # initialize queues for thread communication 
        q_in_path = queues_path + '\\input'
        self.q_in =  persistqueue.FIFOSQLiteQueue(path=q_in_path, multithreading=True, auto_commit=True, db_file_name="input")

        q_out_path = queues_path + '\\output'
        self.q_out =  persistqueue.FIFOSQLiteQueue(path=q_out_path, multithreading=True, auto_commit=True, db_file_name="output")

=======
        # sql = sql_functions.SQLFunctions()
        

        # sql GET function queue implementaion
        q_in_path = queues_path + '\\input'
        if not os.path.isdir(q_in_path):
            print('making dir from thread')
            self.q_in =  persistqueue.FIFOSQLiteQueue(path=q_in_path, multithreading=True, auto_commit=True, db_file_name="input")  
            #self.q_in.task_done()
        self.q_in =  persistqueue.FIFOSQLiteQueue(path=q_in_path, multithreading=True, auto_commit=True, db_file_name="input")

>>>>>>> db40af3c554a604c0307c755056761f38a6fdee4
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
<<<<<<< HEAD
        flag = True
        data = {
            'function': 'GET',
            'uid': 'one',
            'thread_uid': 'one'
=======
        data = {
            'function': 'GET',
            'uid': 'one'
>>>>>>> db40af3c554a604c0307c755056761f38a6fdee4
        }

        #while True:
        try:
            self.q_in.put(data)
            time.sleep(0.5)
<<<<<<< HEAD
            while flag:
                result = self.q_out.get()
=======
                #break
>>>>>>> db40af3c554a604c0307c755056761f38a6fdee4
        except:
            print('didnt put data')
            
        

       