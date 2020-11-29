import sqlite3


conn = sqlite3.connect('D:\\projects\\ardom-1\\servers_query_automation\\query_to_os_version.db', check_same_thread=False)
cursor = conn.cursor()
table_name = 'query_to_os_version'
cursor.execute("create table if not exists {}(query1 text, query2 text, query3 text, query4 text, os_version text)" .format(table_name))
conn.commit()
cursor.execute("insert into {} values (?, ?, ?, ?, ?)" .format(table_name), ['SOME QUERY FOR SPECIFIC OS VERSION1_3', 'SOME QUERY FOR SPECIFIC OS VERSION2_3', 'SOME QUERY FOR SPECIFIC OS VERSION3_3', 'SOME QUERY FOR SPECIFIC OS VERSION4_3', "TEST OS VERSION1"])
conn.commit()
conn.close()