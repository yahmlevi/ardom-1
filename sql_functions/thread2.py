import threading
import sql_functions 

class ThreadTwo(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
<<<<<<< HEAD
        self.sql = sql_functions.SQLFunctions()
        
        
        
    def run(self):
        i=0    
        while True:
            try:
                i += 1
                print(self.sql.update('test uid', 'test type', 'test data'))
                print('thread 2')
                if i > 20:
                    #break
                    pass
            except KeyboardInterrupt:
                break
=======
        sql = sql_functions.SQLFunctions()
        while True:
            print(sql.get('one'))
            print('thread 2')

>>>>>>> db40af3c554a604c0307c755056761f38a6fdee4
       