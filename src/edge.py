class Edge():
	def __init__(self, c1, c2, w):
		self.__course1 = c1	
		self.__course2 = c2
		self.__weight = w
		
	def	getCourse1(self):
		return self.__course1
		
	def	getCourse2(self):
		return self.__course2
	
	def	getWeight(self):
		return self.__weight		
