import os
import csv
print("Election Results")
print("----------------------------")
target_column = 'Ballot ID'
column_sum = 0
csvpath = os.path.join('Resources', 'election_data.csv')

# Lists to store data
Ballot_ID = []
County = []
Candidate = {}
Candidate = dict()
Candidate = {"name": "Charles Casper Stockham"}
Candidate["name"] = "Charles Casper Stockham"

Candidate_list = [
    "Charles Casper Stockham",
    "Diana DeGette"
    "Raymon Anthony Doane"]

Candidate["name"] = Candidate_list 
    
# Total Votes
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    row_count = len(list(csv_reader))
    print("Total Votes:", row_count)

print("----------------------------")

# Candidates
import csv
from collections import Counter
data = []
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        data.append(row[2])  # Assuming the data is in the first column
counter = Counter(data)
total_count = sum(counter.values())
percentages = {}
for item, count in counter.items():
    percentage = (count / total_count) * 100
    percentages[item] = (count, round(percentage, 3))
for item, (count, percentage) in percentages.items():
    print(f'{item}:{percentage:.3f}%, ({count})')

print("----------------------------")

# Winner
max_item, (max_count, max_percentage) = max(percentages.items(), key=lambda x: x[1][0])
print(f'Winner: {max_item}')

# Export analysis results to a text file
folder_path = 'Analysis'
file_name = 'analysis_results.txt'
file_path = os.path.join(folder_path, file_name)
with open(file_path, 'w') as file:
    file.write("Analysis Results:\n")
    file.write("-----------------\n")
    file.write(f"Total Votes: {row_count}\n")
    for item, (count, percentage) in percentages.items():
        file.write(f'{item}: {percentage:.3f}%, ({count})\n')
    file.write("-----------------\n")
    file.write(f'Winner: {max_item}\n')

print("Analysis results exported to 'analysis_results.txt'.")



