def add(*numbers):
    # Addition operation is performed
    return sum(numbers)

def multiply(x, y):
    # Multiplication operation is performed
    return x * y

def divide(x, y):
    # Division operation is performed
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

while True:
    print("Select Semester:")
    for i in range(1, 9):
        print(f"{i}. Sem {i}")
    print("E. Exit")

    option = input("Enter option (1/2/3/4/5/6/7/8/E): ")

    if option == 'E':
        print("You Choose Option E: ")
        print("Exiting the program.")
        break

    if option in ('1', '2', '3', '4', '5', '6', '7', '8'):
        try:
            # Input for subjects
            subjects = [float(input(f"Enter marks for Subject {i}: ")) for i in range(1, 7)]

            # Input for labs
            labs = [float(input(f"Enter marks for Lab {i}: ")) for i in range(1, 4)]

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue  # This continue statement should be properly indented

        # Perform the specified operations
        total_subjects = add(*subjects)
        total_labs = add(*labs)

        multiplied_subjects = multiply(total_subjects, 3)
        multiplied_labs = multiply(total_labs, 2)

        total_result = add(multiplied_subjects, multiplied_labs)

        # Divide the total result by 24
        final_result = divide(total_result, 24)

        # Display the results
        print(f"The sum of subjects is: {total_subjects}")
        print(f"The sum of labs is: {total_labs}")
        print(f"The multiplied sum of subjects by 3 is: {multiplied_subjects}")
        print(f"The multiplied sum of labs by 2 is: {multiplied_labs}")
        print(f"The total result after adding both is: {total_result}")
        print(f"The final result after dividing by 24 is: {final_result}")
    else:
        print("Invalid option. Please enter a valid option.")
