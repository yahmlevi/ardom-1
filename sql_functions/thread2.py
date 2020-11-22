import threading
import sql_functions 

class ThreadTwo(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
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
       