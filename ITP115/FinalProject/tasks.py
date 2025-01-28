# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Final Project
# tasks.py
# Description: This file will define functions to be called
# for in other files within this directory; in this case,
# the functions will be used to perform various tasks.

# Defines a function that allows us to create dictionaries holding
# information about each park and keeps those dictionaries in a list.
def readParksFile(fileName = "national_parks.csv"):
    openFile = open(fileName, "r")
    header = openFile.readline().strip()
    headerList = header.split(",")
    parksList = []
    # print(headerList)
    for line in openFile:
        line = line.strip()
        lineList = line.split(",")
        # print(lineList)
        parksDict = {}
        for num in range(len(headerList)):
            parksDict[headerList[num]] = lineList[num]
        parksList.append(parksDict)
    openFile.close()
    # print(parksList)
    return parksList

# Defines a function that allows us to convert a string of a numerical
# date into a string of a written-out date.
def convertDate(dateStr):
    monthsList = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    dateList = dateStr.split("-")
    month = monthsList[int(dateList[1]) - 1]
    day = dateList[2]
    year = dateList[0]
    # print(dataList)
    newDate = month + " " + day + ", " + year
    return newDate

# Defines a function that allows us to loop through all the parks
# to find which is the largest by acreage.
def getLargestPark(parksList):
    largestArea = 0
    for i in parksList:
        if int(i["Acres"]) > largestArea:
            largestArea = int(i["Acres"])
            largestPark = i["Code"]
    return largestPark

