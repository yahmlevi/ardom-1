from db_accessable import DBAccessable 
from thread2 import ThreadTwo

is_accessable_thread = DBAccessable()
is_accessable_thread.start()

thread = ThreadTwo()
thread.start()

# is_accessable_thread = DBAccessable()
# is_accessable_thread.start():

while True:
    if is_accessable_thread.start():
        print("can access db")
        is_accessable_thread.join()
    
    else:
        print("can't access db")
        thread.join()
        break