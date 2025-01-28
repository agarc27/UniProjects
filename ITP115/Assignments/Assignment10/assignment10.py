# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Assignment 10
# Description: This program allows you to interact with
# a music library and manipulate it in multiple ways.

# Imports functions that will be used in the program
from MusicLibraryHelper import loadLibrary
from MusicLibraryHelper import saveLibrary
import random

# Defines a function that showcases the various actions you can perform
# with the program
def displayMenu():
    print("Manage Your Music Library")
    print("\ta) Display library")
    print("\tb) Display artists")
    print("\tc) Add an artist/album")
    print("\td) Delete an album")
    print("\te) Delete an artist")
    print("\tf) Generate a random playlist")
    print("\tg) Exit")

# Defines a function that prints out the available artists and their
# albums for the user.
def displayLibrary(dictionary):
    for key in dictionary:
        print("Artist: " + key)
        print("\tAlbums:")
        for i in dictionary[key]:
            print("\t\t", i)

# Defines a function that displays the artists available in the library
# to the user.
def displayArtists(dictionary):
    dictKeys = dict.keys(dictionary)
    print("Artists: ")
    for i in dictKeys:
        print("\t" + i)

# Defines a function that allows the user to add an album by a new artist
# or a preexisting artist into the library.
def addAlbum(dictionary):
    newArtist = input("Enter artist: ").title()
    newAlbum = input("Enter album: ").title()
    if newArtist not in dictionary:
        dictionary[newArtist] = newAlbum.split("\n")
        print(newAlbum)
    else:
        if newAlbum not in dictionary[newArtist]:
            dictionary[newArtist].append(newAlbum)

# Defines a function that allows the user to delete an album
# from the music library.
def deleteAlbum(dictionary):
    delArtist = input("Enter artist: ").title()
    delAlbum = input("Enter album: ").title()
    if delArtist in dictionary:
        if delAlbum in dictionary[delArtist]:
            dictionary[delArtist].remove(delAlbum)
            return True
        else:
            return False
    else:
        return False

# Defines a function that allows the user to delete an entire artist
# and their albums from the music library.
def deleteArtist(dictionary):
    delArtist2 = input("Enter artist to delete: ").title()
    if delArtist2 in dictionary:
        dictionary.pop(delArtist2)
        return True
    else:
        return False

# Defines a function that allows the user to generate a random playlist
# compiled by one random album from each artist in the library and save
# their changes to the music file.
def generateRandomPlaylist(dictionary):
    print("Here is your random playlist:")
    for i in dictionary:
        rand = random.choice(dictionary[i])
        print(rand + " by " + i)

# Defines the main function; allows the user to interact, change, and manipulate
# the music library using the functions listed above.
def main():
    fullDict = loadLibrary("music_library.dat")
    choice = ""
    while choice != "g":
        displayMenu()
        choice = input("Choice: ").lower()
        if choice == "a":
            displayLibrary(fullDict)
        elif choice == "b":
            displayArtists(fullDict)
        elif choice == "c":
            addAlbum(fullDict)
        elif choice == "d":
            we = deleteAlbum(fullDict)
            if we == True:
                print("Delete album success")
            else:
                print("Delete album failed")
        elif choice == "e":
            us = deleteArtist(fullDict)
            if us == True:
                print("Delete artist success")
            else:
                print("Delete artist failed")
        elif choice == "f":
            generateRandomPlaylist(fullDict)
        elif choice != "g":
            print("Invalid entry")
    musLibrary = input("Enter music library file name: ")
    saveLibrary(musLibrary, fullDict)
    print("Saved music library to " + musLibrary)

# Calls the main function
main()
