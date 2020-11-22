import sqlite3
import time
import os
import datetime

class QueryOpt():

    #start_time = time.time()
    #print("--- %s seconds ---" % (time.time() - start_time))

    def __init__(self):
        self.conn = sqlite3.connect('D:\\projects\\ardom-1\\sql_functions\\time_tester.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

        self.table_name = 'test1'
        self.cursor.execute("create table if not exists {}(uid, type, data, entry_date)" .format(self.table_name))
        self.conn.commit()
        
        self.table_name1 = 'test2'
        self.cursor.execute("create table if not exists {}(uid text, type boolean, data text, entry_date datetime)" .format(self.table_name1))
        self.conn.commit()
        
        self.table_name3 = 'test3'
        self.cursor.execute("create table if not exists {}(uid varchar, type boolean, data varchar, entry_date random)" .format(self.table_name3))
        self.conn.commit()
        

      
    def put(self, uid, _type, data, table_name_):
        self.cursor.execute("INSERT INTO {} VALUES('{}', '{}', '{}', date('now'))" .format(table_name_, uid, _type, data))
        self.conn.commit()

    def get(self, uid, table_name_):
        self.cursor.execute("SELECT type, data FROM {} WHERE uid = '{}'" .format(table_name_, uid))
        rows = self.cursor.fetchall()
        return rows
          
    def delete_table(self, table_name):
        self.cursor.execute("DELETE FROM {}" .format(table_name))
        self.conn.commit()


Query = QueryOpt()

table_name1 = 'test1'
uid = 0
start_time = time.time()
for i in range(1, 100):
    uid += 1
    Query.put(uid, 'test type', 'test data', table_name1)
total_time = str((time.time() - start_time))
print(Query.get(1, table_name1))
Query.delete_table(table_name1)
print(Query.get(1, table_name1))
print('---------------------------')
print('first table took {} micro sec to query the PUT function 10K times' .format(total_time))
print('---------------------------')
    

table_name2 = 'test2'
uid = 0
start_time = time.time()
for i in range(1, 100):
    uid += 1
    Query.put(uid, 'False', 'test data', table_name2)
total_time = str((time.time() - start_time))
print(Query.get(1, table_name2))
Query.delete_table(table_name2)
print(Query.get(1, table_name2))
print('---------------------------')
print('second table took {} micro sec to query the PUT function 10K times' .format(total_time))
print('---------------------------')


table_name3 = 'test3'
uid = 0
start_time = time.time()
for i in range(1, 100):
    uid += 1
    Query.put(uid, 'test type', 'test data', table_name3)
total_time = str((time.time() - start_time))
print(Query.get(1, table_name3))
Query.delete_table(table_name3)
print(Query.get(1, table_name3))
print('---------------------------')
print('third table took {} sec to query the PUT function 10K times' .format(total_time))
print('---------------------------')
