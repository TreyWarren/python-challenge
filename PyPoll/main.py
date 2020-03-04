import os
import csv
from collections import Counter

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    next(csvreader)
    
    # Definitions
    candidates = []
    tallies = []
    candidates_list = []
    
    # Read each row of data after the header
    for row in csvreader:
        # Create a list of only the candidate responses as to make things easier to work with
        candidates_list.append(str(row[2]))

# This works similar to unique() but it orders the keys by count
candidates = list(Counter(candidates_list).keys())
# This orders the respective keys' values making it easy to match the array indexes
tallies = list(Counter(candidates_list).values())
# The total number of votes cast
total_votes = len(candidates_list)

# A complete list of candidates who received votes
candidate_1 = candidates[0]
candidate_2 = candidates[1]
candidate_3 = candidates[2]
candidate_4 = candidates[3]

# The total number of votes each candidate won
tally_1 = tallies[0]
tally_2 = tallies[1]
tally_3 = tallies[2]
tally_4 = tallies[3]

# The percentage of votes each candidate won
percent_1 = 100*tallies[0]/total_votes
percent_2 = 100*tallies[1]/total_votes
percent_3 = 100*tallies[2]/total_votes
percent_4 = 100*tallies[3]/total_votes         

# Output:
print('Election Results')
print('-------------------------')
print(f'Total Votes: {len(candidates_list)}')
print('-------------------------')
print(f'{candidate_1}: %{percent_1:.3f} ({tally_1})')
print(f'{candidate_2}: %{percent_2:.3f} ({tally_2})')
print(f'{candidate_3}: %{percent_3:.3f} ({tally_3})')
print(f'{candidate_4}: %{percent_4:.3f} ({tally_4})')
print('-------------------------')
print(f'Winner: {candidate_1}')
print('-------------------------')


# save the output file path
output_path = os.path.join('PyPoll.txt')

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_path, 'w') as output:
    writer = csv.writer(output)
    
    writer.writerow(['Election Results'])
    writer.writerow(['--------------------------------'])
    writer.writerow(['Total Votes:' + '\t' + str(len(candidates_list))])
    writer.writerow(['--------------------------------'])
    writer.writerow([str(candidate_1) + ':' + '\t\t' + '%' + str(round(percent_1,3)) + '\t' + str(tally_1)])
    writer.writerow([str(candidate_2) + ':' + '\t\t' + '%' + str(round(percent_2,3)) + '\t' + str(tally_2)])
    writer.writerow([str(candidate_3) + ':' + '\t\t' + '%' + str(round(percent_3,3)) + '\t' + str(tally_3)])
    writer.writerow([str(candidate_4) + ':' + '\t' + '%' + str(round(percent_4,3)) + '\t' + str(tally_4)])
    writer.writerow(['--------------------------------'])
    writer.writerow(['Winner:' + '\t' + str(candidate_1)])
    writer.writerow(['--------------------------------'])
    
    output.close()