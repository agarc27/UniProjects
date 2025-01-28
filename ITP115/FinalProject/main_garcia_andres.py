# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Final Project
# main_garcia_andres.py
# Description: This file will utilize the functions
# defined in the other files in the directory in order
# to run a program that allows you to find information on
# US National Parks.

# Imports functions from the tasks and interface files
# to be used in the program.
import tasks
import interface

# Defines a main function that runs the program and allows the user to
# perform various tasks with the file such as finding the largest park
# or using specific search terms to find parks.
def main():
    print("National Parks")
    parksList = tasks.readParksFile()
    menuDict = interface.getMenuDict()
    choice = ""
    while choice != "Q":
        interface.displayMenu(menuDict)
        choice = interface.getUserChoice(menuDict)
        if choice == "A":
            interface.printAllParks(parksList)
        elif choice == "B":
            interface.printParksInState(parksList)
        elif choice == "C":
            interface.printLargestPark(parksList)
        elif choice == "D":
            interface.printParksForSearch(parksList)

# Calls the main function.
main()
