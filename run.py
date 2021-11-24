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
            showBoard(board)
            print(' '.join(str(coords) for coords in self.coordinates))
            raise IndexError('A ship already occupies that space.')
        else:
            self.fillBoard()

    def filled(self):
        for coords in self.coordinates:
            if board[coords['row']][coords['col']] == 1:
                return True
        return False

    def fillBoard(self):
        for coords in self.coordinates:
            board[coords['row']][coords['col']] = 1

    def contains(self, location):
        for coords in self.coordinates:
            if coords == location:
                return True
        return False

    def destroyed(self):
        for coords in self.coordinates:
            if displayBoard[coords['row']][coords['col']] == 'O':
                return False
            elif displayBoard[coords['row']][coords['col']] == '*':
                raise RuntimeError('Board display inaccurate')
        return True


# Defined Subroutines
def showBoard(board_array):
    print("\n  " + " ".join(str(x) for x in range(1, colSize + 1)))
    for row in range(rowSize):
        print(str(row + 1) + " " + " ".join(str(c) for c in board_array[row]))
    print()


def locationSearch(size, orientation):
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


def randomLocation():
    size = random.randint(minShipSize, maxShipSize)
    orientation = 'horizontal' if random.randint(0, 1) == 0 else 'vertical'

    locations = locationSearch(size, orientation)
    if locations == 'None':
        return 'None'
    else:
        return {'location': locations[random.randint(0, len(locations) - 1)], 'size': size, 'orientation': orientation}


def getRow():
    while True:
        try:
            guess = int(input("Row Guess: "))
            if guess in range(1, rowSize + 1):
                return guess - 1
            else:
                print("\nOops, that's not even in the ocean.")
        except ValueError:
            print("\nPlease enter a number")


def getColumn():
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
    print('''
Select one of the following options:
1.  Set up board
2.  Play the game
3.  Check high scores
4.  Exit
''')
    localChoice = int(input('Enter number choice: '))
    while localChoice < 1 or choice > 4:
        localChoice = int(input('Enter valid choice: '))
    return localChoice


def setBoard():
    nPlayerName = input('Enter Player name: ')
    nRowSize = sizeValidation('row', 10)
    nColSize = sizeValidation('column', 10)
    nShipNum = sizeValidation('ship', 5)
    nMaxShipSize = sizeValidation('max ship size', 3)
    nMinShipSize = sizeValidation('min ship size', 1)
    nRoundsPerGame = sizeValidation('number of round', 50)
    return nPlayerName, nRowSize, nColSize, nShipNum, nMaxShipSize, nMinShipSize, nRoundsPerGame


def sizeValidation(direct, nMax):
    num = int(input(f"Enter the number of {direct}'s: "))
    while num < 1 or num > nMax:
        num = int(input(f'Enter a valid {direct} value: '))
    return num


# Main Program => Play Game

print("\033[1m" + 'Welcome to the Battleship Game' + "\033[0m/n")
playerName, rowSize, colSize, shipNum, maxShipSize, minShipSize, roundsPerGame = None, None, None, None, None, None, None
repeat = True
while repeat is True:
    choice = menu()
    if choice == 1:
        # Settings Variables
        playerName, rowSize, colSize, shipNum, maxShipSize, minShipSize, roundsPerGame = setBoard()
    elif choice == 2:
        if playerName is None:
            print('You need to set up the board first')
        else:
            displayBoard = None

            # Create lists
            shipList = []
            board = [[0] * colSize for x in range(rowSize)]
            displayBoard = [["~"] * colSize for x in range(rowSize)]
            showBoard(displayBoard)

            temp = 0
            while temp < shipNum:
                shipInfo = randomLocation()
                if shipInfo == 'None':
                    continue
                else:
                    shipList.append(Ship(shipInfo['size'], shipInfo['orientation'], shipInfo['location']))
                    temp += 1
            del temp

            for turn in range(roundsPerGame):
                print("Turn:", turn + 1, "of", roundsPerGame)
                print("Ships left:", len(shipList))
                print()
                cordGuess = {}
                while True:
                    cordGuess['row'] = getRow()
                    cordGuess['col'] = getColumn()
                    if displayBoard[cordGuess['row']][cordGuess['col']] == 'X' or displayBoard[cordGuess['row']][cordGuess['col']] == '*':
                        print("\nYou guessed that one already.")
                    else:
                        break
                hitShip = False
                for ship in shipList:
                    if ship.contains(cordGuess):
                        print("Hit!")
                        hitShip = True
                        displayBoard[cordGuess['row']][cordGuess['col']] = 'X'
                        if ship.destroyed():
                            print("Ship Destroyed!")
                            shipList.remove(ship)
                        break
                if not hitShip:
                    displayBoard[cordGuess['row']][cordGuess['col']] = '*'
                    print("You missed!")
                showBoard(displayBoard)
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
