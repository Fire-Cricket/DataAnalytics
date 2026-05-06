# Jordan R. Worrobah
# 5/6/2026
'''
name = input ('Enter your name: ')
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3

print(f"Hello {name}! The average of {num1}, {num2} and {num3} is: {average}")
'''

'''
num2 = '25'
print(type(num2))
print(type(int(num2)))
'''
'''
price = float(input("Enter the price of the item: "))
discount = float(input("Enter the discount percentage: "))
discountamount = price * (discount / 100)
print(f"The discount amount is: ${discountamount:.2f}")
print(f"The final price after discount is: ${price - discountamount:.2f}")
'''

'''
meal = eval(input("Enter the cost of the item: "))
tip = 0.20
tax = 0.0825

tipamount = meal * tip
taxamount = meal * tax

totalCost = meal + tipamount + taxamount

print("----- Meal Cost Breakdown -----")
print(f"{'Meal Cost':<15} ${meal:<15.2f}")
print(f"{'Tip (20%)':<15} ${tipamount:<15.2f}")
print(f"{'Tax (8.25%)':<15} ${taxamount:<15.2f}")
print("-------------------------------")
print(f"{'Total Cost':<15} ${totalCost:<15.2f}")
'''

classmates = ["Leon Poulson", "Dimitri", "Ivana Nwaboi"]

print(f"My classmates are {classmates[0]}, {classmates[1]}, and {classmates[2]}.")