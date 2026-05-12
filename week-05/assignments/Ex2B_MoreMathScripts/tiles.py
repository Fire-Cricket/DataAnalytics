# Jordan R. Worrobah
# 5/10/2026
# Tile box calculator

from math import ceil

if __name__ == "__main__":
    try:
        length = float(input("Enter the length of the room in feet: "))
        width = float(input("Enter the width of the room in feet: "))

        if length <= 0 or width <= 0:
            print("Please enter positive numbers only.")
        else:
            area = length * width
            tiles_needed = area * 1.10
            boxes_needed = ceil(tiles_needed / 12)

            print(f"Room area: {area:.2f} square feet")
            print(f"Tiles needed with 10% extra: {tiles_needed:.2f}")
            print(f"Total boxes to buy: {boxes_needed}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")