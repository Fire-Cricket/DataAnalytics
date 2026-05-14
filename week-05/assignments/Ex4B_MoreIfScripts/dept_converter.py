# Jordan R. Worrobah    
# 5/11/2026 
# Department Converter

deptCode = float(input("Enter your department code: "))

if deptCode == 1:
    print("Marketing")
elif deptCode == 5:
    print("Human Resources")
elif deptCode == 10:
    print("Accounting")
elif deptCode == 12:
    print("Legal")
elif deptCode == 18:
    print("IT")
elif deptCode == 20:
    print("Customer Relations")
else:
    print("Invalid department code")