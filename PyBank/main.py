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
with open(csvpath, 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    data = list(reader)

changes = []
dates = []
previous_value = int(data[0][1])
for row in data[1:]:
    current_value = int(row[1])
    change = current_value - previous_value
    changes.append(change)
    dates.append(row[0]) 
    previous_value = current_value
average_change = sum(changes) / len(changes)
print(f"Average Change: ${average_change:.2f}")

# Greatest Increase in Profits:
min_change = min(changes)
min_change_index = changes.index(min_change)
min_change_date = dates[min_change_index]

max_change = max(changes)
max_change_index = changes.index(max_change)
max_change_date = dates[max_change_index]

print(f'Greatest Increase in Profit: {max_change_date} (${max_change})')
print(f'Greatest Increase in Profit: {min_change_date} (${min_change})')

# Export analysis results to a text file
folder_path = 'Analysis'
file_name = 'analysis_results.txt'
file_path = os.path.join(folder_path, file_name)
with open(file_path, 'w') as file:
    file.write("Financial Analysis:\n")
    file.write("-----------------\n")
    file.write(f"Total Months: {row_count}\n")
    file.write(f"Average Change: ${average_change:.2f}")
    file.write(f"Greatest Increase in Profit: {max_change_date} (${max_change})")
    file.write(f"Greatest Increase in Profit: {min_change_date} (${min_change})")
print("Analysis results exported to 'analysis_results.txt'.")