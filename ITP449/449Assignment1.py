""" Andres Garcia Gomez
    ITP-449
    Assignment #1
    A program that, given someone's name and date of birth, will
    calculate how old they are.
"""

# Needed to make the main function run.
__name__ = '__main__'


def main():
# This beginning section houses most of the variables that will be used
# in the program.
    small_months = "46911" #String of months that have 30 days
    large_months = "135781012" #String of months that have 31 days
    unique_month = "2" #String to specify the month of February
    birth_suffix = "" #Empty string that will have the proper day suffix assigned
    month_name = "" #Empty string that will have proper month name assigned

# This section of code is the actual program, asking for inputs from the user,
# beginning with the user's name and birth year.
    name = input("Hello! Enter your name: ") 
    birth_year = int(input("Enter the year you were born: "))
    birth_month = int(input("Enter the month of the year you were born: ")) 
    birth_day = int(input("Enter the day of the month you were born: "))

# This section of code runs various checks to see if the input provided by the user
# are valid for each time variation (year, month, day), beginning with month
    if abs(birth_month)>12 or birth_month<=0:
        print() # Empty print statment; used to beautify the output (and pass
        # the autotest). Any subsequent empty print statements are likewise for the same purpose.
        print(birth_month, "is an invalid month. (It doesn't exist.)")
        print("Please restart the program.")
    else:

#After determing the month is valid, we run through every possible value it can
#be so that we can assign the value to the respective month (this is easier with Lists).
        if birth_month == 1:
            month_name = "January"
        elif birth_month == 2:
            month_name = "February"
        elif birth_month == 3:
            month_name = "March"
        elif birth_month == 4:
            month_name = "April"
        elif birth_month == 5:
            month_name = "May"
        elif birth_month == 6:
            month_name = "June"
        elif birth_month == 7:
            month_name = "July"
        elif birth_month == 8:
            month_name = "August"
        elif birth_month == 9:
            month_name = "September"
        elif birth_month == 10:
            month_name ="October"
        elif birth_month == 11:
            month_name = "November"
        else:
            month_name = "December"

#Once done with the check for the month, we run another check to see if the day inputted
#by the user works for that month. We have three seperate statements for each scenario:
#February as it has 28 days (no Leaps), shorter months with 30 days, 
# and larger months with 31 days.
        if str(birth_month) in unique_month and abs(birth_day)>28:
            print()
            print(birth_day, "is an invalid day. (It doesn't exist in Feburary.)")
            print("Please restart the program.")
        elif str(birth_month) in large_months and abs(birth_day)>31:
            print()
            print(birth_day, "is an invalid day. (It doesn't exist in",
            month_name + ".)")
            print("Please restart the program.")
        elif str(birth_month) in small_months and abs(birth_day)>30:
            print()
            print(birth_day, "is an invalid day. (It doesn't exist in",
            month_name + ".)")
            print("Please restart the program.")
        else:
#Finally, we do one final check on the year, seeing if the year inputted is valid. We have
#three separate checks for three different scenarios: one for a year greater than 2024, one 
#for the year 2023 with a month past January, and finally one for January 2023 with a day
#past the 21st. Any of these three scenarios would result in future dates that have not happened.
            if abs(birth_year) > 2023:
                print()
                print("You have entered a birthdate which has not yet happened.")
                print("Please restart the program.")
            elif abs(birth_year) == 2023 and abs(birth_month) > 1:
                print()
                print("You have entered a birthdate which has not yet happened.")
                print("Please restart the program.")
            elif abs(birth_year) == 2023 and abs(birth_month) == 1 and abs(birth_day) > 21:
                print()
                print("You have entered a birthdate which has not yet happened.")
                print("Please restart the program.")
            else:
#After all major checks have been done, we assign a suffix to the birthday depending
#on the input. There are only 7 values that don't end in -th, so we write different 
#statements to see if those are the inputted value before defaulting to -th.
                temp_age = 2023 - birth_year
                if birth_day == 1 or birth_day == 21 or birth_day == 31:
                    birth_suffix = "st"
                elif birth_day == 2 or birth_day == 22:
                    birth_suffix = "nd"
                elif birth_day == 3 or birth_day == 23:
                    birth_suffix = "rd"
                else:
                    birth_suffix = "th"
                
#The output of the function then occurs here, with a message using the inputted name
#followed by a declaration of their birth date and then their age. 
                print("\n" "Hello", name + "!")
                print("You were born in", birth_year, "on the", str(birth_day)+birth_suffix,
                "of", month_name + ".")

#The variable temp_age holds the number of the person's age for that year. However, because
#the age calculator is centered around the due date, we check to see if the user's birth date 
#has occurred yet in order to preserve accuracy. This is done by first checking if their birth
#date is in January (1) before checking if it has occurred before the 21st.
                temp_age = 2023 - birth_year
                if birth_month > 1:
                    temp_age -=1
                    print("You are", temp_age, "years old.")
                else:
                    if birth_day > 21:
                        temp_age -=1
                        print("You are", temp_age, "years old.")
                    else:
                        print("You are", temp_age, "years old.") 

#The code we were told to keep that runs the main function.
if __name__ == '__main__':
    main()
