# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

cell1 = "1"
cell2 = "2"
cell3 = "3"
cell4 = "X"
cell5 = "5"
cell6 = "6"
cell7 = "O"
cell8 = "8"
cell9 = "9"
# these will be defined elsewhere, here only so it runs:
player1_symbol = "X"
player2_symbol = "O"

def input1():
    while True:
        position_input = input("Player 1 ("+player1_symbol+") what is your input (number): ")
        print(position_input)
        valid_cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
        if position_input in valid_cells and position_input not in [player1_symbol, player2_symbol]:
            break
        else:
            print("Invalid input smarty pants, don't try to be cute. Go again.")
#check on this, spelling of the function            print_board()
    print("Valid input")
    globals()[f"cell{position_input}"] = player1_symbol
    # the next line is just aa verification, final loop can exclude.
    print(position_input,"is now",globals()[f"cell{position_input}"])
1
# delete this before setting up the loop
input1()

def input2():
    while True:
        position_input = input("Player 2 ("+player2_symbol+") what is your input (number): ")
        print(position_input)
        valid_cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
        if position_input in valid_cells and position_input not in [player1_symbol, player2_symbol]:
            break
        else:
            print("Invalid input smarty pants, don't try to be cute. Go again.")
#check on this, spelling of the function            print_board()
    print("Valid input")
    globals()[f"cell{position_input}"] = player2_symbol
    # the next line is just aa verification, final loop can exclude.
    print(position_input,"is now",globals()[f"cell{position_input}"])

# delete this before setting up the loop
input2()


def check_win():
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

# This can be left in the startup, outside the loop
winner_symbol = None

for combo in winning_combinations:
    if combo[0] == combo[1] == combo[2]:
        winner_symbol = combo[0]
        break

# now, this breaks the 'for' function, what about the game loop to break? 
if winner_symbol != None:
    # WE CAN PRINT HERE THE WINNER 
    break


# Function for ... (displaying the board?)
# # def blabla():
#     pass


# Function for... (choosing a player?)
# def blablabla():
#     pass


# ... write as many functions as you need


# Tic-tac-toe game
# if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
#     print("Welcome to a new round of Tic-Tac-Toe!")
