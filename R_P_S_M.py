"""ROCK PAPER SCISSOR Man v/s Man"""
#SELECT THE GAME START AND EXIT 
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
#***************START******************
    if operation == "S":
        player_1 = input("Enter  Player_1 Name: ")
        player_2 = input("Enter  Player_2 Name: ")
        print(f"The 1st Player Name is: {player_1}")
        print(f"The 2nd Player Name is: {player_2}")
        R = "Rock"
        P = "Paper"
        S = "Scissors"
        this_dict ={ "R" : "Rock",
                     "P" : "Paper",
                     "S" : "Scissors",
                     }

 #************Main Part*****************#      
        def my_function(player_1):
                option = input(f"{player_1} please select your option (R/P/S): ")
                player_1_choice = option.upper()
                
                return player_1_choice

        def my_function_2(player_2):
                option = input(f"{player_2} please select your option (R/P/S): ")
                player_2_choice = option.upper()
                
                return player_2_choice

# Call the functions to get the values
        X = my_function(player_1)
        y = my_function_2(player_2)

# Now you can use player's choice values in thid dict 
        
        
        palyer_1_choice = this_dict[X]
        player_2_choice = this_dict[y]

#************ Game logic to check ***************#
        if palyer_1_choice == R and player_2_choice == P:
            print(f"{player_2} selected {P}, so {player_2} is won the game.")
        elif palyer_1_choice == R and player_2_choice == S:
            print(f"{player_1} selected {R}, so {player_1}is won the game.")
        elif palyer_1_choice == R and player_2_choice == R:
            print(f"{player_1} and {player_2}selected {R}, so the game is Tie.")
        elif palyer_1_choice == P and player_2_choice == R:
            print(f"{player_1} selected {P}, so {player_1} is won the game.")
        elif palyer_1_choice == P and player_2_choice == S:
             print(f"{player_2} selected {S}, so {player_2} is won the game.")
        elif palyer_1_choice == P and player_2_choice == P:
          print(f"{player_1} and {player_2} selected {P}, so the game is Tie.")
        elif palyer_1_choice == S and player_2_choice == P:
            print(f"{player_1} selected {S}, so {player_1} is won the game.")
        elif palyer_1_choice == S and player_2_choice == R:
            print(f"{player_2} selected {R}, so {player_2} is won the game.")
        elif palyer_1_choice == S and player_2_choice == S:
            print(f"{player_1} and {player_2} selected {S}, so the game is Tie.")
        else:
            print("error")