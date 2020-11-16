import os

import csv
# Define input file & path
csvpath = os.path.join('Resources','budget_data.csv')
# Empty list to hold all observations (dictionaries) for the whole dataset
data = []
# Read from the input file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Get the column header from the first row
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        data.append({
            csv_header[0]: row[0],
            csv_header[1]: int(row[1])
        })
        
# Print the whole list to check       
# print(data)

#Formatting
print("------------------")
print("Financial Analysis")
print("------------------")

# Pring the total number of months included in the dataset
print(f"Total months: {len(data)}")

# Calculating the total amount of profit/loss
total = 0
for date_row in data:
    total += date_row['Profit/Losses']
print(f"Total: {total}")

# Initialize variable to store the total change in profit/loss
pl_change_total = 0
# Add another key to store variance on the first row
data[0]['Differences'] = 0
#staring for loop from the second row to calculate difference between n th and (n-1)th observations
for x in range(1,len(data)):
    diff = data[x]['Profit/Losses'] - data[x-1]['Profit/Losses']
    # store the variance
    data[x]['Differences'] = diff
    # Add up all the variances
    pl_change_total += diff

# Changes happening across n-1 iterations
delta = pl_change_total / (len(data) - 1)
print(f"Average Change:  ${round(delta, 2)}")

# Print the whole list to check
# print(data)

# The greatest increase & decrease in profits (date and amount) over the entire period
min = data[0]['Profit/Losses']
min_date = data[0]['Date']
max = data[0]['Profit/Losses']
max_date = data[0]['Date']

for every_row in data:
    if every_row['Differences'] > max:
        max = every_row['Differences'] 
        max_date = every_row['Date']
    if every_row['Differences'] < min:
        min = every_row['Differences'] 
        min_date = every_row['Date']

print(f"Greatest Increase in Profits: {max_date} (${max})")
print(f"Greatest Decrease in Profits: {min_date} (${min})")

# export a text file with the results
# Define output file & path
output_file = os.path.join('analysis','budget_data_analysis.txt')
with open(output_file,"w") as file: 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(data)}")
    file.write("\n")
    file.write(f"Total: ${total}")
    file.write("\n")
    file.write(f"Average Change: {round(delta, 2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_date} (${(str(max))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {min_date} (${(str(min))})")