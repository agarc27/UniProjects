# Andres Garcia, agarciag@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Assignment 3
# Description:
# This program creates a Harry Potter vending machine.
# It determines the change in Harry Potter currency
# and gives a discount.

# Variables for the Harry Potter Currency
base_knut = 1
base_sickle = 29
base_galleon = 493

# Vending Machine Menu and Asking what Choice Customer is Making using variable "choice"
print("Please select an item from the vending machine:")
print("\ta) Assortment of Candy for 11 sickles and 7 knuts")
print("\tb) Butterbeer for 2 sickles")
print("\tc) Quill for 6 sickles")
print("\td) Daily Prophet for 5 knuts")
choice = (input("Choice: "))

# Confirmation of selection and cost of item using variables
if choice == "a" or choice =="A":
    item = "Candy"
    cost = 11 * base_sickle + 7 * base_knut
    print("Thank you for selecting Candy!")
elif choice == "b" or choice == "B":
    item = "Butterbeer"
    cost = 2 * base_sickle
    print("Thank you for selecting Butterbeer!")
elif choice == "c" or choice == "C":
    item = "Quill"
    cost = 6 * base_sickle
    print("Thank you for selecting Quill!")
elif choice == "d" or choice == "D":
    item = "Daily Prophet"
    cost = 5 * base_knut
    print("Thank you for selecting Daily Prophet!")
else:
    item = "Butterbeer"
    cost = 2 * base_sickle
    print("You entered an invalid choice and thus the selected choice is a Butterbeer.")

# Payment Menu in Harry Potter Currency using variables "galleons", "sickles", and "knuts"
print("Please pay by entering the number of each coin:")
paid_galleons = int(input("\tNumber of galleons: "))
paid_sickles = int(input("\tNumber of sickles: "))
paid_knuts = int(input("\tNumber of knuts: "))
payment = base_galleon*paid_galleons + base_sickle*paid_sickles + base_knut*paid_knuts

# Cost of the Selected Item and Payment Provided in Knuts using variables
print("Cost in Knuts: ", cost)
print("Payment in Knuts: ", payment)

# Determines Sufficient Cost and Returns Change using Variables and Equations
if cost > payment:
    print("You did not enter enough money and will not receive the " + item + "!")
else:
    print("You have purchased " + item + "!")
    change = payment - cost
    print("Your change is:", )
    print("You will be given: ")
    print("Galleons: ", change//493)
    change = change % 493
    print("Sickles: ", change//29)
    change = change % 29
    print("Knuts: ", change)


