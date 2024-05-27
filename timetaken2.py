import os
import re
import csv

# Define the directory path and output CSV file path
directory_path = r'C:\Users\david\OneDrive\Masters\Assignments\Programming Assignment'
output_csv_path = os.path.join(directory_path, 'timetaken.csv')

# Files to exclude
exclude_files = {'timetaken.txt', 'pidata.txt', 'timetaken2.txt'}

# Pattern to match the time taken line
time_pattern = re.compile(r'Time taken to sort the array: ([\d.]+) seconds')

# List to store the results
results = []

# Iterate through all .txt files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt') and filename not in exclude_files:
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            # Search for the time taken line
            match = time_pattern.search(content)
            if match:
                time_taken = match.group(1)
                results.append([filename, time_taken])

# Write the results to a CSV file
with open(output_csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header
    csvwriter.writerow(['Filename', 'Time Taken (seconds)'])
    # Write the data
    csvwriter.writerows(results)

print(f"Results have been written to {output_csv_path}")
