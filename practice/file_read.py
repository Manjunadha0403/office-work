# Open the file in read mode
file_path = 'hehe.txt'  #Assigin the file path to variable
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_content = file.read()
    # Process the information
    # let's print the content ssof the file
    print("File Content:")
    print(file_content)

# The file will be automatically closed when you exit the 'with' block

