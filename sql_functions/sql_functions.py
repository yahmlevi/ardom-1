import sqlite3
import threading
import persistqueue
import time
import os

class SQLFunctions(threading.Thread):
#class SQLFunctions():

    def __init__(self, queues_path):
        threading.Thread.__init__(self)
        self.conn = sqlite3.connect('D:\\projects\\ardom-1\\sql_functions\\testdatabase.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.table_name = 'proccess'
        self.cursor.execute("create table if not exists {}(uid text, type text, data text, entry_date datetime)" .format(self.table_name))
        self.conn.commit()
        
        
        # sql GET function queue implementaion
        q_in_path = queues_path + '\\input'
        if not os.path.isdir(q_in_path):
            print('making dir from sql')
            self.q_in = await persistqueue.FIFOSQLiteQueue(path=q_in_path, multithreading=True, auto_commit=True, db_file_name="input")  
            #self.q_in.task_done()
        self.q_in =  persistqueue.FIFOSQLiteQueue(path=q_in_path, multithreading=True, auto_commit=True, db_file_name="input")
        

        # while True:  
        #     #if not self.q_in.empty():
        #     request = self.q_in.get()
        #     print(request)
        #     time.sleep(0.5)
        #     if request:
        #         requested_function = request['function']
        #         print(requested_function)
          

        # q_out_path = queues_path + '\\output'
        # #if not os.path.isdir(q_out_path):
        # self.q_out =  persistqueue.FIFOSQLiteQueue(path=path, multithreading=True, auto_commit=True, db_file_name="output")  
        # self.q_out.task_done()

    def run(self):
        while True:  
            if not self.q_in.empty():
                request = self.q_in.get()
                print(request)
                time.sleep(0.5)
                if request:
                    requested_function = request['function']
                    print(requested_function)
                    if requested_function == 'GET':
                        print('success')
                
        
        # while True:
        #     try:
        #         self.q.put(rows)
        #         continue
        #     except:
        #         print("can't put output")


        
        
        
        
    def put(self, uid, _type, data):
        print('Inserting to DB table')
        self.cursor.execute("INSERT INTO {} VALUES('{}', '{}', '{}', date('now'))" .format(self.table_name, uid, _type, data))
        self.conn.commit()
        print('inserted into DB')
        

    def update(self, uid, type_io, data):
        print('Updating table')
        self.cursor.execute("UPDATE {} SET data = '{}' where uid = '{}'" .format(self.table_name, data, uid))
        self.cursor.execute("UPDATE {} SET type = '{}' where uid = '{}'" .format(self.table_name, type_io, uid))
        self.conn.commit()
        print('Updated table')

        

    def get(self, uid):
        self.cursor.execute("SELECT type, data FROM {} WHERE uid = '{}'" .format(self.table_name, uid))
        rows = self.cursor.fetchall()
        return rows


    def clear(self, date):
        self.cursor.execute("DELETE FROM '{}' WHERE date(entry_date) < '{}'" .format(self.table_name, date))
        self.conn.commit()
        print('Deleted all data up to date {}' .format(date))
        

    def delete(self, uid):
        self.cursor.execute("DELETE FROM {} WHERE uid = '{}'" .format(self.table_name, uid))
        print('Deleted row with uid - {}' .format(uid))
        self.conn.commit()