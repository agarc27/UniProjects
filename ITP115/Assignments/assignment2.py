# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Assignment 2
# Description:
# This program creates a Mad Libs styled story.
# It utilizes user input and creates outputs.

# Creates variables that are based on the user's inputs

princess_adjective = input("Enter adjective: ")
animal = input("Enter an animal (plural): ")
prince_adjective = input("Enter another adjective: ")
rats_verb = input("Enter an action verb without -ing: ")
princess_verb = input("Enter an action verb ending in -s: ")
animal_number = int(input("Enter a number: "))
age_number = int(input("Enter a number between 4-10: "))
year_number = int(input("Enter a number between 14-20: "))
weeks_float = float(input("Enter a number with a decimal: "))

# Prints out a story using the variables that were created by user input
print("Once upon a time, there lived a " + "\"" + princess_adjective + "\"" + " princess who lived in a")
print("tower guarded by " + "\"" + str(animal_number) + "\"" + " " + "\"" + animal + "\"" + "." + " She had been ")
print("locked in there at the age of " + "\"" + str(age_number) + "\"" + " by her father in hopes that she would ")
print("saved by a " + "\"" + prince_adjective + "\"" + " prince one day in the future. Now, after living there")
print("for " + "\"" + str(year_number) + "\"" + " years, she was ready to escape on her own. After ")
print("\"" + str(weeks_float) + "\"" + " weeks of preparation, she assembled a team of rats that were able to")
print("\"" + rats_verb + "\"" + " through the door. She " + "\"" + princess_verb + "\"" + " out of the ")
print("tower and into the sunset. Finally, after " + "\"" + str(age_number + year_number) + "\"" + " years,")
print("she was free.")

# Notes: Unsure if I did the floats and ints correctly since I had to make them strings to print

