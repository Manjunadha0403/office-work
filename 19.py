source_file_path = 'task2.txt'
with open(source_file_path, 'r') as source_file:
    data = source_file.read()

import json

json_data = data
# Parse JSON
data_1 = json.loads(json_data)
# Access elements
status = data_1["status"]
message = data_1["message"]
product_data = data_1["data"]
# Print the values
output_text = f"Status: {status}\nMessage: {message}\nProduct Data:\n"
for key, value in product_data.items():
    output_text += f"{key}:{value}\n"
# Write the output to 'out.txt'
with open('out.txt', 'w') as output_file:
    output_file.write(output_text)
    print("Output written to 'out.txt'")
