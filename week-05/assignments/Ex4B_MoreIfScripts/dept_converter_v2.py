# Jordan R. Worrobah    
# 5/11/2026 
# Department Converter

deptCode = float(input("Enter your department code: "))

match deptCode:
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        print("Invalid department code")

# It is easier to use the match statement for this type of problem because it is more concise and easier to read. 
# The match statement allows us to check for multiple conditions in a more organized way, 
# whereas using multiple if-elif statements can become cumbersome and harder to follow.