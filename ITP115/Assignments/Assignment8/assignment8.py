# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Assignment 8
# Description:
# A program that allows two people to play
# a game of Tic Tac Toe.

# Imports the two functions to be used in the program from the TicTacToe Helper file
from TicTacToeHelper import printUglyBoard
from TicTacToeHelper import checkForWinner

# Defines the function that checks if the position the player wants is
# in play or already taken/not on the board.
def isValidNumber(boardList, position):
    if str(position) in boardList:
        return True
    else:
        return False

# Defines the function that updates the board by overwriting the position
# with the player's letter
def updateBoard(boardList, position, playerLetter):
    boardList.remove(str(position))
    boardList.insert(position, playerLetter)

# Defines the function that essentially plays the game; look inside for further comments
def playGame():
    # Variables to be used below such as the tic-tac-toe board, number of moves, and if a winner is determined
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    moveCounter = 0
    winner = "n"
    # Loop to decide the current turn as well as determine if anyone has won yet
    while winner == "n":
        turnOrder = moveCounter % 2
        printUglyBoard(boardList)
        # Allows for Player X to choose their spot
        if turnOrder == 0:
            moveCounter += 1
            choice = int(input("Player x, enter a number: "))
            check = isValidNumber(boardList, choice)
            while check is False:
                choice = int(input("Player x, enter a number: "))
                check = isValidNumber(boardList, choice)
            else:
                updateBoard(boardList, choice, "x")
        # Allows for Player O to choose their spot
        elif turnOrder == 1:
            moveCounter += 1
            choice = int(input("Player o, enter a number: "))
            check = isValidNumber(boardList, choice)
            while check is False:
                choice = int(input("Player o, enter a number: "))
                check = isValidNumber(boardList, choice)
            else:
                updateBoard(boardList, choice, "o")
        # Checks the loop to determine if a winner has been determined
        winner = checkForWinner(boardList, moveCounter)
    # Calls the conclusion of the game and the winner.
    printUglyBoard(boardList)
    print("Game Over!")
    if winner == "s":
        print("Stalemate reached.")
    elif winner == "x":
        print("Player x is the winner!")
    else:
        print("Player o is the winner!")

# Defines the main function that allows us to play the game and also ask to play another round.
def main():
    print("Let's play Tic Tac Toe!")
    round = "y"
    while round == "y":
        playGame()
        round = input("Do you want to continue playing (y or n)? ").lower()
        round = round.strip()
    print("Goodbye!")

# Calls the main function
main()
