from zvapp.logic.GENERAL import GEN
import sqlite3
import time
import codecs
import datetime 


class SQLFunctions_recreate_table():

    def create(sql_path):
        try:
            conn = sqlite3.connect(sql_path, check_same_thread=False, timeout=20000)
            cursor = conn.cursor()
            table_name = 'temp_proccess'
            cursor.execute("create table if not exists {}(uid text unique PRIMARY KEY, type text, data text, entry_date datetime, datetime_alive datetime, session text)" .format(table_name))
            conn.commit()
        except conn.Error as error:
            print("Error while connecting to sqlite", error)

    def drop(sql_path):
        try:
            conn = sqlite3.connect(sql_path, check_same_thread=False, timeout=20000)
            cursor = conn.cursor()
            table_name = 'temp_proccess'
            cursor.execute("DROP TABLE IF EXISTS {}" .format(table_name))
            conn.commit()
        except conn.Error as error:
            print("Error while droping to sqlite", error)

class SQLFunctions():

    def __init__(self, sql_path):
        try:
            self.conn = sqlite3.connect(sql_path, check_same_thread=False, timeout=20000)
            self.cursor = self.conn.cursor()
            self.table_name = 'temp_proccess'
        except self.conn.Error as error:
            print("Error while connecting to sqlite", error)

    def close(self):
        self.conn.close()

    def post(self, uid, _type, data):
        res = SQLFunctions.get(self, uid)
        if res == []:
            SQLFunctions.insert(self, uid, _type, data)
        else:
            SQLFunctions.update(self, uid, _type, data)
        #output = ""

    def insert(self, uid, _type, data):
        try:
            now = datetime.datetime.now()
            d_now = now.strftime("%m/%d/%Y, %H:%M:%S %f")
            self.cursor.execute("INSERT INTO {} VALUES('{}', '{}', '{}', date('now'),'{}','')" .format(self.table_name, uid, _type, data, d_now))
            self.conn.commit()
        except self.conn.Error as error:
            print("Error while insert to sqlite", error)
        
    def update(self, uid, type_io, data):
        try:
            self.cursor.execute("UPDATE {} SET data = '{}', type = '{}' where uid = '{}'" .format(self.table_name, data, uid))
            #self.cursor.execute("UPDATE {} SET type = '{}' where uid = '{}'" .format(self.table_name, type_io, uid))
            self.conn.commit()
        except self.conn.Error as error:
            print("Error while update to sqlite", error)


    # DONE
    def get(self, uid):
        try:
            self.cursor.execute("SELECT type, data FROM {} WHERE uid = '{}'" .format(self.table_name, uid))
            rows = self.cursor.fetchall()
            return rows
        except self.conn.Error as error:
            print("Cant GET from DB", error)
            return 'Error'

    # DONE
    def clear(self, date):
        try:
            self.cursor.execute("DELETE FROM '{}' WHERE date(entry_date) < '{}'" .format(self.table_name, date))
            self.conn.commit()
        except self.conn.Error:
            print("Cant CLEAR from DB")        
        
    # DONE
    def delete(self, uid):
        try:
            self.cursor.execute("DELETE FROM {} WHERE uid = '{}'" .format(self.table_name, uid))
            self.conn.commit()
            print('Deleted row with uid - {}' .format(uid))
        except self.conn.Error:
            print("Cant DEL from DB")              


    def get_session_list(self):
        try:
            self.cursor.execute("SELECT uid FROM {}" .format(self.table_name))
            rows = self.cursor.fetchall()
            return rows
        except self.conn.Error:
            print("Error while get_session to sqlite")
            return 'Error'  


    def get_alive_date(self, uid):
        try:
            self.cursor.execute("SELECT uid, datetime_alive, data FROM {} WHERE uid = '{}'" .format(self.table_name, uid))
            rows = self.cursor.fetchall()
        except self.conn.Error as error:
            print("Error while get_alive to sqlite", error) 
        try:
            output = list(rows[0])
        except:
            output = rows
        return output

    def update_alive_date(self, uid, datetime_alive):
        try:
            self.cursor.execute("UPDATE {} SET datetime_alive = '{}' where uid = '{}'" .format(self.table_name, datetime_alive, uid))
            replay = self.conn.commit()
        except self.conn.Error as error:
            print("Error while update_alive to sqlite", error) 

# session

    def get_session(self, uid):
        try:
            self.cursor.execute("SELECT uid, session FROM {} WHERE uid = '{}'" .format(self.table_name, uid))
            rows = self.cursor.fetchall()
        except self.conn.Error as error:
            print("Error while get_session to sqlite", error) 
        try:
            output = list(rows[0])
        except:
            output = rows
        return output

    def update_session(self, uid, session):
        # print(session)
        try:
            # session = bytes(session, 'utf-8').decode('utf-8', 'ignore')
            self.cursor.execute("UPDATE {} SET session = '{}' where uid = '{}'" .format(self.table_name, session, uid))
            replay = self.conn.commit()
        except self.conn.Error as error:
            print("Error while update_session to sqlite", error) 

#test

    def test_str(self):
        string = self
        for character in string:
            point = ord(character)
            if point == 0:
                print("SQLite identifier contains NUL character.")
                print(character)
            elif 0xD800 <= point <= 0xDBFF:
                print("SQLite identifier contains high-surrogate character.")
                print(character)
            elif 0xDC00 <= point <= 0xDFFF:
                print("SQLite identifier contains low-surrogate character.")
                print(character)
            elif 0xFDD0 <= point <= 0xFDEF or (point % 0x10000) in (0xFFFE, 0xFFFF):
                print("SQLite identifier contains non-character character.")
                print(character)
