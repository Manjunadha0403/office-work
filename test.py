import csv
list_a = []
list_b = []
file = "PincodeDetails.csv"

# Read the CSV file and store the data in lists
with open(file,'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for index, row in enumerate(reader):
        if index >= 10:
            break
        list_a.append(row[0])
        list_b.append(row[1])
        # x=slice(11)
        # a=list_a[x]
        # b=list_b[x]
       
# Check if list_a is not empty before using it
zip_codes={"pin_code":list_a,
            "city":list_b}
print(zip_codes)