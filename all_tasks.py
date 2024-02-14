# mul_str.py
def get_data():
    return "Data from mul_str.py"


# date_cal.py
def get_data():
    return "Data from date_cal.py"


# R_P_S_S_M.py
def get_data():
    return "Data from R_P_S_S_M.py"


# Denominations.py
def get_data():
    return "Data from Denominations.py"


# palindrome.py
def get_data():
    return "Data from palindrome.py"


# num_str.py
def get_data():
    return "Data from num_str.py"


print("""Select option for execute Task
         S. Start 
         E. Exit""")
while True:
    option = input("Enter option (S/E): ")
    operation = option.upper()

    if operation == 'E':
        print("You Choose Option E: ")
        print("Exiting the Game.")
        break

    if operation == "S":
        print("""Select option the option for task
         a.Multiple strings
         b.calander
         c.Rock paper scissors 
         d.Denominations
         e.Palindrome       
         f.Num_string
         g.Quit""")
        option = input("Enter option (a/b/c/d/e/f/g): ")
        operation = option.lower()

        if operation == 'g':
            print("You Choose Option g: ")
            print("Quit the tasks.")
            break

        if operation == "a":
            def access_files():
             file_name= "mul_str.py"
             with open(file_name, 'r') as file:
                 file_content = file.read()
            # Execute the file content in the current namespace
                 exec(file_content, globals())
                 data = get_data()
                 print(f"Data from {file_name}: {data}")
            # Run the function
            access_files()
        if operation == "b":
            def access_files():
                 file_name= "date_cal.py"
                 with open(file_name, 'r') as file:
                   file_content = file.read()
            # Execute the file content in the current namespace
                   exec(file_content, globals())
                   data = get_data()
                   print(f"Data from {file_name}: {data}")
            # Run the function
            access_files()
        if operation == "c":
            def access_files():
                file_name= "R_P_S_S_M.py"
                with open(file_name, 'r') as file:
                  file_content = file.read()
            # Execute the file content in the current namespace
                  exec(file_content, globals())
                  data = get_data()
                  print(f"Data from {file_name}: {data}")
            # Run the function
            access_files()
        if operation == "d":
            def access_files():
                file_name= "Denominations.py"
                with open(file_name, 'r') as file:
                   file_content = file.read()
            # Execute the file content in the current namespace
                   exec(file_content, globals())
                   data = get_data()
                   print(f"Data from {file_name}: {data}")
            # Run the function
            access_files()
        if operation == "e":
            def access_files():
                file_name= "palindrome.py"
                with open(file_name, 'r') as file:
                    file_content = file.read()
            # Execute the file content in the current namespace
                    exec(file_content, globals())

                    data = get_data()
                    print(f"Data from {file_name}: {data}")
            # Run the function
            access_files()
        if operation == "f":
            def access_files():
                file_name= "num_str.py"
                with open(file_name, 'r') as file:
                    file_content = file.read()
            # Execute the file content in the current namespace
                    exec(file_content, globals())

                    data = get_data()
                    print(f"Data from {file_name}: {data}")
            # Run the function
            access_files()