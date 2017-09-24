class graph(object):	
	
	__N = 0 #No of nodes
	__adj =[[]] #Adjacency List

	def __init__(self, n):
		self.__N = n
		self.__adj = [[] for x in range(self.__N)]
	
	def addEdge(self, n, w):
		self.__adj[n].append(w)
		self.__adj[w].append(n)
		
	def greedyColouring(self):
		result = [-1 for x in range(self.__N)] #No colour set
		result[0] = 0 #First node colour set
		print result
		
		#List storing available colours
	 	coloured = [False for x in range(self.__N)]
		
		#Assigns Colours
		for i in range(self.__N):
			for j in self.__adj[i]:
				if(result[j] != -1):
					coloured[result[j]] = True
		
			#Find first Available colour
			cr = 0
			for cr in range(self.__N):
				if(coloured[cr] == False):
					break
			result[i] = cr
			
			for j in self.__adj[i]:
				if(result[j] != -1):
					coloured[result[j]] = False		
		
		for i in range (self.__N):
			print ("Node ",i," --> Colour ", result[i])
