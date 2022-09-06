from animals import *

choice = 0

while choice != "exit":
    try:
        choice = input(
            "Please enter the number of the habitat you would "
            "like to view: > "
            ).lower()
        print(animals[int(choice)])

    except IndexError as outOfBounds:
        print("There is no habitat with that number.")

    except ValueError as NaN:
        print("Value is not a valid number.")

print("See you later!")
