print("Welcome to my Tip Calculator World")
bill = float(input("What is the total bill? $"))
percent_tip = int(input("How percentage of the bill do you want to give as a tip? "))
number_of_people = int(input("How many people are to pay the bill? "))

total_bill = bill + (bill * percent_tip/100)
splitted_bill = round(total_bill/number_of_people, 2)

if number_of_people == 1:
  print(f"You are to pay a amount of ${splitted_bill} alone")
else:
  print(f"The {number_of_people} of you to pay ${splitted_bill} each")