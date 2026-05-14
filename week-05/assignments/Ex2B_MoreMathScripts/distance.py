# Jordan R. Worrobah    
# 5/10/2026
# Distance between two points
from math import sqrt

if __name__ == "__main__":
    try:
        x1 = float(input("Enter the x-coordinate of the first point: "))
        y1 = float(input("Enter the y-coordinate of the first point: "))
        x2 = float(input("Enter the x-coordinate of the second point: "))
        y2 = float(input("Enter the y-coordinate of the second point: "))

        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(f"The distance between the two points is: {distance:.3f}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values for the coordinates.")
        