#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


#Tip Calculator
Total_bill = float(input("What was the total bill in dollar? "))
tip_perecntage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip = float((tip_perecntage/100) * Total_bill)
bill_added_tip = float(tip + Total_bill)
split_bill = float(bill_added_tip/people)
# # final_amount = round(split_bill, 2)
final_amount = "{:.2f}".format(split_bill)
print(f"Each person should pay: ${final_amount}")