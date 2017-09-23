import datetime
from dbInterface import dbInterface

def main():
	t = Timetable()
	start = datetime.date(2017, 9, 27)
	end = datetime.date(2017, 9, 29)
	t.createTimetable(start, end)

class Timetable:
	def __init__(self):
		self.__start = None
		self.__end = None
		
	#receive start and end dates from admin	
	def getDates(self, start, end):
		self.__start = start
		self.__end = end
		dates = []
		#end = False
		
		while not start == end:
			if start.weekday() < 5:
				dates.append(datetime.datetime(start.year, start.month, start.day, 9, 0, 0))
				
				dates.append(datetime.datetime(start.year, start.month, start.day, 13, 0, 0))
				
				dates.append(datetime.datetime(start.year, start.month, start.day, 17, 0, 0))
				
			start += datetime.timedelta(days=1)	
			
		return dates
		
			
		#check for weekends using a calendar library or something
		#and fill an array with all the possible dates for exams
		#then pull the courses and venues from the db and do graph 
		#colouring on them
		#create array and append each date to it if it's not a 
		#weekend
		
	def createTimetable(self, start, end):
		dates = self.getDates(start, end)
		
		db = dbInterface("../data/schedex.db")
		courses = db.getCourses()
		venues = db.getVenues()
		print venues[0].getName()
		db.close()
		#instantiate dbInterface class
		#create node array with all course objects pulled from db
		#create edge array between courses weighted by the number of students that take both courses
		#create venue array with all venue objects pulled from db
		#create colour array with all date-venue combinations
		#colour nodes with date-venue combos where the venue capacity >= the course size
		#store course-venue-date combos in timetable table in db
		#create google calendar events etc
		
main()		
		
		
