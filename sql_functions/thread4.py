import threading
import sql_functions 

class ThreadFour(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        sql = sql_functions.SQLFunctions()
        while True:
            print(sql.get('one'))
            print('thread 4')

       