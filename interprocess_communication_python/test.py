#import persistqueue

#q = persistqueue.UniqueQ('D:\projects\ardom-1\interprocess_communication_python')
#q.put('str1')

# from persistqueue import Queue
import persistqueue

path = "D:\\projects\\ardom-1\\interprocess_communication_python"

#q = persistqueue.Queue(path)


q = persistqueue.SQLiteQueue(path, auto_commit=True)
q.put('a')
q.put('b')

