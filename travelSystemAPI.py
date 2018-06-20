# -*- coding: utf-8 -*-
from travelToolboxAPI import readItems, printItems, readTransactions, printSummary
from travelPlot import plotTravel
itemsFileName = "items4.csv"
transactionsFileName = "transactions4.csv"

# itemRecords is a dictionary of travelItem records indexed by item ID
itemRecords = {}

# Read the items from itemsFileName into itemRecords
readItems(itemsFileName, itemRecords)

# Print out the list of items from itemRecords
printItems(itemRecords)

# Read the transactions from transactionsFileName into itemRecords
readTransactions(transactionsFileName, itemRecords)

# Print the summary for each item from itemRecords
printSummary(itemRecords)
# Plot the travel for each item from itemRecords 
plotTravel(itemRecords)