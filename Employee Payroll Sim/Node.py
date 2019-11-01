#Author: Jashanpreet Singh

class Node():#Node class
	#initialize the variables
	def __init__(self,data,next = None):
		self.__data = data
		self.__next = next
	
	#method for string representation of the attributes
	def __str__(self):
		return str(self.__data)
	
	#getter for the attributes
	def getNext(self):
		return self.__next
	def getData(self):
		return self.__data
	
	#setter for the next attribute
	def setNext(self,next):
		self.__next = next
	
    
