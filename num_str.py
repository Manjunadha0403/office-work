# Python program for finding string data like [A-Z] and [a-z] in a group of data

# *************INPUT Section*****************#

print("""Select option 
         S. Start 
         E. Exit""")

while True:
   option = input("Enter option (S/E): ")
   operation = option.upper()
   try:
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
            
        print(type(x))
        print(x)
        if x.isalpha():
            print(f"The given is purely alphabetic: {x}")
        elif x.isalnum():
            print(f"The given data is a combination of Alphabetic and Numeric: {x}")
        elif x.isprintable():
            print(f"The given data is a combination of Alphabetic, Numeric, and special characters: {x}")
        else:
            print(f"The input may contain spaces or special characters: {x}")
         
        a = x.split()
        a.sort()
        print("Data in sorted order:", a)
  
        def is_numeric(value):
               return all(c.isdigit() for c in value)

# Use list comprehension to filter strings with all numeric characters
        numeric_strings = [s for s in a if is_numeric(s)]
        print("Original List:", a)
        print("Numeric Strings:", numeric_strings)
        m = len(a)
        print(len(a))
        n =len(numeric_strings)
        print(len(numeric_strings))
        if m ==n:
            print(f"The given data contain only Numeric_string{x} ")
        else:
            print(f"The given data contain not all  Numeric_string values{x} ")
    
   except:
      print("Error in OPtions please select S/E: ")