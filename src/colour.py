from venue import Venue
import datetime

class Colour:
	def __init__(self, ven, date):
		self.__venue = ven
		self.__date = date
		
	def getVenue(self)	:
		return self.__venue
	
	def getDate(self):
		return self.__date
