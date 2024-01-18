import os
import csv
print("Financial Analysis")
print("----------------------------")
csvpath = os.path.join('Resources', 'budget_data.csv')

# Define variables 
target_column = 'Profit/Losses'
column_sum = 0

# Total Month 
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    row_count = len(list(csv_reader))
    print("Total Months:", row_count)


# Total Profit
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    target_column_index = headers.index(target_column)
    for row in csvreader:
        column_sum += float(row[target_column_index])
        
print(f'Sum of: ${column_sum}')

# Average Change
data = []
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  
    for row in csv_reader:
        data.append(float(row[1]))  

changes = []
for i in range(1, len(data)):
    change = data[i] - data[i-1]
    changes.append(change)

average_change = sum(changes) / len(changes)
print(f"Average Change: ${average_change:.2f}")

max_change = max(changes)
min_change = min(changes)

max_change_index = changes.index(max_change)
min_change_index = changes.index(min_change)

data_with_cells = []
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  
    for row in csv_reader:
        data_with_cells.append(dict(zip(header, row)))

print("Greatest Increase in Profits:")
for key, value in data_with_cells[max_change_index].items():
    print(f"{key}: {value}")

print("\nGreatest Decrease in Profits:")
for key, value in data_with_cells[min_change_index].items():
    print(f"{key}: {value}")

# Greatest Increase in Profits
max_change = max(changes)
min_change = min(changes) 