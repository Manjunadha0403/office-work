player_1 = input("Enter Player_1 Name: ")
player_2 = input("Enter Player_2 Name: ")
this_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}

def my_function(player):
    option = input(f"{player} please select your option (R/P/S): ")
    return option.upper()

def play_game():
    while True:
        option = input("Enter option (P/Q): ")
        operation = option.upper()
        if operation == 'Q':
            print("Exiting the Game.")
            break
        elif operation == 'P':
            p_1,p_2,T_1 = 0,0,0
            num_play =  0
            max_no_plays = 100 # Set the desired number of games
            while num_play < max_no_plays:
                g = num_play+1
                print(f"\nGame {g}:")

                player_1_choice = my_function(player_1)
                player_2_choice = my_function(player_2)

                print(f"{player_1}'s select: {this_dict[player_1_choice]}")
                print(f"{player_2}'s select: {this_dict[player_2_choice]}")

                if player_1 == player_2:
                    T_1 += 1
                    print(f" The  game {g} is Tie.")
                elif (player_1 == 'R' and player_2 == 'S') or (player_1 == 'P' and player_2 == 'R') or (player_1 == 'S' and player_2 == 'P'):
                    p_1 += 1
                    print(f" {player_1} is won the game {g}.")
                else:
                    p_2 += 1
                    print(f" {player_2} is won the game {g}.")
        
                num_play += 1
                
                play_again = input("Do you want to play_Again ? (Y/N): ").upper()
                if play_again != 'Y':
                        print(f"Sorry you enter  {play_again}  The game is Quiting")
                        break
            
            print(f"""Now checking overall results:
                  No. of games {g}
                  {player_1} was won {p_1} games
                  {player_2} was won {p_2} games
                  {T_1} games are Tie  """)
            if p_1 > p_2:
                print(f"{player_1} won the overall game.")
            elif p_1 < p_2:
                print(f"{player_2} won the overall game.")
            else:
                print("The overall game is a tie.")
            break
play_game()