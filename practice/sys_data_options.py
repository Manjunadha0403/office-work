import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 4:
    print("Usage: python script.py <value_a> <value_b> <operation_choice>")
    sys.exit(1)

# Extract command-line arguments and convert to the required types
try:
    user_input1 = float(sys.argv[1])
    user_input2 = float(sys.argv[2])
except ValueError:
    print("Invalid input for <value_a> or <value_b>. They should be numeric.")
    sys.exit(1)

user_input3 = str(sys.argv[3])

# Check if user_input3 is a valid option
valid_options = ('A', 'B', 'C', 'D', 'E')
if user_input3 in valid_options:
    # Arithmetic operations
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"

    # Main program
    while True:
        print("Select operation:")
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Exit")

        option = input(f"Enter your choice for {user_input3}: ")

        if option == 'E':
            print("You chose option E.")
            print("Exiting the program.")
            break

        if option in valid_options:
            try:
                result = 0
                if option == 'A':
                    result = add(user_input1, user_input2)
                elif option == 'B':
                    result = subtract(user_input1, user_input2)
                elif option == 'C':
                    result = multiply(user_input1, user_input2)
                elif option == 'D':
                    result = divide(user_input1, user_input2)
                print(f"Result: {result}")
                exit()
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        else:
            print("Invalid input. Please enter a valid option (A, B, C, D, or E).")
else:
    print("Invalid input for <operation_choice>. It should be A, B, C, D, or E.")
