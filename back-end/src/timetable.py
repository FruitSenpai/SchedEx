from __future__ import print_function
import datetime
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from dbInterface import dbInterface
from slot import Slot
from colour import Colour
from graphColour import graphColour

def main():
	t = Timetable()
	start = datetime.date(2017, 9, 27)
	end = datetime.date(2017, 9, 29)
	t.createTimetable(start, end)

class Timetable:
	def __init__(self):
		self.__start = None
		self.__end = None
		
			
	def getDates(self, start, end):
		self.__start = start
		self.__end = end
		dates = []
		
		while not start == end:
			if start.weekday() < 5:
				dates.append(datetime.datetime(start.year, start.month, start.day, 9, 0, 0))
				
				dates.append(datetime.datetime(start.year, start.month, start.day, 13, 0, 0))
				
				dates.append(datetime.datetime(start.year, start.month, start.day, 17, 0, 0))
				
			start += datetime.timedelta(days=1)	
			
		return dates
		
	def createTimetable(self, start, end):	
		dates = self.getDates(start, end)
		
		db = dbInterface("../data/schedex.db")
		courses = db.getCourses()
		venues = db.getVenues()
		edges = db.getEdges()
		#print venues[0].getName()
		db.close()
		for e in edges:
			print (e.getCourse1())
			print (e.getCourse2())
			print (e.getWeight())
		colours = self.getColours(venues, dates)
			
		g = graphColour
		

	def createGoogleEvent(self, students):
		SCOPES = 'https://www.googleapis.com/auth/calendar'
		CLIENT_SECRET_FILE = 'client_secret.json'
		APPLICATION_NAME = 'Google Calendar API Python Quickstart'		
		
		credentials = self.get_credentials()
		http = credentials.authorize(httplib2.Http())
		service = discovery.build('calendar', 'v3', http=http)
		
		event = {
		  'summary': 'COMS3002 - Software Engineering',
		  'location': 'Flower Hall',
		  'start': {
			'dateTime': '2017-09-29T09:00:00-07:00',
	#		'timeZone': 'SouthAfrica',
		  },
		  'end': {
			'dateTime': '2017-09-29T12:00:00-07:00',
	#		'timeZone': 'SouthAfrica',
		  },

		  'attendees': [
			{'email': ''}
		  ],
		  'reminders': {
			'useDefault': False,
			'overrides': [
			  {'method': 'email', 'minutes': 24 * 60},
			  {'method': 'popup', 'minutes': 10},
			],
		  },
		}    


		event = service.events().insert(calendarId='primary', body=event).execute()	
		
	def getColours(self, venues, dates):
		colours = []
		for ven in venues:
			for date in dates:
				c = Colour(ven, date)
				colours.append(c)

		return colours	
		
	def get_credentials(self):

		home_dir = os.path.expanduser('~')
		credential_dir = os.path.join(home_dir, '.credentials')
		if not os.path.exists(credential_dir):
		    os.makedirs(credential_dir)
		credential_path = os.path.join(credential_dir,
		                               'calendar-python-quickstart.json')

		store = Storage(credential_path)
		credentials = store.get()
		if not credentials or credentials.invalid:
		    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
		    flow.user_agent = APPLICATION_NAME
		    if flags:
		        credentials = tools.run_flow(flow, store, flags)
		    else: # Needed only for compatibility with Python 2.6
		        credentials = tools.run(flow, store)
		    print('Storing credentials to ' + credential_path)
		return credentials				
		
if __name__ == "__main__":		
	main()		
		
		
