#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Jan 14 2022
# This program will asks the user to enter a number
# and after it will use a loop to calculate and display the square
# of numbers between 0 and the user's number.

def main():
    # get the user input
    user_string = input("Enter a whole number: ")
    print("")

    # check inputs
    try:
        user_number = int(user_string)
    except Exception:
        print("Invalid input, must be an integer.")
    else:
        # check if number is negative
        if user_number < 0:
            print("Number cannot be negative.")
        else:
            # calculate the squares
            for loop in range(user_number + 1):
                square = loop ** 2
                print("{} exponent 2 is {}". format(loop, square))
    finally:
        # finalize program
        print("")
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
