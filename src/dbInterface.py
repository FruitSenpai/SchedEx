import sqlite3 as sql
from course import Course
from venue import Venue
from edge import Edge

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
			self.__cursor.execute('SELECT COUNT(*) FROM Registration WHERE courseCode=?', (row[0],))
			count = self.__cursor.fetchall()
		
			courses.append(Course(row[0], count))
			
		return courses	
		
	def getEdges(self):
		courses = self.getCourses()
		edges = []
		length = len(courses)
		
		for i in range(length):
			for j in range(i+1, length):
				self.__cursor.execute('SELECT DISTINCT COUNT(*) FROM Registration WHERE courseCode=? OR courseCode=?;', (courses[i].getCode(), courses[j].getCode(),))	
				
				data = self.__cursor.fetchall()
				if data[0] != 0:
					edges.append(Edge(courses[i].getCode(), courses[j].getCode(), ((data[0][0])/2)))
					
		return edges			

	def getVenues(self):
		venues = []
		self.__cursor.execute('SELECT * FROM Venue;')
		data = self.__cursor.fetchall()
		
		for row in data:
			venues.append(Venue(row[1], row[2]))
			
		return venues	

