# When I originally completed this assignment, I did it in Jupyter Notebook but had all my code in a single cell. 
# I eventually realized that this wasn’t optimal and corrected my work accordingly.
# However, I wanted to keep a copy of my original work and decided to save it as a separate python file.

#import libraries and set file path
from pathlib import Path
import csv

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('../Resources/menu_data.csv')
sales_filepath = Path('../Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=',')
    csv_header1 = next(csvreader1)
    for row in csvreader1:
        menu.append(row)

# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter=',')
    csv_header2 = next(csvreader2)
    for row in csvreader2:
        sales.append(row)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list objecs
for row in sales:
    quantity = int(row[3])
    sales_item = str(row[4])
    if sales_item not in report.keys():
        report[sales_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}
    for row in menu:
        item = str(row[0])
        price = float(row[3])
        cost = int(row[4])
        profit = price - cost
        if sales_item == item:
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity
            report.update()  
    row_count += 1

# Oritional text file output code
# --output had unwanted punctuation--
output_path = 'output.txt'
with open(output_path, "w") as csvout:
    csvwriter = csv.writer(csvout)
    for i in report:
        csvwriter.writerow(
            [
                i, report[i]
            ]
        )