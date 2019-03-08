# Homework Assignment #3, Part 1: PyBank
# Brickey LeQuire 

#Import modules:
import os # file management
import csv # CSV read/write
import statistics # lies, damned lies, etc.

csvpath = os.path.join('Resources','budget_data.csv')

date = [] # month-year
pl = [] # monthly profit/loss for month in current row
pl_total = 0 # sum of all monthly profits/losses
pl_change = 0 # difference between current and previous monthly profit/loss
pl_change_list = [] # list of all pl_change values
pl_prev_row = 0 # profit/loss for month in previous row
months_total = 0 # total months in CSV data
avg_change = 0 # arithmetic mean of all pl_change values
max_increase = 0 # greatest month-to-month increase, in $
max_decrease = 0 # greatest month-t0-month decrease, in $
max_increase_month = () # month and year of max_increase
max_decrease_month = () # month and year of max_decrease
first_loop = True 


with open(csvpath, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #skip header row
    for row in csvreader:
        date.append(row[0]) #populate list of dates
        pl.append(row[1]) #populate list of profits/losses
        if first_loop == False:
            pl_change = float(row[1]) - pl_prev_row
            pl_change_list.append(pl_change)
        pl_total = pl_total + float(row[1]) #keep running total of net profits/losses
        pl_prev_row = float(row[1])
        if first_loop == True:
            first_loop = False

months_total=len(date) #number of months in CSV file
avg_change = statistics.mean(pl_change_list)
max_increase = max(pl_change_list)
max_decrease = min(pl_change_list)
max_increase_index = pl_change_list.index(max_increase)
max_decrease_index = pl_change_list.index(max_decrease)
max_increase_month = date[(max_increase_index+1)]
max_decrease_month = date[(max_decrease_index+1)]



# print(pl_change_list)

print()
print('Financial Analysis')
print('----------------------------')
print('Total Months: '+str(months_total))
print('Total: $'+'{:,.2f}'.format(pl_total))
print('Average Change: $'+'{:,.2f}'.format(avg_change))

print('Greatest Increase in Profits: $'+'{:,.2f}'.format(max_increase)+' ('+max_increase_month+')')
print('Greatest Decrease in Profits: $'+'{:,.2f}'.format(max_decrease)+' ('+max_decrease_month+')') 




