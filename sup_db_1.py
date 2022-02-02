# ============================================================
# Program:	sup_db_1.py
# Version:	1.1
# Created by: Fernando Figueroa
# Date:	2022-01-26
#
# Main proc.: Library convertion
# Purpose: Library Transference to Python from PHP
#
# Receives:
# Realize:
# Returns:
#============================================================

# Headers and libraries 

from debug_1 import *
import mysql.connector as mysql
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
import numpy as np
from collections import deque

# Init the second cape

def init_script_db(bool_DEBUG, url_from):

	r_server_get = requests.get(url_from)
	file_path = os.path.realpath(__file__)

	# Block direct access

	pattern = "/sup_db/"

	match_pattern_1 = preg.search(pattern, str(r_server_get.headers))
	match_pattern_2 = preg.search(pattern, str(file_path))

	if(match_pattern_2 != None) | (match_pattern_1 != None):
		print("= direct access disabled =")
		sys.exit();

	if(bool_DEBUG == 1):
		shout('p', 'sup_db')
#
# ========================================= [ IMPLEMENTATION ]
#

class DbConnection:

	# --- Properties --- #

	def __init__(self, __DBHOST, __DBUSER, __DBPWD, 
					__DBNAME, __TABLEPREFIX, __db_this, __db_result):

		# Host name
		self.__DBHOST = __DBHOST
		# Db user
		self.__DBUSER = __DBUSER
		# Db password
		self.__DBPWD = __DBPWD
		# Db name
		self.__DBNAME = __DBNAME
		# Tables prefix
		self.__TABLEPREFIX = __TABLEPREFIX
		# Db connection
		self.__db_this = __db_this
		self.__db_result = __db_result

	# --- Methods --- #

    # DB error msgs

	def dbError(self):
		shout('e', Error("There was an error"))


	# DB type

	def dbType(self):
		self.__db_this = self.conex.get_server_info()
		return self.__db_this


	# DB login

	def dbLogin(self):
		global bool_DEBUG
		bool_DEBUG = 1   #____ testing

		if(bool_DEBUG == 0):
			obj_this = [obscure(self.__DBUSER), obscure(self.__DBNAME)]
			conc_obj = "login: ", obj_this[0], " on ", obj_this[1]
			shout('i', conc_obj)

		try:
			self.conex = mysql.connect(host = self.__DBHOST,
                                  database = self.__DBNAME,
                                  user = self.__DBUSER,
                                  password = self.__DBPWD,
                                  charset = 'utf8') # ** checar redundancia

			if self.conex.is_connected():
				__db_info = self.conex.get_server_info()
				#print(__db_info)
				self.conex.set_character_set_name('utf8') # ** checar redundancia
				# y checar parte de SET ... = utf8, al parecer es equivalente
				self.cursor = MySQLCursor(self.conex)
				self.cursor = self.conex.cursor(prepared = True)


			else:
				self.__db_result = self.dbError()
				#shout('e', self.__db_result)
				self.conex.close()
				return self.__db_result


		except Error as err:
			print("Error while connecting to MySQL", err)
			self.__db_result = "Error while connecting: {}".format(err)
			return self.__db_result

		#return self.conex


	#DB query

	def dbQuery(self, str_query, params):
		global bool_DEBUG
		bool_DEBUG = 0 #_____ testing 

		str_query = str_query.strip()

		if(bool_DEBUG == 1):
			shout('q', str_query)

		pattern = "/^SELECT/"
		match_pattern = preg.search(pattern, str_query)
		if(match_pattern != None):
			self.__db_this = self.cursor.execute(str_query, params)

		self.__db_result = self.conex.cmd_query(str_query)
		print(self.__db_result)


	#DB condition
 
	def dbCondition(self, arr_this):
		global bool_DEBUG
		bool_DEBUG = 0 #____ testing
		str_connect = 'AND' if(arr_this[0] == '&&') else 'OR'

		if(isinstance(arr_this[1], list) == True):
			#connect, arrat, array
			self.__db_this = self.dbCondition(arr_this[1]), 
			str_connect, self.dbCondition(arr_this[2])

			return self.__db_this

		elif(np.isscalar(arr_this[1]) == True):
			str_dbfield = arr_this[1]
			str_operator = '='
			arr_elements = []
			pattern = '/^[\W\S]+$/'
			match_pattern = preg.search(pattern, arr_this[2])

			if(match_pattern != None):
				# connect, dbfield, operator, array
				str_operator = arr_this[2]
				poped = arr_this.popleft()

			# else connect, dbfield, array
			for str_itemvalue in arr_this[2]:
				elements = [str_dbfield, str_operator, str_itemvalue]
				arr_elements.append(elements)

			self.__db_result = str_connect, arr_elements
			return self.__db_result

		else:
			return "('error' = 'on dbCondition)"
		

	# DB clear quotes

	def dbClrQuotes(self, arr_data):
		for i in range(0, len(arr_data)):
			arr_data[i] = preg.sub(r'/(\'|\\)/', r'\\1', (arr_data[i]))
			print(arr_data[i])
		return arr_data


	# Recover array | hash with results

	def dbFetch(self, k = 'arr'):
		if(k != 'hash'):
			self.__db_result = self.cursor.fetchone()
			return self.__db_result
		else:
			self.__db_result = self.cursor.fetchall()
			return self.__db_result


	# Recover rows | array of arrays with all result (use carefully! (?))

	def dbResult(self, k = 'all'):
		global bool_DEBUG
		bool_DEBUG = 0 #____ testing
		i = num_rows = self.__db_result
		if(bool_DEBUG == 1):
			db_this = i, "results found"
			shout('', db_this)

		if(k == 'rows'):
			return i

		elif(k == 'free'):
			self.__db_result = self.conex.close()

		elif(i < 500):
			#while(arr_this == self.dbFetch('row')): ## CHECAR SINTAX DEL DE PHP
				#aa_result = arr_this
			#return aa_result if(i != None) else 0
			pass
		
		else:
			return -1

	# DB Logout

	def dbLogout(self):
		global bool_DEBUG
		bool_DEBUG = 0 #____ testing
		if(bool_DEBUG == 1):
			shout('i', "logout")
		return self.conex.close() or self.dbError() #CHECAR implicacion del OR

	# Table prefix

	def dbPrefix(self):
		return self.__TABLEPREFIX
















