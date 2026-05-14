# Jordan R. Worrobah
# 5/12/2026
# Min and Max

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
c = float(input("Enter one more number: "))

if a >= b and a >= c:
    max_value = a
elif b >= a and b >= c:
    max_value = b
else:
    max_value = c

if a <= b and a <= c:
    min_value = a
elif b <= a and b <= c:
    min_value = b
else:
    min_value = c

print(f"The maximum value is: {max_value:.2f}")
print(f"The minimum value is: {min_value:.2f}") 

