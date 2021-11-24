"""
Battle Ship Game Version 1 => 12/11/2021
"""
# Importing Libraries into Python Code
import random


class Ship:
    """Class approach for board manipulation"""

    def __init__(self, size, orientation, location,):
        self.size = size

        if orientation == 'horizontal' or orientation == 'vertical':
            self.orientation = orientation
        else:
            raise ValueError("'horizontal' or 'vertical' values only accepted."
                             )

        if orientation == 'horizontal':
            if location['row'] in range(rowSize):
                self.coordinates = []
                for col in range(size):
                    if location['col'] + col in range(colSize):
                        self.coordinates.append({'row': location['row'], 'col': location['col'] + col})
                    else:
                        raise IndexError('Column is out of range.')
            else:
                raise IndexError('Row is out of range.')
        elif orientation == 'vertical':
            if location['col'] in range(colSize):
                self.coordinates = []
                for row in range(size):
                    if location['row'] + row in range(rowSize):
                        self.coordinates.append({'row': location['row'] + row, 'col': location['col']})
                    else:
                        raise IndexError('Row is out of range.')
            else:
                raise IndexError('Column is out of range.')

        if self.filled():
            show_board(board)
            print(' '.join(str(coords) for coords in self.coordinates))
            raise IndexError('A ship already occupies that space.')
        else:
            self.fill_board()

    def filled(self):
        for coords in self.coordinates:
            if board[coords['row']][coords['col']] == 1:
                return True
        return False

    def fill_board(self):
        for coords in self.coordinates:
            board[coords['row']][coords['col']] = 1

    def contains(self, location):
        for coords in self.coordinates:
            if coords == location:
                return True
        return False

    def destroyed(self):
        for coords in self.coordinates:
            if DISPLAY_BOARD[coords['row']][coords['col']] == 'O':
                return False
            elif DISPLAY_BOARD[coords['row']][coords['col']] == '*':
                raise RuntimeError('Board display inaccurate')
        return True


# Defined Subroutines
def show_board(board_array):
    """To display board content."""
    print("\n  " + " ".join(str(x) for x in range(1, colSize + 1)))
    for row in range(rowSize):
        print(str(row + 1) + " " + " ".join(str(c) for c in board_array[row]))
    print()


def location_search(size, orientation):
    """Search location of ships on the battleship game."""
    locations = []
    if orientation != 'horizontal' and orientation != 'vertical':
        raise ValueError("Orientation must have a value of either 'horizontal' or 'vertical'.")

    if orientation == 'horizontal':
        if size <= colSize:
            for row in range(rowSize):
                for col in range(colSize - size + 1):
                    if 1 not in board[row][col:col+size]:
                        locations.append({'row': row, 'col': col})
    elif orientation == 'vertical':
        if size <= rowSize:
            for col in range(colSize):
                for row in range(rowSize - size + 1):
                    if 1 not in [board[i][col] for i in range(row, row+size)]:
                        locations.append({'row': row, 'col': col})

    if not locations:
        return 'None'
    else:
        return locations


def random_location():
    """Function to randomly place ship locations on board."""
    size = random.randint(min_shipSize, max_shipSize)
    orientation = 'horizontal' if random.randint(0, 1) == 0 else 'vertical'

    locations = location_search(size, orientation)
    if locations == 'None':
        return 'None'
    else:
        return {'location': locations[random.randint(0, len(locations) - 1)], 'size': size, 'orientation': orientation}


def get_row():
    """Procedure to validate row selection by user."""
    while True:
        try:
            guess = int(input("Row Guess: "))
            if guess in range(1, rowSize + 1):
                return guess - 1
            else:
                print("\nOops, that's not even in the ocean.")
        except ValueError:
            print("\nPlease enter a number")


def get_column():
    """Procedure to validate column selection by user."""
    while True:
        try:
            guess = int(input("Column Guess: "))
            if guess in range(1, colSize + 1):
                return guess - 1
            else:
                print("\nOops, that's not even in the ocean.")
        except ValueError:
            print("\nPlease enter a number")


def menu():
    """Function to validate menu selection choices by the user."""
    print('''
Select one of the following options:
1.  Set up board
2.  Play the game
3.  Check high scores
4.  Exit
''')
    local_choice = int(input('Enter number choice: '))
    while local_choice < 1 or choice > 4:
        local_choice = int(input('Enter valid choice: '))
    return local_choice


def set_board():
    """Function for user selection on choices for the Battlship Board."""
    n_player_name = input('Enter Player name: ')
    n_rowsize = size_validation('row', 10)
    n_colsize = size_validation('column', 10)
    n_shipnum = size_validation('ship', 5)
    n_max_shipsize = size_validation('max ship size', 3)
    nmin_ship_size = size_validation('min ship size', 1)
    n_roundspergame = size_validation('number of round', 50)
    return n_player_name, n_rowsize, n_colsize, n_shipnum, n_max_shipsize, nmin_ship_size, n_roundspergame


def size_validation(direct, n_max):
    """Function to range check the entries for the set_board function."""
    num = int(input(f"Enter the number of {direct}'s: "))
    while num < 1 or num > n_max:
        num = int(input(f'Enter a valid {direct} value: '))
    return num


def game_details(player, row, col, shipno, max_ship, min_ship, rounds):
    """Procedure to output the settings selected by the user."""
    print(f'''
-----------------------------------------------------------------
Welcome {player} to the BattleShip Game.
The Board size is {row} by {col}
The number of ships is {shipno}
The ship size ranges from {min_ship} to {max_ship} blocks
You have {rounds} guesses before you sink!
Good Luck!
-----------------------------------------------------------------
''')

# Main Program => Play Game


print("\033[1m" + 'Welcome to the Battleship Game' + "\033[0m/n")
playerName, rowSize, colSize, shipNum, max_shipSize, min_shipSize, roundsPerGame = None, None, None, None, None, None, None

REPEAT = True
while REPEAT is True:
    choice = menu()
    if choice == 1:
        # Settings Variables
        playerName, rowSize, colSize, shipNum, max_shipSize, min_shipSize, roundsPerGame = set_board()
        game_details(playerName, rowSize, colSize, shipNum, max_shipSize, min_shipSize, roundsPerGame)
    elif choice == 2:
        if playerName is None:
            print('You need to set up the board first')
        else:
            DISPLAY_BOARD = None

            # Create lists
            shipList = []
            board = [[0] * colSize for x in range(rowSize)]
            DISPLAY_BOARD = [["~"] * colSize for x in range(rowSize)]
            show_board(DISPLAY_BOARD)

            TEMP = 0
            while TEMP < shipNum:
                shipInfo = random_location()
                if shipInfo == 'None':
                    continue
                else:
                    shipList.append(Ship(shipInfo['size'], shipInfo['orientation'], shipInfo['location']))
                    TEMP += 1
            del TEMP

            for turn in range(roundsPerGame):
                print("Turn:", turn + 1, "of", roundsPerGame)
                print("Ships left:", len(shipList))
                print()
                cordGuess = {}
                while True:
                    cordGuess['row'] = get_row()
                    cordGuess['col'] = get_column()
                    if DISPLAY_BOARD[cordGuess['row']][cordGuess['col']] == 'X' or DISPLAY_BOARD[cordGuess['row']][cordGuess['col']] == '*':
                        print("\nYou guessed that one already.")
                    else:
                        break
                HITSHIP = False
                for ship in shipList:
                    if ship.contains(cordGuess):
                        print("Hit!")
                        HITSHIP = True
                        DISPLAY_BOARD[cordGuess['row']][cordGuess['col']] = 'X'
                        if ship.destroyed():
                            print("Ship Destroyed!")
                            shipList.remove(ship)
                        break
                if not HITSHIP:
                    DISPLAY_BOARD[cordGuess['row']][cordGuess['col']] = '*'
                    print("You missed!")
                show_board(DISPLAY_BOARD)
                if not shipList:
                    break

            # End Game
            if shipList:
                print("You lose!")
            else:
                print("All the ships are sunk. You win!")
    elif choice == 3:
        print('TBC')
    else:
        print('Hopefully we see you again soon!')
        exit()
