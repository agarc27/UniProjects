# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Assignment 5
# Description: This program counts the number of letters
# and special characters there are in a user-inputted sentence.

# Variable to hold the entire alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Beginning of the program; asks for the number of times
# to run it
print("Character Distribution")
num = int(input("Enter the number of times to run: "))

# The first for loop; responsible for looping
# the program the desired number of times
for h in range(num):
    # User input for the sentence to be used
    sentence = input("Enter a sentence: ")
    SpCount = 0
    # Second for loop; loops the sentence to check for special characters
    for i in str.lower(sentence):
        if i in alphabet or i == " ":
            SpCount += 0
        else:
            SpCount += 1
    # If statement that prints the number of Special Characters
    if SpCount > 0:
        print("Special Characters: ", "*" * SpCount)
    else:
        print("Special Characters: NONE")
    # Outer loop responsible for going through each letter of the alphabet
    for i in alphabet:
        Count = 0
        # Inner loop responsible for counting how many of each letter
        # of the alphabet is found in the sentence.
        for j in str.lower(sentence):
            if i == j and j in str.lower(sentence):
                Count += 1
            else:
                Count += 0
        # If loop responsible for printing how many times each letter occurs.
        if Count > 0:
            print(str.capitalize(i) + ": " + "*" * Count)
        else:
            print(str.capitalize(i) + ": NONE")
