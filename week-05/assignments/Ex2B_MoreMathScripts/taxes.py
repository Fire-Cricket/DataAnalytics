#Jordan R. Worrobah
#Taxes Calculator
#5/10/2026


if __name__ == "__main__":
    try:
        hours = float(input("Enter your hours worked: "))
        rate = float(input("Enter your hourly pay rate: "))
        if hours < 0 or rate < 0:
            print("Please enter positive numbers only.")

        else:
            pay = hours * rate
            tax = 0.23
            taxed = pay * tax
            total = pay - taxed
            print(
                f"Your pay is {format(pay, '.2f')} dollars before taxes. "
                f"Your tax amount is {format(taxed, '.2f')} dollars. "
                f"Your total pay including taxes is {format(total, '.2f')} dollars."
            )
    except ValueError:
        print("Invalid input. Please enter valid numbers.")