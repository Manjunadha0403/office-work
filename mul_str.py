# Python program for finding string data like [A-Z] and [a-z] in a group of data

# *************INPUT Section*****************#

print("""Select option 
         S. Start 
         E. Exit""")

while True:
    option = input("Enter option (S/E): ")
    operation = option.upper()

    if operation == 'E':
        print("You Choose Option E: ")
        print("Exiting the Task.")
        break

    if operation == "S":
        print("""Select option data from
         a. Terminal input
         b. file input
         c. Quit""")
        option = input("Enter option (a/b/c): ")
        operation = option.lower()

        if operation == 'c':
            print("You Choose Option c: ")
            print("Quit the Task.")
            break

        if operation == "a":
            # Prompt the user to enter data
            x = input("Enter The Data:")
        elif operation == "b":
            #change the file name as you need
            source_file = 'clgs_pro.csv'#file name
            with open(source_file, 'r') as source_file:
                data = source_file.read()
            x = data
        else:
            print("Invalid option. Please enter 'a' or 'b'.")
            continue

        # Lists to store different types of characters
        uppercase_list = []
        lowercase_list = []
        mixedcase_list = []
        numeric_data = []
        numaric_data_other = []
        special_characters_data = []
        special_characters_data_other = []

        # Check the type of input data
        if x.isalpha():
            print(f"The given is purely alphabetic: {x}")
        elif x.isalnum():
            print(f"The given data is a combination of Alphabetic and Numeric: {x}")
        elif x.isprintable():
            print(f"The given data is a combination of Alphabetic, Numeric, and special characters: {x}")
        else:
            print(f"The input may contain spaces or special characters: {x}")

        # ********************Main Section*************************#
        # Split the input into a list of words and sort them
        a = x.split()
        a.sort()
        print("Data in sorted order:", a)

        # Iterate through each character in the sorted list
        for char in a:
            if char.isalpha():
                # Check and categorize alphabetic characters
                if char.isupper():
                    uppercase_list.append(char)
                elif char.islower():
                    lowercase_list.append(char)
                else:
                    mixedcase_list.append(char)
            elif char.isnumeric():
                # Check and categorize numeric characters
                numeric_data.append(char)
            elif char.isalnum():
                # Check and categorize alphanumeric characters
                numaric_data_other.append(char)
            else:
                # Check and categorize special characters
                special_characters_data.append(char)

        print(f"Uppercase words: {uppercase_list}")
        print(f"Lowercase words: {lowercase_list}")
        print(f"Mixed-case words: {mixedcase_list}")
        print(f"Numeric values: {numeric_data}")

        try:
            # Handle errors when checking numeric data
            for char in numeric_data:
                if not char.isnumeric():
                    numaric_data_other.append(char)
        except Exception as e:
            print(f"Error: {e}")

        print(f"Numeric values with additional data: {numaric_data_other}")
        print(f"Special characters: {special_characters_data}")

        # *********************output Section **************************#
        # Convert lists to tuples
        alpha_tuple_U = tuple(uppercase_list)
        alpha_tuple_l = tuple(lowercase_list)
        alpha_tuple_m = tuple(mixedcase_list)
        numaric_tuple_N = tuple(numeric_data)
        numaric_tuple_NN = tuple(numaric_data_other)
        special_tuple_U = tuple(special_characters_data)

        # Join tuples into strings
        alpha_u = "*".join(alpha_tuple_U)
        alpha_l = "**".join(alpha_tuple_l)
        alpha_m = "***".join(alpha_tuple_m)

        numa_n = "*@".join(numaric_tuple_N)
        numa_n_o = "**@".join(numaric_tuple_NN)

        spcl = "and".join(special_tuple_U)

        # Print the results with messages describing operations
        print(f"""Uppercase characters joined with '*': {alpha_u}
          Lowercase characters joined with '**': {alpha_l}
          Mixed-case characters joined with '***': {alpha_m}
          Numeric values joined with '*@': {numa_n}
          Numeric values with additional data joined with '**@': {numa_n_o}
          special charaters:{special_characters_data}""")

        print(f"""If you want chack again please enter  options "s" 
                              or 
                please enter E for Exit the task""")
