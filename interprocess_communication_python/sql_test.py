import sql_functions 

uid = 'one'
io_type = 'input'
data = 'test data'

sql = 
sql = sql_functions.SQLFunctions(uid, io_type, data)
sql.put()
