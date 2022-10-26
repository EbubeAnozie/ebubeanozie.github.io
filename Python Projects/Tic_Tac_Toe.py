"""
SPECIFICATION:
Version 1.10

This is a simple TIC-TAC-TOE game for two players.

The program divides the operations of the game
into seperate functional units for clarity in
implimentation.
"""



def display(row1, row2, row3):
    print('\n')
    print(row1)
    print("\n-------|---------|-------\n")
    print(row2)
    print("\n-------|---------|-------\n")
    print(row3)


def valid_input():
    row = ''
    column = ''
    while (row not in ['1', '2', '3']) or (column not in ['1', '2', '3']):
        row = input("Enter 1 or 2 or 3 for row: ")
        column = input("Enter 1 or 2 or 3 for column: ")
    return (int(row), 2*int(column)-2)



def player1_turn():
    print("\nPLAYER 1")
    space_chosen = valid_input()
    while space_chosen in occupied_position:
        print("Space already occupied.")
        space_chosen = valid_input()
    occupied_position.append(space_chosen)
    if space_chosen[0] == 1:
        row1[space_chosen[1]] = 'X'
        display(row1, row2, row3)
    elif space_chosen[0] == 2:
        row2[space_chosen[1]] = 'X'
        display(row1, row2, row3)
    else:
        row3[space_chosen[1]] = 'X'
        display(row1, row2, row3)

def player2_turn():
    print("\nPLAYER 2")
    space_chosen = valid_input()
    while space_chosen in occupied_position:
        print("Space already occupied.")
        space_chosen = valid_input()
    occupied_position.append(space_chosen)
    if space_chosen[0] == 1:
        row1[space_chosen[1]] = 'O'
        display(row1, row2, row3)
    elif space_chosen[0] == 2:
        row2[space_chosen[1]] = 'O'
        display(row1, row2, row3)
    else:
        row3[space_chosen[1]] = 'O'
        display(row1, row2, row3)
        
# Check for win or draw
def check_for_win():

    if (row1[0]==row1[2]==row1[4]=='X'
        or row2[0]==row2[2]==row2[4]=='X' 
        or row3[0]==row3[2]==row3[4]=='X'
        or row1[0]==row2[0]==row3[0]=='X' 
        or row1[2]==row2[2]==row3[2]=='X'
        or row1[4]==row2[4]==row3[4]=='X' 
        or row1[0]==row2[2]==row3[4]=='X'
        or row1[4]==row2[2]==row3[0]=='X'):
        print("\nPLAYER 1 has WON!\n")
        return "player1"

    elif (row1[0]==row1[2]==row1[4]=='O'
          or row2[0]==row2[2]==row2[4]=='O'
          or row3[0]==row3[2]==row3[4]=='O'
          or row1[0]==row2[0]==row3[0]=='O'
          or row1[2]==row2[2]==row3[2]=='O'
          or row1[4]==row2[4]==row3[4]=='O'
          or row1[0]==row2[2]==row3[4]=='O'
          or row1[4]==row2[2]==row3[0]=='O'):
        print("\nPLAYER 2 has WON!\n")
        return "player2"

    elif len(occupied_position) == 9:
        print("\nSTALEMATE!\nNo WINNER!")
        return "player1"

    else:
        pass


# Check if the player wants to play again
def play_again():
    check = ''
    while (not check.isdigit()) or (int(check) not in (1, 0)):
        check = input("Enter 1 to continue play, or 0 to quit the game: ")
    
    return int(check)


# Write a function on instruction and game rule.
def display_rules():
    response = ''
    while (not response.isdigit()) or (int(response) not in (0,1)):
        response = input("Enter 1 to read the rules for the game, or 0 to continue: ")
    if int(response) == 1:
        print("\nINSTRUCTIONS")
        print("1. This game version is between two human players.")
        print("2. Both players will play on the same 3 squares by 3 squares grid.")
        print("3. Player1 plays with are mark X by default, and player2 with mark O.")
        print("4. Players take turns putting their marks in empty squares.")
        print("5. The player that first gets 3 of his marks in a row (up, down, across, or diagonally) wins the game.")
        print("6. When all the 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
        return
    else:
        return

# default values setter
def default_values():
    row1 = [' ','|',' ','|',' ']
    row2 = [' ','|',' ','|',' ']
    row3 = [' ','|',' ','|',' ']
    occupied_position = []
    
    return row1, row2, row3, occupied_position



# MAIN BODY of the program

# Integrating the different units

display_rules()

row1, row2, row3, occupied_position = default_values()

display(row1, row2, row3)

while True:
    player1_turn()
    a = check_for_win()
    if a == "player1":
        if play_again():
            # set to default
            row1, row2, row3, occupied_position = default_values()
            display_rules()
            display(row1, row2, row3)
            continue
        else:
            break
    player2_turn()
    a = check_for_win()
    if a == "player2":
        if play_again():
            #clear display
            row1, row2, row3, occupied_position = default_values()
            display(row1, row2, row3)
            continue
        else:
            break
print("GAME ENDED")
