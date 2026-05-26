# Jordan R. Worrobah
# 5/26/2026

# ---------------- VALUE ERROR ----------------

try:
    number = int("hello")

except ValueError:
    print(
        "ValueError: You entered text where a number was expected."
    )

else:
    print(number)

finally:
    print("Let's try another one...\n")


# ValueError example

try:
    age = int("twenty")

except ValueError:
    print(
        "ValueError: Could not convert the string to an integer."
    )

else:
    print(age)

finally:
    print("Let's try another one...\n")


# ---------------- NAME ERROR ----------------

try:
    m = banana

except NameError:
    print(
        "NameError: Oops, looks like you tried to use "
        "an undefined variable."
    )

else:
    print(m)

finally:
    print("Let's try another one...\n")


# NameError example

try:
    print(score)

except NameError:
    print(
        "NameError: The variable does not exist."
    )

else:
    print(score)

finally:
    print("Let's try another one...\n")


# ---------------- TYPE ERROR ----------------

try:
    result = 5 + "10"

except TypeError:
    print(
        "TypeError: You cannot add an integer and a string together."
    )

else:
    print(result)

finally:
    print("Let's try another one...\n")


# TypeError example

try:
    item = len(50)

except TypeError:
    print(
        "TypeError: len() cannot be used on an integer."
    )

else:
    print(item)

finally:
    print("Let's try another one...\n")


# ---------------- SYNTAX ERROR ----------------

try:
    eval("if True print('Hello')")

except SyntaxError:
    print(
        "SyntaxError: Invalid Python syntax detected."
    )

else:
    print("Code worked.")

finally:
    print("Let's try another one...\n")


# SyntaxError example

try:
    eval("5 +")

except SyntaxError:
    print(
        "SyntaxError: Expression is incomplete."
    )

else:
    print("Code worked.")

finally:
    print("Let's try another one...\n")