import persistqueue


path = "D:\\projects\\ardom-1\\interprocess_communication_python"

q = persistqueue.SQLiteQueue(path, auto_commit=True)
print(q.get())
