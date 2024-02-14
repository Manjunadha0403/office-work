source_file_path = 'task2.py'
destination_file_path = 'hehe.txt'

try:
    with open(source_file_path, 'r') as source_file:
        data = source_file.read()

    with open(destination_file_path, 'w') as destination_file:
        destination_file.write(data)
except Exception as e:
    print(f"An error occurred: {e}")