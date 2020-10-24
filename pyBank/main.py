# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# count the rows minus the header for the total number of months
row_count = 0
profit_loss = 0
netchangePnL = 0
current_change = 0
lastPnL = 0
greatest_inc_key = ""
greatest_inc_val = 0
greatest_dec_key = ""
greatest_dec_val = 0
# # Method 1: Plain Reading of CSV files
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next (reader, None)
    for row in reader:
        #make sure row count doesn't include the header
        row_count += 1

#calculate the net total amount of "profit/losses" over the entire period
        key = row[0]
        PnL = float(row[1])
        profit_loss += PnL
#calculate the average of the changes in "profit/losses" over the entire period
        #determine the change and then adding all the changes
        if row_count > 1:
            current_change = PnL-lastPnL
            netchangePnL += current_change
        lastPnL = PnL
#provide the greatest increase in profits (date and amount over the entire period)
        if greatest_inc_val < current_change:
            greatest_inc_val = current_change
            greatest_inc_key = key
#determine the greatest decrease in losses (date and amount) over the entire period
        if greatest_dec_val > current_change:
            greatest_dec_val = current_change
            greatest_dec_key = key
#print the analysis to the terminal and also export to a text file with the results
    mytext = "Financial Analysis\n"
    mytext+= "----------------------------------\n"
    mytext+= f"Total Months: {row_count}\n"
    mytext+= f"Total: {profit_loss:.2f}\n"
    mytext+= f"Average Change: {netchangePnL/(row_count-1):.2f}\n"
    mytext+= f"Greatest Increase in Profits: {greatest_inc_key} (${greatest_inc_val:.2f})\n"
    mytext+= f"Greatest Decrease in Profits: {greatest_dec_key} (${greatest_dec_val:.2f})\n"
    print (mytext)
    #'w' open file and write to it
    textpath = os.path.join('Analysis', 'Financial_Analysis.txt')
    with open (textpath,"w") as txtfile:
        txtfile.write (mytext)
        
    





