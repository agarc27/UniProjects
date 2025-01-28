# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Assignment 9
# Description: This program allows you to type a word in English and
# translate it into one of fourteen different languages.

# Defines a function that registers all the various languages used in the file
# and converts them into a list
def getAllLanguages(fileName = 'languages.csv'):
    openFile = open(fileName, "r")
    header = openFile.readline()
    for line in openFile:
        line.strip()
    openFile.close()
    headerList = header.strip()
    headerList = headerList.split(",")
    return headerList

# Defines a function that displays the possible languages the user can translate
# and asks them to choose one.
def getTranslationLanguage(languagesList):
    langList1 = languagesList[1:7]
    langList2 = languagesList[8:]
    print("Translate English words to one of the following languages:")
    print(langList1)
    print(langList2)
    chosenLang = input("Enter a language: ")
    chosenLang = chosenLang.strip()
    while chosenLang.capitalize() not in langList1 and chosenLang.capitalize() not in langList2:
        print("This program does not support", chosenLang.capitalize())
        chosenLang = input("Enter a language: ")

    return chosenLang.capitalize()

# Defines a function that creates a file that has all the available words
# in the list in the appropriate language
def readDataFile(languagesList, languageStr = 'English', fileName = 'languages.csv'):
    wordList = []
    file = open(fileName, "r")
    file.readline()
    num = int(languagesList.index(languageStr))
    for line in file:
        line.strip()
        line = line.split(",")
        think = line[num]
        wordList.append(think)
    file.close()
    return wordList

# Defines a function that creates an album named after the chosen language
# and keeps track of what words have been translated
def createTextFile(language = 'Italian'):
    transFile = language + ".txt"
    trans = open(transFile, "w")
    print("Words translated from English to " + language, file = trans)
    trans.close()

# Defines a function that is able to translate the word
# from English to the chosen langauge
def translateWords(englishList, translationList, language):
    firstFile = language + ".txt"
    choice = "Y"
    opener = open(firstFile, "a")
    while choice == "Y":
        word = input("Enter a word to translate: ")
        if word not in englishList:
            print(word, "is not in the English list")
        else:
            num = englishList.index(word)
            transWord = translationList[num]
            if transWord == "-":
                print(word, "did not have a translation.")
            else:
                print(word, "translated to", transWord)
                print(word + "=" + transWord, file = opener)
                choice = input("Another word? (Y or N) ")
                choice = choice.strip()
                choice = choice.capitalize()
    opener.close()
    print("Translated words have been saved to " + firstFile)

# Defines a main function that translates a chosen word into a language chosen
# from the user; the translated words are then put into a file
def main():
    print("Language Translator")
    langList = getAllLanguages()
    englishList = readDataFile(langList)
    choiceLang = getTranslationLanguage(langList)
    choiceList = readDataFile(langList, choiceLang)
    createTextFile(choiceLang)
    translateWords(englishList, choiceList, choiceLang)

# Calls the main function
main()
