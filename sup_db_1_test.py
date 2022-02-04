
from sup_db_1 import *

bool_DEBUG = 0
#init_script_debug(bool_DEBUG, 'https://httpbin.org')
init_script_db(bool_DEBUG, 'https://httpbin.org')
db1 = DbConnection('localhost', 'root', '', 'motors', '', '', '')



db1.dbLogin()
#x = db1.dbLogin()
#print(x)

#print(db1.dbType())
#print(y)

#str_query = "INSERT INTO motors (name, fab, cil) VALUES (%s, %s, %s)"
#data_query = "NissanRT", "Nissan", 2

#db1.dbQuery(str_query, data_query)
db1.dbQuery("SELECT name FROM motors")


#cursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("tim", 19))
db1.dbFetch('hash')


print(db1.dbResult('all'))



x = ['juan', 'ddomil', 'yes']
#print(db1.dbCondition(x))
db1.dbClrQuotes(x)



#db1.dbLogout()
