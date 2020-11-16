import csv
import os
from collections import Counter
# Define input file & path
filepath = os.path.join('Resources','election_data.csv')
# Read from the input file
with open(filepath, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # Empty list to hold all observations for just candidates
    candidates = [] 

    for row in csvreader:
        candidates.append(row['Candidate'])
        
print("Election Results")
print('--------------------------')
print(f'Total Votes: {len(candidates)}')
print('--------------------------')
 
vote_counter = Counter(candidates)
# print(vote_counter)

# count all the votes grouped by candidates
for key in vote_counter:
    print(f'{key}:{vote_counter[key]/len(candidates)*100: .3f}% ({vote_counter[key]})')
print('--------------------------')        

# variable to compare for maximum vote count
winner_vote_count = 0
# variable to store the name of the winner
Winner = []
# Iterate through each row of vote_counter to find the winner
for vote_count in vote_counter:
    if vote_counter[vote_count] > winner_vote_count:
        # Place the greater value in winner_vote_count
        winner_vote_count = vote_counter[vote_count]
        # Place the key value in Winner
        Winner = vote_count
print(f'Winner: {Winner}')
print('--------------------------')   
# Define output file & path
output_file = os.path.join('analysis','election_data_analysis.txt')

with open(output_file,"w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write('--------------------------')
    file.write("\n")
    file.write(f'Total Votes: {len(candidates)}')
    file.write("\n")
    file.write('--------------------------')
    file.write("\n")
    # Again iterate thorugh vote_counter for writing in the output file, better than hard coding every line
    for key in vote_counter:
        file.write(f'{key}:{vote_counter[key]/len(candidates)*100: .3f}% ({vote_counter[key]})')
        file.write("\n")
    file.write('--------------------------')
    file.write("\n")
    file.write(f'Winner: {Winner}')
    file.write("\n")
    file.write('--------------------------')    