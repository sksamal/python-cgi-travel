# -*- coding: utf-8 -*-
#Author :Pasinee Sritragul
# Course: CSCE 101
# Assignment: 4 -Travel Management System, Python Classes
# Date: 19 October 2017
class travelItem :

    def __init__(self, itemID, itemName, itemCount) :
        # Constructor to create inventoryItem
        self.id = itemID
        self.name = itemName
        self.AvailableStart = itemCount
        self.transactions = []
    def getID(self) :
        # getID returns the tour ID
        return(self.id)
    def getName(self) :
        # getName returns the tour name
        return(self.name)
        
    def setName(self, newName) : 
        # setName sets the tour name
        self.name = newName
    def getAvailableStart(self) :
        # returns the starting availability
        return self.AvailableStart 
    def appendTransaction(self, num) :
        self.transactions.append(num)
        # appendTransaction appends a transaction to the transactions list
    
    def getTransactions(self) :
        # getTransactions returns the list of transactions
        return(self.transactions)
    def getReservations(self) :
        # returns the total of reservation transactions
        Reservations = 0
        for num in self.transactions :
            if( num>=0):
                Reservations = Reservations + num
        return Reservations 
        
    def getCancellations(self) :
        # returns the total of cancellation transactions
        Cancellations= 0
        for num in self.transactions :
            if(num<0):
                Cancellations = Cancellations + num
        return Cancellations   
    def getAvailableEnd(self) :
        #availableEnd = 0
        for num in self.transactions :
           #availableEnd = self.getAvailableStart() - self.getReservations() - self.getCancellations()
           return (self.getAvailableStart() - self.getReservations() - self.getCancellations())
        # returns the ending availability, which is availableStart minus transactions
    def printRecord(self) :
        # Prints all attributes
        print("id:", self.id)
        print("name:", self.name)
        print("availableStart:", self.availableStart)
        print("transactions:", self.transactions)

    