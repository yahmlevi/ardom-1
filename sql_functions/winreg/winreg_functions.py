import winreg
import sys
import time
import sqlite3

iterations = 1000
string_data = "test-string"
for i in range(0, 10000):
    string_data += "test-string"

# WINREG
#def winreg_put(string_data, winreg_path = "Software\Yahm\Tests", sub_key_name = "test sub-key"):
def winreg_put(string_data, sub_key_name, winreg_path):
    access_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, winreg_path, 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(access_key, sub_key_name, 0, winreg.REG_SZ, string_data)
    winreg.CloseKey(access_key)



winreg_path = "Software\Yahm\Tests\AnotherOneFour"
winreg.CreateKey(winreg.HKEY_CURRENT_USER, winreg_path)
sub_key = "test sub-key"
start_time = time.time()
for i in range(0, iterations):
    sub_key += str(i)
    winreg_put(string_data, sub_key, winreg_path)
total_time = str((time.time() - start_time))
size_of_str = sys.getsizeof(string_data)
print("it took {} sec to PUT a large string of size {} into WINREG {} times" .format(total_time, size_of_str, iterations))
# WINREG



# SQLite
def put(uid, _type, data, table_name_):
    conn = sqlite3.connect('D:\\projects\\ardom-1\\sql_functions\\winreg\\time_tester.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO {} VALUES('{}', '{}', '{}', date('now'))" .format(table_name_, uid, _type, data))
    conn.commit()



def update(uid, type_io, data, table_name):
    conn = sqlite3.connect('D:\\projects\\ardom-1\\sql_functions\\winreg\\time_tester.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("UPDATE {} SET data = '{}', type = '{}' where rowid = '{}'" .format(table_name, data, type_io, uid))
    conn.commit()


# init
conn = sqlite3.connect('D:\\projects\\ardom-1\\sql_functions\\winreg\\time_tester.db', check_same_thread=False)
cursor = conn.cursor()
table_name = 'test1'
cursor.execute("create table if not exists {}(uid, type, data, entry_date)" .format(table_name))
conn.commit()

start_time = time.time()
for i in range(0,iterations):
    pass
    #put(string_data, 'test type', 'test data', table_name)
total_time = str((time.time() - start_time))
print("it took {} sec to PUT a large string of size {} into SQLite {} times" .format(total_time, size_of_str, iterations))




# COMPRESS THE DATA - TAKES MUCH LONGER THEN PUT TO WINREG

# import zlib

#compressed_string_data = zlib.compress(string_data.encode())
# #---------------
# start_time = time.time()
# #print(compressed_string_data)
# compressed_string_data = zlib.compress(string_data.encode(), level=-1)
# total_time = str((time.time() - start_time))
# print("it took {} sec to compress the data" .format(total_time))
# #---------------
# # start_time = time.time()
# # winreg.SetValueEx(access_key, sub_key_name, 0, winreg.REG_SZ, compressed_string_data)
# # total_time = str((time.time() - start_time))
# # size_of_str = sys.getsizeof(compressed_string_data)
# # print("it took {} sec to PUT a compressed string with size {}" .format(total_time, size_of_str))


