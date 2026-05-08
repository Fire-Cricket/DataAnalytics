'''
num = input("Enter a number: ")
num = float(num)

if num == int(num):
    print("You entered an integer.")
    if num > 0:
        print("Positive")
    elif num == 0:
        print("Zero")
    elif num < 0:
        print("Negative")
    print("Done")
else:
    print("You did not enter an integer dummy.")
'''

'''
num = 5 
while num > 0:
    print(num)
    num -= 1

for num in range(5):
    print("Hello")
'''

'''
for item in [1, 2, 3, 4]:
    if item == 2:
        print(item)
        break
'''

score = input("Enter your score: ")

try:
    score = int(score)

   
    if score < 0:
        print("Please enter a positive number.")
    else:
        if score >= 90:
            print(f"Grade: {score} -- Grade: A")
        elif score >= 80:
            print(f"Grade: {score} -- Grade: B")
        elif score >= 70:
            print(f"Grade: {score} -- Grade: C")
        elif score >= 60:
            print(f"Grade: {score} -- Grade: D")
        else:
            print(f"Grade: {score} -- Grade: F")

except:
    print("You did not enter an integer dummy.")