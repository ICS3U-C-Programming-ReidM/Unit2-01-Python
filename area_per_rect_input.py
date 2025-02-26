#!/usr/bin/env python3

# Created by: Reid MacLean
# Created on: February 24, 2025
# This program calculates and displays the area and perimeter for a given user input

def main():
    # gives the user input for the length and width
    length = int(input("What is the length of the rectangle? (cm) "))
    width = int(input("What is the width of the rectangle? (cm): "))

    # calculates the area and perimeter with the given input
    print ("area is {}cm^2.".format(length * width))
    print ("perimeter is {}cm".format((2 * length) + (2 * width)))

if __name__ == "__main__":
    main()
