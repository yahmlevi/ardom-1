import sql_functions 
import thread1
import thread2
import thread3
import thread4
import thread5

uid = 'four'
io_type = 'output'
data = 'yahm4'

queues_path = 'D:\\projects\\ardom-1\\sql_functions\\queues'
sql_thread = sql_functions.SQLFunctions(queues_path)
sql_thread.start()

thread = thread1.ThreadOne(queues_path)
thread.start()

sql_thread.join()
thread.join()

#sql = sql_functions.SQLFunctions()

#sql.put(uid, io_type, data)

#sql.update(uid, io_type, data)

#row = sql.get(uid)

#sql.delete(uid)

#delete_up_to_date = '2020-10-20'
#sql.clear(delete_up_to_date)

# thread = thread1.ThreadOne()
# thread.start()

# thread2 = thread2.ThreadTwo()
# thread2.start()

# thread3 = thread3.ThreadThree()
# thread3.start()

# thread4 = thread4.ThreadFour()
# thread4.start()

# thread5 = thread5.ThreadFive()
# thread5.start()