import datetime
from dbInterface import dbInterface
from slot import Slot

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
		
			
		#check for weekends using a calendar library or something
		#and fill an array with all the possible dates for exams
		#then pull the courses and venues from the db and do graph 
		#colouring on them
		#create array and append each date to it if it's not a 
		#weekend
		
	#receive start and end dates from admin	
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
		
		#each time node is coloured, instantiate a slot
		#create an event with an attendees list of all the students who take that course
		#insert the slot into the timetable table
		
		credentials = self.get_credentials()
		http = credentials.authorize(httplib2.Http())
		service = discovery.build('calendar', 'v3', http=http)
		
		event = {
		  'summary': 'Google I/O 2017',
		  'location': '800 Howard St., San Francisco, CA 94103',
		  'description': 'A chance to hear more about Google\'s developer products.',
		  'start': {
			'dateTime': '2017-09-28T09:00:00-07:00',
	#		'timeZone': 'SouthAfrica',
		  },
		  'end': {
			'dateTime': '2017-09-28T12:00:00-07:00',
	#		'timeZone': 'SouthAfrica',
		  },
		  #can pull list of students for each course from db and add them to attendees list
		  'attendees': [
			{'email': 'parryjas@gmail.com'}
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
		
def get_credentials(self):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
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
		
main()		
		
		
