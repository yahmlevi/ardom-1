import sql_functions
import sql_service
import thread1
import thread2

uid = 'four'
io_type = 'output'
data = 'yahm4'

# queues_path = 'D:\\projects\\ardom-1\\sql_functions\\queues'
# sql_thread = sql_service.SQLService(queues_path)
# sql_thread.start()

# thread = thread1.ThreadOne(queues_path)
# thread.start()

# sql_thread.join()
# thread.join()

sql = sql_functions.SQLFunctions()

#sql.put(uid, io_type, data)

sql.update(uid, io_type, data)

#row = sql.get(uid)

#sql.delete(uid)

#delete_up_to_date = '2020-10-20'
#sql.clear(delete_up_to_date)

# thread = thread1.ThreadOne()
# thread.start()

# thread2 = thread2.ThreadTwo()
# thread2.start()
