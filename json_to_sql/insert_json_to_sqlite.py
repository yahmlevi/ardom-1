import json
import sqlite3
<<<<<<< HEAD
import time
=======
>>>>>>> db40af3c554a604c0307c755056761f38a6fdee4

str_test = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

<<<<<<< HEAD
t0 = time.time()
# convert into JSON:
json_test = json.dumps(str_test)
t1 = time.time()
time = t1-t0
print("convert python object to a json string took {}" .format(time))

# # convert into JSON:
# json_test = json.dumps(str_test)
=======
# convert into JSON:
json_test = json.dumps(str_test)
>>>>>>> db40af3c554a604c0307c755056761f38a6fdee4

# insert to DB:
conn = sqlite3.connect('D:\\projects\\ardom-1\\json_to_sql\\testdatabase.db', check_same_thread=False)
cursor = conn.cursor()
table_name = 'test'
cursor.execute("create table if not exists {}(uid text, type text)" .format(table_name))
conn.commit()
cursor.execute("insert into {} values (?, ?)" .format(table_name), ['one', json_test])
conn.commit()
conn.close()