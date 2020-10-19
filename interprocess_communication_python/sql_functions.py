import sqlite3

class SQLFunctions():

    def __init__(self, uid, io_type, data):

        self.conn = sqlite3.connect('D:\\projects\\ardom-1\\interprocess_communication_python\\testdatabase.db')
        self.cursor = self.conn.cursor()
        self.uid = uid
        self.type = io_type
        self.data = data
        self.table_name = 'proccess'
        
        #self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name={}" .format(self.table_name))
        try:
            self.cursor.fetchone()[0]
        except:
            print('creating table...')
            self.cursor.execute("CREATE TABLE proccess(uid text, type text, data text)")
            self.conn.commit()

    def put(self):
        print('Inserting to DB table')
        self.cursor.execute("INSERT INTO {} VALUES({}, {}, {})" .format(self.table_name, self.uid, self.type, self.data))
        self.conn.commit()
        print('inserted into DB')
        

    def get(self):
        pass

    def clear(self, date):
        pass

    def delete(self):
        pass