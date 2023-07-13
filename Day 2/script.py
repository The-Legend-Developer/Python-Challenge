def convert_to_words(num):
  if num == 0:  
    return "zero"  
  ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
  tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
  teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
  words = "" 

  if num>= 1000:  
    words += ones[num // 1000] + " thousand "  
  num %= 1000  
  if num>= 100:  
    words += ones[num // 100] + " hundred "  
  num %= 100  
  if num>= 10 and num<= 19:  
    words += teens[num - 10] + " "  
    num = 0  
  elif num >= 20: 
    words += tens[num // 10] + " "  
  num %= 10
  if num>= 1 and num<= 9:  
    words += ones[num] + " "  
  return words.strip()  

print("Welcome to my Tip Calculator World")
bill = float(input("What is the total bill? $"))
percent_tip = int(input("How percentage of the bill do you want to give as a tip? "))
number_of_people = int(input("How many people are to pay the bill? "))

total_bill = bill + (bill * percent_tip/100)
splitted_bill = round(total_bill/number_of_people, 2)

if number_of_people == 1:
  print(f"You are to pay a amount of ${splitted_bill} alone")
else:
  print(f"The {convert_to_words(number_of_people)} of you to pay ${splitted_bill} each")