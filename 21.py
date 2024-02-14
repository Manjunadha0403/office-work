import re

with open("out.txt", 'r') as txt_file:
    data_t = txt_file.read()

# Your text data
text_data = data_t

# Define a regular expression pattern to match the long_description field
pattern = r"long_description:(.*?)\n"
pattern_1 = r"name:(.*?)\n"
# Use re.search to find the first match in the text
match = re.search(pattern, text_data)
match_1 = re.search(pattern_1,text_data)
# Extract the value of the long_description field
if match_1:
    name = match_1.group(1).strip()
    print(f"Product Name: {name}")
else:
    print("error")
if match:
    long_description = match.group(1).strip()
    print(f"Description: {long_description}")
else:
    print("Long description not found.")
