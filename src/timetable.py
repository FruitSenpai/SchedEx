class Timetable:
	def __init__(self):
		self.__startDate
		self.__endDate
		
	#receive start and end dates from admin	
	def getDates():
		#check for weekends using a calendar library or something
		#and fill an array with all the possible dates for exams
		#then pull the courses and venues from the db and do graph 
		#colouring on them
		#create array and append each date to it if it's not a 
		#weekend
		
	def createTimetable(self):
		dates = self.getDates()
		
		#instantiate dbInterface class
		#create node array with all course objects pulled from db
		#create edge array between courses weighted by the number of students that take both courses
		#create venue array with all venue objects pulled from db
		#create colour array with all date-venue combinations
		#colour nodes with date-venue combos where the venue capacity >= the course size
		#store course-venue-date combos in timetable table in db
		#create google calendar events etc
		
		
