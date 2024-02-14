# Python program for finding string data like [A-Z] and [a-z] in a group of data
# Input Section
x = input("Enter The Data:")
        
# Lists to store different types of characters
uppercase_list = []
lowercase_list = []
mixedcase_list = []
numeric_data = []
numaric_data_other = []
special_characters_data = []

# Split the input into a list of words and sort them
input_list = x.split()
# Iterate through each character in the sorted list
for char in input_list:
    if char.isalpha():
                # Check and categorize alphabetic characters
        if char.isupper():
            uppercase_list.append(char)
        elif char.islower():
            lowercase_list.append(char)
        else:
            mixedcase_list.append(char) 

    elif char.isnumeric():
            numeric_data.append(char)               # Check and categorize numeric characters
            
    elif char.isalnum():
            numaric_data_other.append(char)         # Check and categorize alphanumeric characters
                
    else:
            special_characters_data.append(char)    # Check and categorize special characters
            
print(f"""
        Uppercase words: {uppercase_list}
        Lowercase words: {lowercase_list}
        Mixed-case words: {mixedcase_list}
        Numeric values: {numeric_data}
        Numeric_other_values{numaric_data_other}
        Special Characters{special_characters_data}""")

result_list = []

for words in input_list:
    if len(words) > 2:#word length
        new_word = words[0] + '*' * (len(words) - 2) + words[-1] 
#"""when word length is more then 2 starting and end letter  only is present remaing replace with * """
        result_list.append(new_word)
    else:
        result_list.append(words)
        
print(input_list)#original data
print(result_list)#after Execute