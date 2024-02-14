# Program for taking command-line arguments

import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py <value_a> <value_b>")
    sys.exit(1)

# Extract command-line arguments
user_input1 = sys.argv[1]
user_input2 = sys.argv[2]

# Check if the input is an integer
if user_input1.isdigit() and user_input2.isdigit():
    # Convert inputs to integers
    x = float(user_input1)
    y = float(user_input2)

    # Perform calculations
    z = x + y
    j = y - x

    print(f"Sum: {z}")
    print(f"Difference: {j}")
else:
    print("Invalid data")
