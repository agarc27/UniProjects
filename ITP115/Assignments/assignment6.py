# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Assignment 6
# Description: The program displays a scrambled word
# and counts the number of guesses it takes for the user
# to decipher it.

# Importing the random module
import random

# The list of words and hints that will be used in the jumble
wordList = ["penguin", "sword", "shoes", "yellow"]
hintList = ["An Arctic animal.", "A knight's weapon of choice.",
            "Like clothes, but for your feet.", "The color of bananas."]

# The variables to be used in the program
chosenWord = random.choice(wordList)
chosenHint = hintList[wordList.index(chosenWord)]
chosenList = list(chosenWord)
empty = ""
counter = 1
guess = ""

# While loop that scrambles the word until its unrecognizable
while len(chosenList) > 0:
    letter = random.choice(chosenList)
    empty += letter
    chosenList.remove(letter)
print("The jumbled word is", "\"" + empty + "\"")

# While loop that counts the number of guesses it takes to solve
# the word as well as offers a hint
while guess != chosenWord:
    guess = input("Enter your guess: ").lower()
    if guess != chosenWord:
        counter += 1
        print("That is not correct.")
        hintChoice = input("Do you want a hint (y or n)?: ")
        if hintChoice == "Y" or hintChoice == "y":
            print("The hint is ", "\"" + chosenHint + "\"")

# Ending display that tells you attempted number of guesses
print("You got it!")
print("It took you " + str(counter) + " guesses!")
