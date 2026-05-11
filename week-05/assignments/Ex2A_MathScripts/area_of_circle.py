#Jordan R. Worrobah
#Area of a Circle Calculator
#5/9/2026
from math import pi

if __name__ == "__main__":
    try: 
        birthday = float(input("Enter your birthday (Just the day): "))

        radius = birthday / 2

        area = pi * radius ** 2
        print(f"Your birthday is {birthday:.2f}")
        print(f"The radius of the circle is {radius:.2f}")
        print(f"The area of a circle with radius {radius:.2f} is {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()