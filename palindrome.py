print("""Select option for Task
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
        print("""Select option for Task
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
            string = input("Enter a data_values:")
        elif operation =="b":
             source_file = 'clgs_pro.csv'
             with open(source_file, 'r') as source_file:
                data = source_file.read()
                string = data
        else:
            print("Invalid option. Please enter 'a' or 'b'.")
            continue
        palindrome = []
        non_palindrome = []
# Renamed the variable to avoid shadowing the built-in str
        str_v= string  
# Check the type of input data
        if str_v.isalpha():
            print(f"The given is purely alphabetic: {str_v}")
            x = str_v[::-1]
            if str_v==x:
             print(f"The given data {str_v} is in palindrome")
            else:
             print(f"The given data {str_v} is not in palindrome")  
        else:
            print(f"The is also take _space_ as character: {str_v}")

# ********************Main Section************************* #
# Split the input into a list of words and sort them
            a = str_v.split()
            a.sort()
            print(len(a))
            print("Data in sorted order:", a)

# Iterate through each word in the sorted list
              # Iterate through each word in the sorted list
            for word in a:
              if word == word[::-1]:  # Check if the word is a palindrome
                print(f"{word} is a PALINDROME")
                palindrome.append(word)
              else:
                print(f"{word} is NOT a PALINDROME")
                non_palindrome.append(word)

        # Print the lists of palindromes and non-palindromes
                print("\nPalindromes:", palindrome)
                print("Non-Palindromes:", non_palindrome)
            print(f"\nIf you want to check again, please enter 'S' or enter 'E' to exit the task")