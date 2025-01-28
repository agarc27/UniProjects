"""
Tic Tac Toe Helper: provides two functions to be used for a game of Tic Tac Toe
1) Check for winner: determines the current state of the board
2) Print ugly board: prints out a tic tac toe board in a basic format
"""


# Given a tic, tac, toe board determine if there is a winner
# Function inputs:
#     boardList: an array of 9 strings representing the tic tac toe board
#     moveCounter: an integer representing the number of moves that have been made
# Returns a string:
#     'x' if x won
#     'o' if o won
#     'n' if no one wins
#     's' if there is a stalemate
def checkForWinner(boardList, moveCounter):
    j = 0
    for i in range(0, 9, 3):
        # Check for 3 in a row
        if boardList[i] == boardList[i+1] == boardList[i+2]:
            return boardList[i]

        # Check for 3 in a column
        elif boardList[j] == boardList[j+3] == boardList[j+6]:
            return boardList[j]

        # Check the diagonal from the top left to the bottom right
        elif boardList[0] == boardList[4] == boardList[8]:
            return boardList[0]

        # Check the diagonal from top right to bottom left
        elif boardList[2] == boardList[4] == boardList[6]:
            return boardList[2]
        j += 1

    # If winner was not found and board is completely filled up, return stalemate
    if moveCounter > 8:
        return "s"

    # Otherwise, 3 in a row anywhere on the board
    return "n"


# Print out the tic tac toe board
# Input: list representing the tic tac toe board
# Return value: none
def printUglyBoard(boardList):
    print()
    counter = 0
    for i in range(3):
        for j in range(3):
            print(boardList[counter], end="  ")
            counter += 1
        print()
