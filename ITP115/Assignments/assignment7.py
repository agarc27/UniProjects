# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: number or nickname
# Assignment 7
# Description:
# This program allows you to play rounds of
# Rock, Paper, Scissors against the computer.

# Importing the random module to be used for the computer's number
import random


# Prints the rules of Rock Paper Scissors within a defined function
def displayRules():
    print("Let's play Rock Paper Scissors.")
    print("The rules of the game are:")
    print("\tRock smashes Scissors")
    print("\tScissors cut Paper")
    print("\tPaper covers Rock")
    print("If both the choices are the same, it's a tie")


# Randomly generates a number from 0 to 2 to be used as the computer's
# choice for Rock, Paper, Scissors within a function
def getComputerNum():
    computerNum = random.randrange(0, 3, 1)
    return computerNum


# Asks for input from the player to determine their choice for
# Rock, Paper, Scissors within a function
def getPlayerNum():
    print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")
    playerNum = int(input("> "))
    while playerNum != 0 and playerNum != 1 and playerNum != 2:
        print("Try Again.")
        print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")
        playerNum = int(input("> "))
    return playerNum


# Determines the winner of the round using the results of the previous
# two functions, within a function
def playRound(computerNum, playerNum):
    roundScore = playerNum - computerNum
    # A score of 0 means a tie
    if roundScore == 0:
        return 0
    # A score of -1 or 2 means the computer wins.
    elif roundScore == -1 or roundScore == 2:
        return -1
    # A score of 1 means you win.
    else:
        return 1


# Function that asks for player input if they want to continue playing
def continueGame():
    cont = input("Do you want to continue playing (y or n)? ")
    cont = cont.lower()
    cont = cont.strip()
    if cont == "y":
        return True
    else:
        return False

# Main function used to call all previous functions; also counts the number of ties, wins
# and losses as well as loops if the player wishes to keep playing
def main():
    tieCounter = 0
    comCounter = 0
    playCounter = 0
    more = True
    while more == True:
        displayRules()
        computerNum = getComputerNum()
        playerNum = getPlayerNum()
        round = playRound(computerNum, playerNum)
        if round == 0:
            tieCounter += 1
            print("You and the computer tied!")
        elif round == -1:
            comCounter += 1
            print("The computer wins.")
        else:
            playCounter += 1
            print("You win!")
        more = continueGame()
    print("You won " + str(playCounter) + " game(s).")
    print("The computer won " + str(comCounter) + " game(s).")
    print("You tied with the computer " + str(tieCounter) + " time(s).")


# Calling the main function
main()
