import csv
from collections import defaultdict

# Code for the first CSV file
filename_1 = "clg_details.csv"
fields_1 = ['Clg Name', 'Code', 'City', 'State']

# Code for the second CSV file
filename_2 = "Student_records.csv"
fields_2 = ['Name', 'Branch', 'CGPA', 'City']

# Read and merge data from both CSV files based on the common field
merged_data = defaultdict(dict)

# Read data from the first CSV file
with open(filename_1, 'r') as csvfile1:
    csvreader_1 = csv.DictReader(csvfile1, fieldnames=fields_1)
    next(csvreader_1)  # Skip header row
    for row in csvreader_1:
        city_value = row["City"].lower()
        merged_data[city_value].update(row)

# Read data from the second CSV file and merge it with existing data
with open(filename_2, 'r') as csvfile2:
    csvreader_2 = csv.DictReader(csvfile2, fieldnames=fields_2)
    next(csvreader_2)  # Skip header row
    for row in csvreader_2:
        city_value = row["City"].lower()
        merged_data[city_value].update(row)

# Write the combined data to a new CSV file with ordered columns
combined_filename = "sublet.csv"
combined_fields = ['City', 'Clg Name', 'Code', 'State', 'Name', 'Branch', 'CGPA']  # Add all field names
with open(combined_filename, 'w', newline='') as combined_csvfile:
    csvwriter = csv.DictWriter(combined_csvfile, fieldnames=combined_fields)
    csvwriter.writeheader()
    csvwriter.writerows(merged_data.values())
