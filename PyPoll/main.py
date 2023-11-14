#Declare variables 
import os
import csv 

candidate_list = {
     "Charles Caspter Stockham":0, 
     "Diana DeGette":0, 
     "Raymon Anthony Doane":0}

votes = 0

#Tie to csv file 
csvpath = os.path.join('Resources''election_data.csv')

#Find total votes cast 
with open(csvpath, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader: 
        votes += 1
        votes_cast=str(row[2])
        
        if 'Charles Caspter Stockham' in votes_cast:
            candidate_list['Charles Caspter Stockham'] += 1 

        elif 'Diana DeGette'in votes_cast: 
            candidate_list['Diana DeGette'] += 1
        
        elif 'Raymon Anthoy Doane' in votes_cast: 
            candidate_list[Raymon Anthony Doane] += 1

    #Percent from total for each candidate 
    



#Find the who won, with greatest total votes 
if total_voteA > total_voteB And 
    total_voteA > total_voteC Then
    winner = 'Charles Caspter Stockham'

if total_voteB > total_voteA And 
    total_voteB > total_voteC Then
    winner = 'Diana DeGette'

if total_voteC > total_voteB And 
    total_voteC > total_vote Then
    winner = 'Raymon Anthony Doane'

#Print results 

