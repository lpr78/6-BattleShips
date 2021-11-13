# Class
class battleShips:

    def __init__(self, hsize, vsize, ships, player1, player2):
        self.hsize = horizontalSize
        self.vsize = verticalSize
        self.player1 = player1
        self.player2 = PLAYER2
        self.ships = battleShips

    def gamBoard(self):
        board = []
        for x in range (0,self.horizontalSize):
            for x in range (0,self.verticalSize):
                board.append(0)




# Subroutines

# Main Program

# Constants
PLAYERS = 2
PLAYER2 = 'Computer'

# Variables
horizontalSize = int(input('Enter the Horizontal grid size: '))
verticalSize = int(input('Enter the Vertical grid size: '))
player1 = input('Enter player name: ')
battleShips = int(input('Enter the number of battleships (max of 5): '))
while battleShips <0 or battleShips >5:
    battleShips = int(input('Enter a valid number of battleships (max of 5): '))