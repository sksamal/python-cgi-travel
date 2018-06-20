#!/usr/bin/python3
from travelToolbox import readItems, readTransactions
from travelClass import travelItem
import cgi
data = cgi.FieldStorage()
ID = data.getvalue('ID')
itemsFileName = "items4.csv"
transactionsFileName = "transactions4.csv"

itemRecords = {}
# itemRecords is a dictionary of travelItem records indexed by item ID
readItems(itemsFileName, itemRecords)

# Read the transactions from transactionsFileName into itemRecords
readTransactions(transactionsFileName, itemRecords)

Name = ""
Start = "" 
End = "" 
for rec in itemRecords :
  if int(itemRecords[rec].getID()) == int(ID):
    Name = itemRecords[rec].getName()
    Start = itemRecords[rec].getAvailableStart()	
    End = itemRecords[rec].getAvailableEnd()	
#
# To be written
print('Content-type:text/html\r\n\r\n')
print('<!DOCTYPE HTML>')
print('<html>')
print('<head>')
print('<meta charset="UTF-8">')
print('<title>Travel</title>')
print('</head>')
print('<body>')
print('<h1>', ID, '</h1>')
print('<h1> Name:', Name, '</h1>')
print('<h1> Start:', Start, '</h1>')
print('<h1> End:', End, '</h1>')
print('</body>')
print('</html>')
