#Day 3 Exercise 4

#Pizza Order Practice

#Instructions
'''
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1

'''

'''
Hint
Think about what you've learnt about multiple if statements and see if you can reduce the number of lines of code while having the same functionality.
'''

#Code


print("Welcome to python pizza Deliveries !")
Pizza_type = input("What type of Pizza do you want ? S , M, or L ")
Bill = 0

if Pizza_type == "S":
    Bill = 15
    #print("Your Bill is $15.")
elif Pizza_type == "M":
    Bill = 20
    #print("Your bill is $20.")
else:
    Bill = 25
    #print("Your bill is $25.")

wants_pepperoni = input("Do you want Pepperoni? Y or N ")
if wants_pepperoni == "Y":
    if Pizza_type == "S":
        Bill = Bill + 2
    #print(f"Your Total bill is ${Bill}")
    else:
        Bill = Bill + 3

wants_extra_cheese = input("Do you want extra cheese ? Y or N ")
if wants_extra_cheese == "Y":
    Bill = Bill + 1
print(f"Your Total Bill is ${Bill}")
