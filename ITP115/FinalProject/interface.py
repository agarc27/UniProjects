# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Final Project
# interface.py
# Description: This file will define functions to be called
# for in other files within this directory; in this case,
# the functions will be used for the program's interface.

# Imports the functions from the tasks.py file that will
# be utilized within some of these functions.
from tasks import convertDate
from tasks import getLargestPark

# Defines a function that returns a dictionary to be used
# for the menu of the program.
def getMenuDict():
    menuDict = {"A": "All national parks", "B": "Parks in a particular state", "C": "The largest park",
                "D": "Search for a park", "Q": "Quit"}
    return menuDict

# Defines a function that displays the menu of the program
# to the user.
def displayMenu(menuDict):
    menuKeys = menuDict.keys()
    for i in menuKeys:
        print(i + " -> " + menuDict[i])

# Defines a function that verifies if the user's menu choice
# is valid and returns a capitalized version of their choice.
def getUserChoice(menuDict):
    menuKeys = menuDict.keys()
    choice = ""
    while choice not in menuKeys:
        choice = input("Choice: ").upper()
    return choice

# Defines a function that prints information on all parks
# within the file. Info includes name, code, location, acres, and date established.
def printAllParks(parksList):
    for i in parksList:
        print(i["Name"] + " " + "(" + i["Code"] + ")")
        print("\tLocation: " + i["State"])
        print("\tArea: " + i["Acres"] + " acres")
        print("\tDate Established: " + convertDate(i["Date"]))

# Defines a function that verifies if the user's input for a state
# is valid in terms of length (2 letters).
def getStateAbbr():
    stateChoice = input("Enter a state: ").strip()
    while len(stateChoice) != 2:
        print("Need the two letter abbreviation")
        stateChoice = input("Enter a state: ").strip()
    return stateChoice.upper()

# Defines a function that prints all the parks within a specific state
# depending on the user's choice in the getStateAbbr() function.
def printParksInState(parksList):
    state = getStateAbbr()
    counter = 0
    for i in parksList:
        if state == i["State"]:
            print(i["Name"] + " " + "(" + i["Code"] + ")")
            print("\tLocation: " + i["State"])
            print("\tArea: " + i["Acres"] + " acres")
            print("\tDate Established: " + convertDate(i["Date"]))
            counter += 1
    if counter == 0:
        print("There are no national parks in " + state + " or it is not a valid state.")

# Defines a function that prints out information on the largest park, including
# description, bu using the getLargestPark function from tasks.py.
def printLargestPark(parksList):
    largestPark = getLargestPark(parksList)
    for i in parksList:
        if largestPark == i["Code"]:
            print(i["Name"] + " " + "(" + i["Code"] + ")")
            print("\tLocation: " + i["State"])
            print("\tArea: " + i["Acres"] + " acres")
            print("\tDate Established: " + convertDate(i["Date"]))
            print("\tDescription: " + i["Description"] + "...\"")

# Defines a functions that prints one or more parks and their information
# depending on a search parameter the user provides; the search term
# is only checked for within the code, name, or description of the park.
def printParksForSearch(parksList):
    searchTerm = input("Enter text for searching: ")
    counter = 0
    for i in parksList:
        if searchTerm in i["Code"]:
            print(i["Name"] + " " + "(" + i["Code"] + ")")
            print("\tLocation: " + i["State"])
            print("\tArea: " + i["Acres"] + " acres")
            print("\tDate Established: " + convertDate(i["Date"]))
            print("\tDescription: " + i["Description"] + "...\"")
            counter += 1
        if searchTerm in i["Name"]:
            print(i["Name"] + " " + "(" + i["Code"] + ")")
            print("\tLocation: " + i["State"])
            print("\tArea: " + i["Acres"] + " acres")
            print("\tDate Established: " + convertDate(i["Date"]))
            print("\tDescription: " + i["Description"] + "...\"")
            counter += 1
        if searchTerm in i["Description"]:
            print(i["Name"] + " " + "(" + i["Code"] + ")")
            print("\tLocation: " + i["State"])
            print("\tArea: " + i["Acres"] + " acres")
            print("\tDate Established: " + convertDate(i["Date"]))
            print("\tDescription: " + i["Description"] + "...\"")
            counter += 1
    if counter == 0:
        print("There are no national parks for the search text of '" + searchTerm + "'.")
