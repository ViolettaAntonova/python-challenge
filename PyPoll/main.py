# import module for interactiong with operating system
import os
# import module to work with csv file
import csv

#path for csv file
csvpath = os.path.join('/Users/violettajanuskevica/Desktop/python-challenge/PyPoll/Resources/election_data.csv')
#path where to put results
txtpath = os.path.join('/Users/violettajanuskevica/Desktop/python-challenge/PyPoll/analysis/analysis.txt')

#declaring all variables that I will need
x = 0
winner = 0

#open csv file
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    #skip headers
    csv_header = next(csvfile)
    
    #creating list for row[2] candidate names
    list = [row[2] for row in csv_reader]
    
    #finding the lenght of the list, total votes
    x = len(list)
    
    #creating unique list of candidates
    canditates = [[row,list.count(row)] for row in set(list)]
    
    #loop throught list
    for row in canditates:
        #add percentage
        row.append((row[1] / x) * 100)
        
        #find winner
        if row[1] > winner:
            winner = row[1]
            name = row[0]
 
#print results to terminal
print('Election Results')
print('_'*40)
print(f'Total Votes: {x} ')
print('_'*40)

for candidate in canditates:
  print(f'{candidate[0]}: {round(candidate[2],3)}% ({candidate[1]})')

print('_'*40)
print(f'Winner: {name} ')
print('_'*40)

#write results to txt file
with open(txtpath, "w") as out:
    out.write('Election Results')
    out.write("\n")
    out.write('_'*40)
    out.write("\n")
    out.write(f'Total Votes: {x} ')
    out.write("\n")
    out.write('_'*40)
    out.write("\n")
    for candidate in canditates:
      out.write(f'{candidate[0]}: {round(candidate[2],3)}% ({candidate[1]}) \n')
    out.write("\n")
    out.write('_'*40)
    out.write("\n")
    out.write(f'Winner: {name} ')
    out.write("\n")
    out.write('_'*40)
