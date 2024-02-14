"""Python program for Find string data like [A-Z] and[a-z] in a group of data"""
#*************INPUT Section*****************#
# Prompt the user to get  the data from file
source_file = 'clgs_pro.csv'
with open(source_file, 'r') as source_file:
        data = source_file.read()
x = data
# Lists to store different types of characters
uppercase_list = []
lowercase_list = []
mixedcase_list = []
numeric_data = []
numaric_data_other = []
special_characters_data = []
special_characters_data_other = []

# Check the type of input data
if x.isalpha():
    print(f"The given is purely alphabetic: {x}")
elif x.isalnum():
    print(f"The given data is a combination of Alphabetic and Numeric: {x}")
elif x.isprintable():
    print(f"The given data is a combination of Alphabetic, Numeric, and special characters: {x}")
else:
    print(f"The is also take _space_ as charater:{x}")

#********************Main Section*************************#
# Split the input into a list of words and sort them
a = x.split()
a.sort()
print("Data in sorted order:", a)

# Iterate through each character in the sorted list
for char in a:
    if char.isalpha():
# Check and categorize alphabetic characters
        if char.isupper():
            uppercase_list.append(char)
        elif char.islower():
            lowercase_list.append(char)
        else:
            mixedcase_list.append(char)
    elif char.isnumeric():
# Check and categorize numeric characters
        numeric_data.append(char)
    elif char.isalnum():
# Check and categorize alphanumeric characters
        numaric_data_other.append(char)
    else:
# Check and categorize special characters
        special_characters_data.append(char)

print(f"Uppercase words: {uppercase_list}")
print(f"Lowercase words: {lowercase_list}")
print(f"Mixed-case words: {mixedcase_list}")
print(f"Numeric values: {numeric_data}")

try:
# Handle errors when checking numeric data
    for char in numeric_data:
        if not char.isnumeric():
            numaric_data_other.append(char)
except:
    print("Error")

print(f"Numeric values with additional data: {numaric_data_other}")

print(f"Special characters: {special_characters_data}")

#*********************output Section **************************#
# Convert lists to tuples
alpha_tuple_U = tuple(uppercase_list)
alpha_tuple_l = tuple(lowercase_list)
alpha_tuple_m = tuple(mixedcase_list)
numaric_tuple_N = tuple(numeric_data)
numaric_tuple_NN = tuple(numaric_data_other)
special_tuple_U = tuple(special_characters_data)

# Join tuples into strings
alpha_u = "*".join(alpha_tuple_U)
alpha_l = "**".join(alpha_tuple_l)
alpha_m = "***".join(alpha_tuple_m)

numa_n = "*@".join(numaric_tuple_N)
numa_n_o = "**@".join(numaric_tuple_NN)

spcl = "and".join(special_tuple_U)

# Print the results with messages describing operations
print(f"Uppercase characters joined with '*': {alpha_u}")
print(f"Lowercase characters joined with '**': {alpha_l}")
print(f"Mixed-case characters joined with '***': {alpha_m}")
print(f"Numeric values joined with '*@': {numa_n}")
print(f"Numeric values with additional data joined with '**@': {numa_n_o}")
print(f"Special characters joined with 'and': {spcl}")
