# DAY 3 PROJECT 2

#BMI 2.0

#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
'''
It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''

'''
Warning you should round the result to the nearest whole number. 
The interpretation message needs to include the words in bold from the interpretations above. 
e.g. underweight, normal weight, overweight, obese, clinically obese.
'''

#Code

height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
BMI = int(weight/(height*height))
bmi = round(BMI)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, You are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, You are obese")
else: 
    print(f"Your BMI is {bmi}, You are clinically obese.") 