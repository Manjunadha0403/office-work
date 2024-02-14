import random

print("""Select option for Game
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
        print("""Select option for Game
         a. Man v/s computer 
         b. Man v/s man
         c. Quit""")
        option = input("Enter option (a/b/c): ")
        operation = option.lower()

        if operation == 'c':
            print("You Choose Option c: ")
            print("Quit the Game.")
            break
#************ Man v/s Computer*************#
        if operation == "a":
            player_1 = "computer"
            player_2 = input("Enter player Name: ")
           
            def my_function(player_1_choice):
                option = random.choice(['R', 'P', 'S'])
                player_1_choice = option
                return player_1_choice

            def my_function_2(player_2):
                option = input(f"{player_2} please select your option (R/P/S): ")
                player_2_choice = option.upper()
                return player_2_choice
#************Man v/s Man*****************
        elif operation == "b":
            print("Only Two Player mode is there" )
            player_1 = input("Enter Player_1 Name: ")
            player_2 = input("Enter Player_2 Name: ")
            print(f"The 1st Player Name is: {player_1}")
            print(f"The 2nd Player Name is: {player_2}")

            def my_function(player_1):
                option = input(f"{player_1} please select your option (R/P/S): ")
                player_1_choice = option.upper()
                
                return player_1_choice

            def my_function_2(player_2):
                option = input(f"{player_2} please select your option (R/P/S): ")
                player_2_choice = option.upper()
                
                return player_2_choice
        else :
            print("Invalid option. Please enter 'a' or 'b'.")
            continue
        R = "Rock"
        P = "Paper"
        S = "Scissors"
        this_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}
            # Call the functions to get the values
        player_1_choice = my_function(player_1)
        player_2_choice = my_function_2(player_2)

        # Now you can use p_1 and p_2 wherever you need the values
        print(f"{player_1}'s select: {this_dict[player_1_choice]}")
        print(f"{player_2}'s select: {this_dict[player_2_choice]}")

        # Game logic
        if player_1_choice == 'R' and player_2_choice == 'P'  :
            print(f"{player_2} selected {this_dict[player_2_choice]}, so {player_2} is won the game.")
        elif player_1_choice == 'R' and player_2_choice == 'S':
            print(f"{player_1} selected {this_dict[player_1_choice]}, so {player_1} is won the game.")
        elif player_1_choice == 'R' and player_2_choice == 'R':
            print(f"{player_1} and {player_2} both players selected {this_dict[player_1_choice]}, so the game is Tie.")
        elif player_1_choice == 'P' and player_2_choice == 'R':
            print(f"{player_1} selected {this_dict[player_1_choice]}, so {player_1} is won the game.")
        elif player_1_choice == 'P' and player_2_choice == 'S':
            print(f"{player_2} selected {this_dict[player_2_choice]}, so {player_2} is won the game.")
        elif player_1_choice == 'P' and player_2_choice == 'P':
            print(f"{player_1} and {player_2} both players selected {this_dict[player_1_choice]}, so the game is Tie.")
        elif player_1_choice == 'S' and player_2_choice == 'P':
            print(f"{player_1} selected {this_dict[player_1_choice]}, so {player_1} is won the game.")
        elif player_1_choice == 'S' and player_2_choice == 'R':
            print(f"{player_2} selected {this_dict[player_2_choice]}, so {player_2} is won the game.")
        elif player_1_choice == 'S' and player_2_choice == 'S':
            print(f"{player_1} and {player_2} both players selected {this_dict[player_1_choice]}, so the game is Tie.")
        else:
            print("Error")
        print(f"\nIf you want to play again, please enter 'S' or enter 'E' to exit the Game")