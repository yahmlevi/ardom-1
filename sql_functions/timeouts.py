import sqlite3
import time
import os

class SQLFunctions():

    def access_db_get_func(uid, table_name='proccess', timeout):
        
        total_time_slept = 0
        sleep_time = 0.05
        connection_str = 'D:\\projects\\ardom-1\\sql_functions\\testdatabase.db'
        flag = True

        while flag:
            
            try:
                conn = sqlite3.connect(connection_str, check_same_thread=False, timeout=1)
                cursor = conn.cursor()
                cursor.execute("SELECT type, data FROM {} WHERE uid = '{}'" .format(table_name, uid))
                rows = cursor.fetchall()

            except sqlite3.OperationalError:
                time.sleep(sleep_time)
                total_time_slept += sleep_time

                if total_time_slept > timeout:
                    flag = False


        
