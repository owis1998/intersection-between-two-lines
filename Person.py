class Person:

	__numOfPer = 0
	def __init__(self, name, id):
		self.__name = name 
		self.__id = id
		Person.__numOfPer += 1


	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name

	def getId(self):
		return self.__id

	def setId(self, id):
		self.__id = id

	@staticmethod
	def getNumOfPer():
		return Person.__numOfPer
