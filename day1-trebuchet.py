"""
--- Day 1: Trebuchet?! ---

Assumptions
No wrong inputs

Author: @abhinanddmanoj
Link: https://adventofcode.com/2023/day/1
"""

import pdb


FILE = "input.txt"

with open("input.txt", "r") as f:
    sum = 0
    numbers = {
            "one"   : "1",
            "two"   : "2",
            "three" : "3",
            "four"  : "4",
            "five"  : "5",
            "six"   : "6",
            "seven" : "7",
            "eight" : "8",
            "nine"  : "9",
            }

    for line in f:
        ones, tens = "", ""

        # Modifying to include 'word' numbers
        modified = []

        # Contains only numeric values
        filtered_modified = []

        element = ""
        for char in line:
            if char.isdigit():
                modified.extend([element, char])
                element = ""

            else:
                element += char
        modified.append(element)

        for index in range(len(modified)):
            # Check if it is present in numbers
            element = modified[index]
            element_length = len(element)

            if element.isdigit():
                filtered_modified.append(element)
            elif element in numbers:
                filtered_modified.append(numbers[element])
            elif not element == "":
                
                # pdb.set_trace()
                char_index = 0
                while char_index <= element_length-3:
                    for offset in range(3, 6):
                        substr = element[char_index:char_index+offset]
                        if substr in numbers:
                            char_index += len(substr)
                            filtered_modified.append(numbers[substr])

                    char_index += 1


                """
                start = 0
                end = 0
                while end <= element_length:
                    substring = element[start:end]
                    if substring in numbers:
                        filtered_modified.append( numbers[substring] )
                        start += len(substring)-1
                        end += 1

                    end += 1

                """

                """

                for number in numbers:
                    if number in element:
                        # Convert all instances of current number string to a number
                        # should be at right position
                        for offset in range(element.count(number)):
                            filtered_modified.append(numbers[number])
                """
        # print(filtered_modified)

        # Removing non-numeric elements
        for element in filtered_modified:
            if not element.isdigit():
                filtered_modified.remove(element)

        if len(filtered_modified) == 1:
            print(filtered_modified[0]+filtered_modified[0])
            sum += int(filtered_modified[0]+filtered_modified[0])
        else:
            n = len(filtered_modified)
            print(filtered_modified[0]+filtered_modified[n-1])
            sum += int(filtered_modified[0]+filtered_modified[n-1])

        # print(modified)


        """
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
        """


print("total:", sum)
