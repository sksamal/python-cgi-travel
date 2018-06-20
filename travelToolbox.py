# -*- coding: utf-8 -*-
#Author :Pasinee Sritragul
# Course: CSCE 101
# Assignment: 4 -Travel Management System, Python Classes
# Date: 19 October 2017
import csv
from travelClass import travelItem

def readItems(itemsFileName, itemRecords) :
    # readItems reads items from itemsFileName into the itemRecords dictionary

    # Open itemsFileName and create a CSV file reader
    itemsFile = open(itemsFileName, 'r')
    itemsReader = csv.reader(itemsFile)

    # Process each row of the items file
    for row in itemsReader :
        # Get the values for the record
        (iid, iname, icount) = row
        iid = str(iid)
        iname = str(iname)
        icount = int(icount)
   
        # Check if this ID is not yet in itemRecords
        if (not(iid in itemRecords)) :
            # Create a travelItem object and add it to itemRecords
            itemRecord = travelItem(iid, iname, icount)
            itemRecords[iid] = itemRecord

def printItems(itemRecords) :
    # printItems prints the list of items from the itemRecords dictionary

    # Print the header
    print("ID     NAME")
    print("-----  ------------")
    # For each item record in itemRecords
    for rec in itemRecords.values() :
        # Print the item ID and name
        print("{0:5s}  {1:12s}".format(rec.getID(), rec.getName()))
    # Print the footer
    print()

def readTransactions(transactionsFileName, itemRecords) :
    # readTransactions reads transactions from transactionsFileName into the itemRecords dictionary
   
    transactionsFile = open(transactionsFileName, 'r')
    itemsReader = csv.reader(transactionsFile)

    # Process each row of the items file
    for row in itemsReader :
        # Get the values for the record
        (iid, icount) = row
        iid = str(iid)
        icount = int(icount)
   
   # Check if this ID is not yet in itemRecords
        if ((iid in itemRecords)) :
            itemRecords[iid].appendTransaction(icount)
            # Create a travelItem object and add it to itemRecords
            
           
def printSummary(itemRecords) :
    # printSummary prints a summary from the itemRecords dictionary
    print("Tours")
    print("=====")
    print("ID     NAME           START RESV.  CANCL.  END")
    print("-----  ------------   ----- ------ ---- ----")
    # For each item record in itemRecords
    for rec in itemRecords :
        # Print the item ID and name
        print("{0:5s}  {1:12s} {2:6} {3:6} {4:6} {5:6}".format(itemRecords[rec].getID(),itemRecords[rec].getName(),itemRecords[rec].getAvailableStart(),itemRecords[rec].getReservations(),itemRecords[rec].getCancellations(),itemRecords[rec].getAvailableEnd() ))
        # Print the footer
