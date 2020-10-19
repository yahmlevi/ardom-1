import threading
import sql_functions 

class ThreadOne(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        sql = sql_functions.SQLFunctions()
        print(sql.get('one'))

       