import sql_functions 
import thread1
import thread2

uid = 'five'
io_type = 'output'
data = 'yahssddm121 yahm'


sql = sql_functions.SQLFunctions()

#sql.put(uid, io_type, data)

#sql.update(uid, io_type, data)

row = sql.get(uid)

#sql.delete(uid)

delete_up_to_date = '2020-10-20'
#sql.clear(delete_up_to_date)

thread = thread1.ThreadOne()
thread.start()

thread2 = thread2.ThreadTwo()
thread2.start()