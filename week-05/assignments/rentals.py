# Jordan R. Worrobah
# 5/10/2026
# Rental

from math import ceil

if __name__ == "__main__":
    try:
        people = int(input("Enter the number of tourists: "))

        if people <= 0:
            print("Please enter a positive number of tourists.")

        else:
            seatsPerVan = 15
            vanCost = 250

            vansNeeded = ceil(people / seatsPerVan)
            totalCost = vansNeeded * vanCost
            costPerPerson = totalCost / people

            print(
                f"Number of tourists: {people}\n"
                f"Vans needed: {vansNeeded}\n"
                f"Total rental cost: ${totalCost:.2f}\n"
                f"Cost per person: ${costPerPerson:.2f}"
            )

    except ValueError:
        print("Invalid input. Please enter a whole number.")