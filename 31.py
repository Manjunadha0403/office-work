import requests
import json
import re

def my_url():
        url = "http://127.0.0.1:8000"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            print("data is read/collect")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
        destination_file_path = 'task.txt'
        try:
            with open(destination_file_path, 'w') as destination_file:
                destination_file.write(data)
                print("Data is write")
        except Exception as e:
            print(f"An error occurred: {e}")
def my_url_data():
    source_file_path = 'task.txt'
    with open(source_file_path, 'r') as source_file:
        data = source_file.read()
    json_data = data
    # Parse JSON
    data_1 = json.loads(json_data)
    # Access elements
    message = data_1["message"]
    # Print the values
    output_text = f"Message: {message}"
    # Write the output to 'out.txt'
    with open('out.txt', 'w') as output_file:
        output_file.write(output_text)
        print("Output written to 'out.txt'")
def my_data():
    with open("out.txt", 'r') as txt_file:
        data_t = txt_file.read()
    # Your text data
    text_data = data_t
    print(text_data)
    # Define a regular expression pattern to match the long_description field
    pattern = r"Message:(.*"")\n"
    print(pattern)
    # Use re.search to find the first match in the text
    match = re.search(pattern, text_data)
    print(match)
    # Extract the value of the long_description field
    if match:
        Message = match.group(0).strip()
        print(f"Description: {Message}")
    else:
        print("Long Msg not found.")

my_url()
my_url_data()
my_data()