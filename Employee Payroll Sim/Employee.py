#Author: Jashanpreet Singh
class Employee(): #employee class
    def __init__(self, ID = '', hours = 0.0, pay = 0.0, wage = 0.0):
    #initialize the attributes
        self.__ID = ID
        self.__hours = hours
        self.__pay = pay
        self.__wage = wage

    #setter for the attributes
    def setID(self, option):
        self.__ID = option
    def setHours(self, option):
        self.__hours = option
    def setPay(self, option):
        self.__pay = option
    def setWage(self,option):
        self.__wage = option
        
    #getter for the attributes
    def getID(self):
        return self.__ID
    def getHours(self):
        return self.__hours
    def getPay(self):
        return self.__pay
    def getWage(self):
        return self.__wage

    #method to print the attributes
    def __str__(self):
        return 'Employee ID: ' + str(self.getID()) + '\n' + 'Hours Worked: ' + str(self.getHours()) + '\n' + 'Hourly Pay: ' + str(self.getPay()) + '\n' +'Gross Wages: ' + str(self.getWage()) + '\n'
    
