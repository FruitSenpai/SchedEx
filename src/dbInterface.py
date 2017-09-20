import sqlite3 as sql

def main():
	db = dbInterface("../data/schedex.db")
	db.getDates()

class dbInterface:
	def __init__(self, name):
		#the next line may be used for testing
		#name = data\schedex.db
		self.__connection = sql.connect(name)
		self.__cursor = self.__connection.cursor()
		
	def close(self):
		self.__connection.close()	
		
	#create methods for the various commands required	
	def getDates(self):
		self.__cursor.execute('SELECT * FROM Staff;')
		data = self.__cursor.fetchone()
		print("SQL Version " + str(data[1]))
		
main()		
