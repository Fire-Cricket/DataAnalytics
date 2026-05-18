# Jordan R. Worrobah    
# 5/13/2026
# Savings Goals

print("\n---------- Welcome to the savings calculator ----------")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            exit()

print() 

checkingBalance = get_float("Please insert your current checking account balance: ")

print("-------------------------------------------------------")

print() 

savingsBalance = get_float("Please insert your current savings account balance: ")

print("-------------------------------------------------------")

print() 

savingsGoal = get_float("Please insert your current savings goal: ")

print("-------------------------------------------------------")

print() 

weeklySavings = get_float("Please insert your weekly savings amount: ")

print("-------------------------------------------------------")

bankBalance = savingsBalance + checkingBalance

week = 0

# treatedMyself = False

passedHalfway = False

while bankBalance < savingsGoal:
    week +=1
    halfway = savingsGoal / 2
    bankBalance = weeklySavings + bankBalance

    if halfway <= bankBalance and not passedHalfway:
        print(f"Almost there! Week {week} my balance is up to ${bankBalance:.2f}.")
        passedHalfway = True
    if week <= 10:
        print(f"Week {week}: This week my balance increased to ${bankBalance}.")

'''
    if bankBalance >= savingsGoal * 0.75 and not treatedMyself:

        treat = 25
        bankBalance -= treat
        treatedMyself = True


        print(f"So close! After treating myself, my balance is up to ${bankBalance:.2f}.")
'''

print(f"Goal met by week: {week}! My current balance is ${bankBalance}.")