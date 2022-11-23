# When I originally completed this assignment, I did it in Jupyter Notebook but had all my code in a single cell. 
# I eventually realized that this wasn’t optimal and corrected my work accordingly.
# However, I wanted to keep a copy of my original work and decided to save it as a separate python file.


#import libraries and set file path
from pathlib import Path
import csv
csvpath = Path('../Resources/budget_data.csv')

#initialize lists (read below)
pl = []
month = []
delta = []

#open csv file as an object, pass into csv.reader()
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #make each column into a list (month="Date", pl="Profit/losses")
    for column in csvreader:
        pl.append(int(column[1]))
        month.append(str(column[0]))

#calculate the lenght and sum of the pl list        
month_count = len(pl)        
total_pl = sum(pl)

# calculate changes in profit/loss for each month and add to a seperate list (delta)
for i in range(month_count-1):
    delta.append(pl[i+1]-pl[i])
    
#calculate the average of the delta list
avg_change = round(sum(delta)/len(delta), 2)

#calculate the maximum/minimum values in the delta list to find the biggest increase/decrase
biggest_increase = max(delta)
biggest_decrease = min(delta)

#find the indexes of the biggest increase and decrease
bii = delta.index(max(delta))
bdi = delta.index(min(delta))

# find the specific months at the above index (had to add one because it wouldn't work otherwise)
best_month = month[bii+1]
worst_month = month[bdi+1]
        
#print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: {total_pl}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {best_month} $({biggest_increase})")
print(f"Greatest Decrease in Profits: {worst_month} $({biggest_decrease})")

#output Text file with with the results 
output_path = 'output.txt'
with open(output_path, 'w') as csvout:
    csvout.write(f"Financial Analysis\n")
    csvout.write(f"----------------------------\n")
    csvout.write(f"Total Months: {month_count}\n") 
    csvout.write(f"Total: {total_pl}\n")
    csvout.write(f"Average Change: {avg_change}\n")
    csvout.write(f"Greatest Increase in Profits: {best_month} $({biggest_increase})\n")
    csvout.write(f"Greatest Decrease in Profits: {worst_month} $({biggest_decrease})\n")