import sqlite3 as sql

class dbInterface:
	def __init__(self):
		self.__connection = None
		self.__cursor = None
	
	#initialise db connection
	def connect(self, name):
		#the next line may be used for testing
		#name = data\schedex.db
		self.__connection = sql.connect(name)
		self.__cursor = connection.cursor()
		
	def close(self):
		self.__connection.close()	
		
	#create methods for the various commands required	
	
