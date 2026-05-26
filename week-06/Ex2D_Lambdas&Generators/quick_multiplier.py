# Jordan R. Worrobah
# 5/19/2026
'''
doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler('banana'))
'''

def multiplier():

    value = input('Enter a value: ')

    num2 = int(input('Enter the multiplier: '))

    multiply = lambda x, y: x * y

    try:

        value = float(value)

        result = multiply(value, num2)

        print(f'Here is {value} multiplied by {num2}: {result}')

    except:

        result = multiply(value, num2)

        print(f'Here is "{value}" multiplied by {num2}: {result}')


multiplier()