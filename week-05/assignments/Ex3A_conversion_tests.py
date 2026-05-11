# Description: This script tests various numeric conversion techniques 
# Author: Jordan R. Worrobah
# Date: 5/10/2026

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

aFloat = float(a)  # Works: converts string to float
aFloatInt = int(float(a))  # Works: converts float to int

aSliced = a[1:6]  # Gets "101.1"
aSlicedFloat = float(aSliced)  # Converts sliced string to float


bInt = int(b)  # Works: valid integer string
bFloat = float(b)  # Works: valid float conversion

bSliced = b[:]  # Gets "55"
bSlicedInt = int(bSliced)  # Converts sliced string to integer

# cInt = int(c)  # ValueError: contains letters
# cFloat = float(c)  # ValueError: contains letters

cSliced = c[:3]  # Gets "402"
cSlicedInt = int(cSliced)  # Converts sliced string to integer

# dInt = int(d)  # ValueError: contains letters
# dFloat = float(d)  # ValueError: contains letters

dSliced = d[7]  # Gets "5"
dSlicedInt = int(dSliced)  # Converts sliced string to integer

# Strip method examples

print(a.strip(), type(a.strip()))
print(d.strip(), type(d.strip()))

# Original variables

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Converted variables

print(aFloat, type(aFloat))
print(aFloatInt, type(aFloatInt))
print(aSliced, type(aSliced))
print(aSlicedFloat, type(aSlicedFloat))

print(bInt, type(bInt))
print(bFloat, type(bFloat))
print(bSliced, type(bSliced))
print(bSlicedInt, type(bSlicedInt))

print(cSliced, type(cSliced))
print(cSlicedInt, type(cSlicedInt))

print(dSliced, type(dSliced))
print(dSlicedInt, type(dSlicedInt))

'''
a)
This will work because on a ='55' because it is a valid integer string. 
But, if we tried to convert c = '402 Stevens' to an integer, 
it would raise a ValueError because it contains non-numeric characters.

b)
The conversion of a to a float will succeed on variable b and a because it is a valid floating-point number.
However, this will make variable b a float instead of an integer, which may not be the intended outcome.

c)
This makes variable a3 an integer by first converting the string to a float and then to an integer.

d)

'''