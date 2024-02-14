while True:
    variable1 = input("Enter the first variable name: ")
    user_input1 = input("Enter a value : ")

    variable2 = input("Enter the second variable name: ")
    user_input2 = input("Enter a value : ")

    # Check if the input is an integer
    if variable1.isalpha() and variable2.isalpha() and user_input1.isdigit() and user_input2.isdigit():
    # Check if the inputs  are integer & alphabetical
        

        # Convert inputs to integers
        x = int(user_input1)
        y = int(user_input2)

        # Perform calculations
        z = x + y
        j = y - x

        print(f"Sum: {z}")
        print(f"Difference: {j}")
    else:
        print("Invalid data")
        break