# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

import os
print(os.getcwd())

# Import libraries
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menuFilePath = 'C:/Users/jan/Desktop/FinTech/Module2Challenge/PyRamen/Resources/menu_data.csv'
salesFilePath = 'C:/Users/jan/Desktop/FinTech/Module2Challenge/PyRamen/Resources/sales_data.csv'

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Read in the menu data into the menu list
with open(menuFilePath, 'r') as file:
    csvReader = csv.reader(file)
    next(csvReader)  # Skip the header
    for row in csvReader:
        menu.append(row)

# Read in the sales data into the sales list
with open(salesFilePath, 'r') as file:
    csvReader = csv.reader(file)
    next(csvReader)  # Skip the header
    for row in csvReader:
        sales.append(row)

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
rowCount = 0

# Loop over every row in the sales list
for sale in sales:
    # Line_Item_ID, Date, Credit_Card_Number, Quantity, Menu_Item
    # Initialize sales data variables
    quantity = int(sale[3])
    salesItem = sale[4]

    # If the item value not in the report, add it as a new entry with initialized metrics
    if salesItem not in report:
        report[salesItem] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}

    # For every row in our sales data, loop over the menu records to determine a match
    for item in menu:
        # Item, Category, Description, Price, Cost
        # Initialize menu data variables
        menuItem = item[0]
        price = float(item[3])
        cost = float(item[4])

        # Calculate profit of each item in the menu data
        profit = price - cost

        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if salesItem == menuItem:
            report[salesItem]["01-count"] += quantity
            report[salesItem]["02-revenue"] += price * quantity
            report[salesItem]["03-cogs"] += cost * quantity
            report[salesItem]["04-profit"] += profit * quantity

    # Increment the row counter by 1
    rowCount += 1

# Print total number of records in sales data
print(f"Total number of records in sales data: {rowCount}")

# Write out report to a text file
with open('report.txt', 'w') as file:
    for key, value in report.items():
        file.write(f"{key} {value}\n")