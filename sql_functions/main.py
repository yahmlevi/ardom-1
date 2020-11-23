<<<<<<< HEAD
import sql_functions
import sql_service
import thread1
import thread2
=======
import sql_functions 
import thread1
import thread2
import thread3
import thread4
import thread5
>>>>>>> db40af3c554a604c0307c755056761f38a6fdee4

uid = 'four'
io_type = 'output'
data = 'yahm4'

<<<<<<< HEAD
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
=======
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
>>>>>>> db40af3c554a604c0307c755056761f38a6fdee4

#row = sql.get(uid)

#sql.delete(uid)

#delete_up_to_date = '2020-10-20'
#sql.clear(delete_up_to_date)

# thread = thread1.ThreadOne()
# thread.start()

# thread2 = thread2.ThreadTwo()
# thread2.start()
<<<<<<< HEAD
=======

# thread3 = thread3.ThreadThree()
# thread3.start()

# thread4 = thread4.ThreadFour()
# thread4.start()

# thread5 = thread5.ThreadFive()
# thread5.start()
>>>>>>> db40af3c554a604c0307c755056761f38a6fdee4
