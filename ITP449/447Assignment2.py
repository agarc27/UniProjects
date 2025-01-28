""" Andres Garcia Gomez
    ITP-449
    Assignment #2
    A program that prints the number of combinations of change
    for a given amount of money. 
"""

#This section of code is needed for the main fucntion to be called.
__name__ = '__main__'

# In this section, we define a function that allows us to get user input
# as to the amount of change we will be using.
def get_user_input():
    amount = input("Enter an amount of money: ")
    # We use a try except statement here to make sure the input is valid. If the input
    # is numerical, the value will get converted into a float and returned. If it's
    # invalid (i.e. a non-numerical string) it makes the user input a value again.
    # Unfortunately, it only asks for re-input once, so it is limited. 
    try:
        amount = float(amount) # Converts string from input() into float()
        return(amount)
    except:
        amount = input("That is not a valid number. Enter an amount of money: ")
        amount = float(amount) # Converts string from input() into float()
        return(amount)

# In this section, we define another function that will calculate 
# the number of combinations given an amount and return that value.
def get_total_combinations(amount):
    mod_amount = int(amount*100) # Due to how float math is iffy in Python,
    # we convert the change into an int by multiplying it by 100 (cents).
    combination_count = 0 # Counter to count all combinations

    # This section is composed of four for loops, one for each coin we are using,
    # with the outermost loop referring to quarters and the innnermost to pennies.
    # We find the range by dividing the amount by the coin amount, using int to 
    # round down the number, and then add 1 since range doesn't include the last value.
    for q in range(int(mod_amount/25)+1): #Quarters
        for d in range(int(mod_amount/10)+1): #Dimes
            for n in range(int(mod_amount/5)+1): #Nickels
                for p in range(mod_amount+1): #Pennies
    # At every range value for every coin, we multiply them by their amounts and
    # add them all together. If they match the amount, we tick the counter up by 1.
                    combo = q*25 + d*10 + n*5 + p*1 
                    if combo == mod_amount:
                        combination_count +=1
    return combination_count
    
# Finally, the main function introduces the user to the function of the program
# as well as uses the previous two functions.
def main():
    print("This program calculates the number of coin combinations") 
    print("you can create from a given amount of money.")
    print()
    change = get_user_input()
    total = get_total_combinations(change)
    print("The total number of combinations for", "$" + str(change), "is", str(total) +".")

# We need this to call the main function!!
if __name__ == '__main__':
    main()
