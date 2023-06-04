#Day 5 Exercise 5

# Love Calculator
#Instructions

'''

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

'''

'''
Hint
The lower() function changes all the letters in a string to lowercase.
The count() function will give you the number of times a letter occurs in a string.
'''

#Code

print("Welcome to the love calculator !")

Name1 = input("What is Your Name? ")
Name2 = input("What is their Name? ")

combined_Strings = Name1 + Name2
lowercase_String = combined_Strings.lower()

T = lowercase_String.count("t")
R = lowercase_String.count("r")
U = lowercase_String.count("u")
E = lowercase_String.count("e")

true = T + R + U + E

L = lowercase_String.count("L")
O = lowercase_String.count("O")
V = lowercase_String.count("V")
E = lowercase_String.count("E")

love = L + O + V + E

love_score = int(str(true) + str(love))

if (love_score <10) or (love_score > 90):
    print(f"Your score is {Love_score}, you go togrther like coke and mentos.")
elif(love_score >=40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
