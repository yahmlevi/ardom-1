import sqlite3


class InMemorySQL():

    def __init__(self):
        #self.conn = sqlite3.connect(":memory:", check_same_thread=False, timeout=1)
        self.conn = sqlite3.connect('D:\\projects\\ardom-1\\sql_functions\\testdatabase.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.table_name = 'proccess'
        self.cursor.execute("create table if not exists {}(uid PRIMARY KEY, type text, data text, entry_date datetime)" .format(self.table_name))
        self.conn.commit()

        
    def put(self, uid, _type, data):
        print('Inserting to DB table')
        self.cursor.execute("INSERT INTO {} VALUES('{}', '{}', '{}', date('now'))" .format(self.table_name, uid, _type, data))
        self.conn.commit()
        print('inserted into DB')
        

    def update(self, uid, type_io, data):
        print('Updating table')
        self.cursor.execute("UPDATE {} SET data = '{}', type = '{}' where rowid = '{}'" .format(self.table_name, data, type_io, uid))
        self.conn.commit()
        print('Updated table')
        

    def get(self, uid):
        self.cursor.execute("SELECT type, data FROM {} WHERE uid = '{}'" .format(self.table_name, uid))
        rows = self.cursor.fetchall()
        return rows


    def clear(self, date):
        self.cursor.execute("DELETE FROM '{}' WHERE date(entry_date) < '{}'" .format(self.table_name, date))
        self.conn.commit()
        print('Deleted all data up to date {}' .format(date))
        

    def delete(self, uid):
        self.cursor.execute("DELETE FROM {} WHERE uid = '{}'" .format(self.table_name, uid))
        print('Deleted row with uid - {}' .format(uid))
        self.conn.commit()
