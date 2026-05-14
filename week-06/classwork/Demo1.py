# Jordan R. Worrobah
# 5/12/2026
'''
def greeting():
    name = input("What is your name? ")
    print(f"Hello, {name}!")
greeting()
'''
'''
def greeting():
    name = input('Please enter your name:')
    return name

result = greeting()
print(f"Hello, {result}!")
'''
'''
def greeting(name, city, hobby):
    return name, city, hobby

result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print(type(result))

print(f"Hello, {result[0]}! You are from {result[1]} and you enjoy {result[2]}.")
'''
