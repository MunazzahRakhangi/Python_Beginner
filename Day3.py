#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#It will take your current age as the input and output a message with our time left in this format:

#You have x days, y weeks, and z months left.

#Where x, y and z are replaced with the actual calculated numbers.

#Hint
#There are 365 days in a year, 52 weeks in a year and 12 months in a year.
#Try copying the example output into your code and replacing the relevant parts so that the sentence is formated the same way.

#Life in weeks
age = input("What is your current age? ")
age_as_int = int(age)
year_remaining = 50 - age_as_int
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remaining = year_remaining * 12
message = print(f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left.")
print(message)