import sqlite3
import sql_functions
import threading

class DBAccessable(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.sql = sql_functions.SQLFunctions()
    


    def run(self):

        connection_str = 'D:\\projects\\ardom-1\\sql_functions\\testdatabase.db'

        try:
            # conn = sqlite3.connect(connection_str, check_same_thread=False, timeout=1)
            # cursor = conn.cursor()
            # table_name = 'proccess'
            # cursor.execute("INSERT INTO {} VALUES('{}', '{}', '{}', date('now'))" .format(table_name ,'test uid', 'test type', 'test dat'))
            # conn.commit()
            # conn.close()
            self.sql.update('test uid', 'test type', 'test data')
            return True
                
        #except sqlite3.OperationalError:
        except:
            return False


        
