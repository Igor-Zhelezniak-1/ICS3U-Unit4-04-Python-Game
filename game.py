#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is game

import random


def main():

    secret_number = random.randint(0, 9)  # a number between 0 and 9
    # process & output
    while True:
        integer = input("Enter the number between 0-9: ")
        try:
            number = int(integer)
            if number == secret_number:
                print("You guessed correct!")
                break
            elif number < 0 or number > 9:
                print("You need enter number 0-9")
            elif number > secret_number:
                print("Secret number less than {0}".format(number))
            elif number < secret_number:
                print("Secret number greater than {0}".format(number))

        except Exception:
            print("This was not a number")
        finally:
            print("")
    print("Thanks for playing")


if __name__ == "__main__":
    main()
