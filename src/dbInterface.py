import sqlite3 as sql
from course import Course
from venue import Venue

class dbInterface:
	def __init__(self, name):
		#the next line may be used for testing
		#name = data\schedex.db
		self.__connection = sql.connect(name)
		self.__cursor = self.__connection.cursor()
		
	def close(self):
		self.__connection.close()	
		
	#create methods for the various commands required	
	def getCourses(self):
		courses = []
		self.__cursor.execute('SELECT * FROM Course;')
		data = self.__cursor.fetchall()
		
		for row in data:
			self.__cursor.execute('SELECT COUNT(*) FROM Course WHERE courseCode=?', (row[0],))
			count = self.__cursor.fetchall()
		
			courses.append(Course(row[0], count))
			
		return courses	

	def getVenues(self):
		venues = []
		self.__cursor.execute('SELECT * FROM Venue;')
		data = self.__cursor.fetchall()
		
		for row in data:
			venues.append(Venue(row[1], row[2]))
			
		return venues	

