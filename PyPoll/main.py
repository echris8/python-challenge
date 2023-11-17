#Declare variables 
import os
import csv 

total_votes = 0
votes = []
tallies = []
winner = ""
most = 0

#Tie to csv file 
input_path = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")

#Find total votes cast 
with open(input_path, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    csv_list = list(csvreader)

votes = [row[2] for row in csv_list]
total_votes = len(votes)
names = []

#Find unique names 
for name in votes: 
    if name not in names:   
        names.append(name)
        tallies.append(0) 

#Find number of votes for each unique name 
for vote in votes: 
    for i, name in enumerate(names):
        if vote == name: 
            tallies[i] += 1 

#Find who received the most votes
for i, name in enumerate(names): 

    most = max(tallies)

for i, vote in enumerate(tallies): 
    if vote == most: 
        winner = names [i]      

# #Identify file to write to 
output_path = os.path.join(os.path.dirname(__file__), "analysis.md")

#print(winner, most)
with open(output_path, "w") as md_file:
    md_file.write(f"Election Results\n")
    md_file.write("-" * 40 + "\n")
    md_file.write(f"Total Votes:  {total_votes}\n")
    md_file.write("-" * 40 + "\n")
    for i, name in enumerate(names):
        md_file.write(f"{name}: {((tallies[i]/total_votes)*100):.3f}%   ({tallies[i]})\n")
    md_file.write("-" * 40 + "\n")
    md_file.write(f"Winner: {winner}\n")
    md_file.write("-" * 40 + "\n")

#Print results 
print(f"Results written to {output_path}") 

