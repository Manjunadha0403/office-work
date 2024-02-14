#Program for 
import  sys
while True:
    user_input1 = input("Enter a value a: ")
    user_input2 = input("Enter a value b: ")

    # Check if the input is an integer
    if user_input1.isdigit() and user_input2.isdigit():
        

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
