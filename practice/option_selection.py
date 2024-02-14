"""Programe for Arthamatic Operations for Two numbers"""
def add(x, y):
    #addition operation is perform
    return x + y

def subtract(x, y):
    #Subtraction operation is perform
    return x - y

def multiply(x, y):
    #Multiplication operation is perform
    return x * y

def divide(x, y):
    # Division operation is perform
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
    # Some times Result is Zero
while True:
    print("""Select operation:
          A. Addition
          B. Subtraction
          C. Multiplication
          D. Division
          E. Exit""")

    option = input("Enter option (A/B/C/D/E): ").upper()
    #select the option for  Arthamatic operation
    if option in ('A', 'B', 'C', 'D','E'):
        if option == 'E':
            print("You Choose Option E: ")
            print("Exiting the program.")
            break
        try:
            num_x = float(input("Enter first number x: "))
            num_y = float(input("Enter second number y: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        if option == 'A':
            x = num_x+num_y
            print(f"The Addition given numbers  is :{x} ")
        elif option == 'B':
            x = num_x-num_y
            print(f"The  Subtraction of given numbers is :{x} ")
        elif option == 'C':
            x = num_x*num_y
            print(f"The Multiplication of given numbers is :{x} ")

        elif option == 'D':
            x = num_x/num_y
            print(f"The Division of given numbers is :{x} ")
    else:
        print("Sorry you select a Invalid Input and please Try A,B,C,D,E,")