
from sup_db_1 import *

bool_DEBUG = 0
#init_script_debug(bool_DEBUG, 'https://httpbin.org')
init_script_db(bool_DEBUG, 'https://httpbin.org')
db1 = DbConnection('localhost', 'root', '', 'motors', '', '', '')



db1.dbLogin()
#x = db1.dbLogin()
# print(x)

#y = db1.dbType()
#print(y)


query = ("INSERT INTO motors (name, fab, cil)"
	"VALUES (%s, %s, %s)")
data = ('hyundai1x', 'hyundai', 2)
db1.dbQuery("SHOW TABLES;", "")


#x = ('-b', 4, 'juan')
#db1.dbCondition(x)
#db1.dbClrQuotes(d)

#db1.dbResult(k = 'n')

db1.dbLogout()
