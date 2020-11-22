import in_memory_sqlite

uid = 'four'
io_type = 'output'
data = 'yahm4'


sql = in_memory_sqlite.InMemorySQL()

sql.put(uid, io_type, data)

sql.update(uid, io_type, data)

row = sql.get(uid)
print(row)

sql.delete(uid)

# delete_up_to_date = '2020-10-20'
# sql.clear(delete_up_to_date)
