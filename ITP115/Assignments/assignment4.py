# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Assignment 4
# Description:
# This program identifies the largest and
# smallest numbers of the user's inputs.

# Variable to be used to secure the "do while" loop
another = "Y"

# The outer while loop that determines whether to redo the program again based on user input
while another == "Y" or another == "y":
    # The variables to be used in the program; they reset every time the system runs.
    smallest_number = 99999
    largest_number = 0
    count = 0
    sum_var = 0
    num = int(input("Input a number greater than or equal to 0 or -1 to quit: "))
    # The inner loop runs the program that finds the smallest, largest, and average number
    while num != -1:
        if num <= smallest_number:
            smallest_number = num
        if num >= largest_number:
            largest_number = num
        sum_var += num
        count += 1
        num = int(input("Input a number greater than or equal to 0 or -1 to quit: "))
    # Prints out the largest and smallest number as well as the average
    print("The largest number is ", largest_number)
    print("The smallest number is ", smallest_number)
    print("The average number is ", sum_var/count)
    # Confirmation to repeat the program again or not
    another = input("Would you like to enter another set of numbers (y/n)?: ")
    if another == "N" or another == "n":
        print("Goodbye!")
