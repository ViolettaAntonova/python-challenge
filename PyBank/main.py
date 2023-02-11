# import module for interactiong with operating system
import os
# import module to work with csv file
import csv

#path for csv file
csvpath = os.path.join('/Users/violettajanuskevica/Desktop/python-challenge/PyBank/Resources/budget_data.csv')
#path where to put results
txtpath = os.path.join( '/Users/violettajanuskevica/Desktop/python-challenge/PyBank/analysis/analysis.txt')

#declaring all variables that I will need
x = 0
total = 0
change = 0
prev = 0
average = 0
inc = 0
dec = 0
total_change = 0

#open csv file
with open(csvpath, ) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    #skip headers
    csv_header = next(csvfile)
    
    #loop through all file
    for row in csv_reader:
        #finding total of months
        x += 1
        #counting total of Profit/Losses
        total += int(row[1])
        
        #finding change in Profit/Losses over intire period
        change = int(row[1]) - prev
        #skip first value iteration
        if prev == 0:
            change = 0
        #declaring the previous value
        prev = int(row[1])
        #counting total change
        total_change += change
        
        #finding increase
        if change > int(inc):
            inc = change
            monthinc = row[0]

        #finding decrease
        if change < int(dec):
            dec = change
            monthdec = row[0]

    #finding average
    average = total_change / (x - 1)

#print analysis to terminal
print("Financial Analysis")
print("________________________________")
print(f'Total Months: {x} ')
print(f'Total: ${int(total)}')
print(f'Average Change: ${round(average,2)} ')
print(f'Greatest Increase in Profits: {monthinc} (${inc})')
print(f'Greatest Decrease in Profits: {monthdec} (${dec})')

#write results to txt file
with open(txtpath, "w") as out:
    out.write("Financial Analysis")
    out.write("\n")
    out.write("________________________________")
    out.write("\n")
    out.write(f'Total Months: {x}')
    out.write("\n")
    out.write(f'Total: ${int(total)}')
    out.write("\n")
    out.write(f'Average Change: ${round(average,2)}')
    out.write("\n")
    out.write(f'Greatest Increase in Profits: {monthinc} (${inc})')
    out.write("\n")
    out.write(f'Greatest Decrease in Profits: {monthdec} (${dec})')
