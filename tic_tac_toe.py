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

# DISPLAYING THE BOARD
def display_board():
    """This function prints out the current state of the game board."""
    print("\n")
    print(" " + cell1 + " | " + cell2 + " | " + cell3)
    print("-----------")
    print(" " + cell4 + " | " + cell5 + " | " + cell6)
    print("-----------")
    print(" " + cell7 + " | " + cell8 + " | " + cell9)
    print("\n")

# GETTING THE PLAYERS TO CHOOSE A SYMBOL
def choose_symbol():
    """Asks Player 1 to choose X or O and assigns the other to Player 2."""
    player1_symbol = ""
    # Keep asking while the answer is NOT one of the valid options
    while player1_symbol != "X" and player1_symbol != "x" and player1_symbol != "O" and player1_symbol != "o":
        player1_symbol = input("Welcome Player 1, would you like to be 'X' or to be 'O'? ")
        # If they typed a wrong letter, print the error message
        if player1_symbol != "X" and player1_symbol != "x" and player1_symbol != "O" and player1_symbol != "o":
            print("Invalid input! Please choose either 'X' or 'O'.")
    # this chnages lowercase input to uppercase
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

# ask players for the input
def input1():
    while True:
        print("Player 1 (" + player1_symbol +") what is your input (number): ")
        position_input = input()
        valid_cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
        if position_input in valid_cells and position_input not in [player1_symbol, player2_symbol]:
            break
        else:
            print("Invalid input smarty pants, don't try to be cute. Go again.")
            display_board()
    globals()[f"cell{position_input}"] = player1_symbol
    # the next line is just a verification, final loop can exclude.
    # print(position_input,"is now",globals()[f"cell{position_input}"])

def input2():
    while True:
        print("Player 2 (" + player2_symbol + ") what is your input (number): ")
        position_input = input()
        valid_cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
        if position_input in valid_cells and position_input not in [player1_symbol, player2_symbol]:
            break
        else:
            print("Invalid input smarty pants, don't try to be cute. Go again.")
            display_board()
    globals()[f"cell{position_input}"] = player2_symbol
    # the next line is just a verification, final loop can exclude.
    # print(position_input,"is now",globals()[f"cell{position_input}"])

def check_win():
    winner_symbol = ""
    winning_combinations = [
    (cell1, cell4, cell7),  # column 1
    (cell2, cell5, cell8),  # column 2
    (cell3, cell6, cell9),  # column 3
    (cell1, cell2, cell3),  # row 1
    (cell4, cell5, cell6),  # row 2
    (cell7, cell8, cell9),  # row 3
    (cell1, cell5, cell9),  # diagonal 1
    (cell3, cell5, cell7),  # diagonal 2
    ]
    for combo in winning_combinations:
        if combo[0] == combo[1] == combo[2]:
            winner_symbol = combo[0]
    return winner_symbol

# MAIN LOOP
def play_game():
    turn = 1
    while turn <= 9: # because the game should have a total of at most 9 turns
        print("Turn number:",turn)
        display_board()
        input1()
        winner_symbol = check_win()
        if winner_symbol != "":
            print ("PLAYER 1 IS THE WINNER!!!")
            break
        turn += 1
        if turn == 10:
            print("It's a tie!")
            break
        print("Turn number:",turn)
        display_board()
        input2()
        winner_symbol = check_win()
        if winner_symbol != "":
            print ("PLAYER 2 IS THE WINNER!!!")
            break
        turn += 1
    
# Tic-tac-toe game runner
if __name__ == "__main__":
    print("Welcome to a new round of Tic-Tac-Toe!")
        # 1. Let the players choose their symbols
    player1_symbol, player2_symbol = choose_symbol()
    # Start loop
    play_game()


