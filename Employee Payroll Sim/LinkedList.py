#Author: Jashanpreet Singh

from Node import * #import the node class
class LinkedList(): #Linked List class
    #intialize the variables
    def __init__(self):
        self.__head = None
#*
    #method to append a node to the linked list
    def append(self,data):
        temp1 = Node(data) #get the data to be a node
        #handles if there is nothing in the list
        if self.__head == None:
            self.__head = temp1
        #handles if there are already existing nodes in the linked list
        else:
            temp = self.__head
            while temp.getNext() != None:
                temp = temp.getNext()
            temp.setNext(temp1)
            temp1.setNext(None)
    
    #method to iterate through the items in the linked list
    def __iter__(self):
        current = self.__head
        #goes through the list
        while current is not None:
            yield current.getData() #yields the data in each node
            current = current.getNext() #gets the next node
    #method to search for an Employee id in the linked list
    def searchId(self, id):
        temp = self.__head
        found = False
        #find the id by going through the list
        while temp != None and not found:
            if temp.getData().getID() == id: #allows the id's of each node to be compared
                found = True
            else:
                temp = temp.getNext()
        return found, temp
#*
    #methof to remove a node from the linked list
    def remove(self, item):
        current = self.__head
        previous = None
        found = False
        #finds the item in the list
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        #if the item was in the first node
        if previous == None:
            self.__head = current.getNext()
        #item was somewhere else
        else:
            previous.setNext(current.getNext())
#*
    #method to print the linked list
    def __str__(self):
        temp = self.__head
        returnStr = ''
        count = 0
        while temp != None:
            count += 1
            returnStr += str(count) + '. ' + str(temp.getData()) + '\n'
            temp = temp.getNext()
        return returnStr
        
