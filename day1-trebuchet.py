"""
--- Day 1: Trebuchet?! ---

Assumptions
No wrong inputs

Author: @abhinanddmanoj
Link: https://adventofcode.com/2023/day/1
"""

# Assumptions
# No wrong inputs

FILE = "input.txt"

with open("input.txt", "r") as f:
    sum = 0

    for line in f:
        ones, tens = "", ""

        for char in line:
            if char.isdigit():
                if tens == "":
                    tens = char
                else:
                    ones = char

        if ones == "":
            sum += int(tens+tens)
            print(tens+tens)
        else:
            sum += int(tens+ones)
            print(tens+ones)


print("total:", sum)
