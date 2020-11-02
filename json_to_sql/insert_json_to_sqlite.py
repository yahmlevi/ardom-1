import json
import sqlite3

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

# convert into JSON:
json_test = json.dumps(str_test)

# insert to DB:
conn = sqlite3.connect('D:\\projects\\ardom-1\\json_to_sql\\testdatabase.db', check_same_thread=False)
cursor = conn.cursor()
table_name = 'test'
cursor.execute("create table if not exists {}(uid text, type text)" .format(table_name))
conn.commit()
cursor.execute("insert into {} values (?, ?)" .format(table_name), ['one', json_test])
conn.commit()
conn.close()