#Day 8 
# Exercise 1 - Paint Area Calculator

#Instructions

'''
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 * 4) / 5

                           = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

Hint
To round up a number:

https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python

Make sure you name your function/parameters the same as when it's called on the last line of code.

'''

#Code

import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height, width, cover):
    area = float(height*width)
    num_of_cans = math.ceil(area/cover)
    print(f"You'll need {num_of_cans} cans of paint")


paint_calc(height=test_h, width=test_w, cover=coverage)
