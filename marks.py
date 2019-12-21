#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: December 2019
# This program get's the marks from user and calculates the average

import random


def average(marks):
    # This calculates average of the marks

    total = 0
    items = 0

    # process
    for number in marks:
        total = total + number
        items = items + 1

    # Calculates average
    average = total / items

    # output
    return round(average)


def main():
    # This takes the user's marks and passes them to average()

    # This is a list to hold the 20 numbers
    marks = []
    final_average = 0
    mark = 0

    # process
    while mark != -1:
        # input
        mark = int(input("Mark: "))
        marks.append(mark)

    marks.pop()

    final_average = average(marks)
    print("The average is " + str(final_average))


if __name__ == "__main__":
    main()
