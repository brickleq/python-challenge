# Brickey LeQuire
# Homework Assignment #3, Part 2: PyPoll

import os # file management
import csv # csv read/write

voter_id = [] # Voter ID (column 1)
county = [] # County (column 2)
vote = [] # Candidate voter selected (column 3)
mydict = {} # dictionary to hold candidate names and total votes each received
max_votes = 0 # greatest number of votes received by any one candidate

csv_path = os.path.join('Resources/election_data.csv') # open CSV file and assign it a variable
with open(csv_path, 'r', newline='') as csvfile: # open the file
    csvreader = csv.reader(csvfile, delimiter=',') # tell Python how to read the file
    csv_header = next(csvreader) # get column headers from first row (skips data import for header row)
    for row in csvreader: # loop through all subsequent rows
        voter_id.append(row[0]) # retrieve each voter's voter ID number
        county.append(row[1]) # retrieve each voter's county of residence
        vote.append(row[2]) # retrieve each voter's choice of candidate
        candidate = row[2] # candidate voted for in this row
        if candidate in mydict.keys(): # if candidate's name is already in dictionary...
            mydict[candidate] +=1 # increase that candidate's vote tally by 1
        else: # otherwise...
            mydict[candidate] = 1 # set that candidate's vote tally to 1
        if mydict[candidate] > max_votes: # if candidate's vote tally > than current value of max_votes...
            max_votes = mydict[candidate] # set max_votes to equal votes received by this candidate
            winner = candidate # set winner to candidate's name
votes_cast=(len(vote)) #  The total number of votes cast

# output results to text file, screen

text_file = open("PyPoll_output_PBL.txt", "w") # create text file in same folder as main.py, assign variable to path
print('Election Results')
text_file.write('Election Results')
print('-------------------------')
text_file.write('-------------------------')
print('Total Votes: ' + str(votes_cast))
text_file.write('Total Votes: ' + str(votes_cast))
print('-------------------------')
text_file.write('-------------------------')
for i in mydict: # loop through dictionary
    candidate_name = str(i) # get candidate names
    votes_received = str(mydict[i]) # get number of votes candidate received
    percentage = mydict[i]/votes_cast*100 # divide by total votes cast, multiply by 100 to get percentage
    percentage_string = str('{:,.2f}'.format(percentage)) # format percentage with 2 places after decimal
    print(candidate_name + ' : ' + votes_received + ' ' + '(' + percentage_string + '%)')
    text_file.write(candidate_name + ' : ' + votes_received + ' ' + '(' + percentage_string + '%)')
print('-------------------------')
text_file.write('-------------------------')
print('Winner: ' + winner)
text_file.write('Winner: ' + winner)
print('-------------------------')
text_file.write('-------------------------')
text_file.close() # if you open it, close it