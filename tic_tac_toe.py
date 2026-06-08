# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# GLOBAL VARIABLES FOR THE BOARD CELLS
cell1 = "1"
cell2 = "2"
cell3 = "3"
cell4 = "4"
cell5 = "5"
cell6 = "6"
cell7 = "7"
cell8 = "8"
cell9 = "9"


#1. DISPLAYING THE BOARD
def display_board():
    """This function prints out the current state of the game board."""
    print("\n")
    print(" " + cell1 + " | " + cell2 + " | " + cell3)
    print("-----------")
    print(" " + cell4 + " | " + cell5 + " | " + cell6)
    print("-----------")
    print(" " + cell7 + " | " + cell8 + " | " + cell9)
    print("\n")


#2. GETTING THE PLAYERS TO CHOOSE A SYMBOL
def choose_symbol():
    """Asks Player 1 to choose X or O and assigns the other to Player 2."""
    player1_symbol = ""
    
    # Keep asking while the answer is NOT one of the valid options
    while player1_symbol != "X" and player1_symbol != "x" and player1_symbol != "O" and player1_symbol != "o":
        player1_symbol = input("Welcome Player 1, would you like to be 'X' or to bey 'O'? ")
        
        # If they typed a wrong letter, print the error message
        if player1_symbol != "X" and player1_symbol != "x" and player1_symbol != "O" and player1_symbol != "o":
            print("Invalid input! Please choose either 'X' or 'O'.")

    # this chnages lowercase inpuut to uppercase
    if player1_symbol == "x":
        player1_symbol = "X"
    if player1_symbol == "o":
        player1_symbol = "O"

    # Assign the unselected symbol to Player 2
    if player1_symbol == "X":
        player2_symbol = "O"
    else:
        player2_symbol = "X"

    
    print("\nPlayer 1 is " + player1_symbol + "!")
    print("Player 2 is " + player2_symbol + "!\n")
    
    return player1_symbol, player2_symbol


#ASKING FOR PLAYER INPUT TAKING TURNS
def play_game(player1_symbol, player2_symbol):
    """Loops through turns and updates the board variables."""
    # we use global to change the cell variables outside this function
    global cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9
    
    # we always start with Player 1
    current_player = "Player 1"
    current_symbol = player1_symbol
    
    # we defind the number of turns
    turn = 1
    while turn <= 9: # because the game should have a total of at most 9 turns
        print(current_player + ", it is your turn to play. (" + current_symbol + ")")
        position = input("Choose a position: ")
    

    # WE NEED TO INSERT ALEX's CODE HERE TO RESTRICT OVERWRITING OF PREVIOUS PLAYER INPUT


    # this updates the correct cell based on the previous player input
        if position == "1":
            cell1 = current_symbol
        elif position == "2":
            cell2 = current_symbol
        elif position == "3":
            cell3 = current_symbol
        elif position == "4":
            cell4 = current_symbol
        elif position == "5":
            cell5 = current_symbol
        elif position == "6":
            cell6 = current_symbol
        elif position == "7":
            cell7 = current_symbol
        elif position == "8":
            cell8 = current_symbol
        elif position == "9":
            cell9 = current_symbol
            
        # this reprints the entire updated board for us to see
        display_board()
        
        # after a turn, we then switch turns to the other player
        if current_player == "Player 1":
            current_player = "Player 2"
            current_symbol = player2_symbol
        else:
            current_player = "Player 1"
            current_symbol = player1_symbol
            
        # turn increment to move to the next turn number
        turn = turn + 1







# Tic-tac-toe game runner
if __name__ == "__main__":
    print("Welcome to a new round of Tic-Tac-Toe!")
    
    # 1. Let the players choose their symbols
    p1, p2 = choose_symbol()
    
    # 2. Then display the starting board
    display_board()

    # 3. Start loop
    play_game(p1, p2)