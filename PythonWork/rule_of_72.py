# Jordan R. Worrobah
# 5/9/2026
# Rule of 72 Calculator

if __name__ == "__main__":
    try:
        savings = float(input("Enter your current savings amount: "))
        rate = float(input("Enter the annual interest rate (%): "))

        if savings <= 0 or rate <= 0:
            print("Please enter positive numbers only.")

        else:
            years = 72 / rate
            doubled_balance = savings * 2

            rate_decimal = rate / 100

            print(
                f"Your current savings is {format(savings, '.2f')}. "
                f"At a {format(rate_decimal, '.0%')} interest rate, "
                f"your savings account will be worth {format(doubled_balance, '.2f')} "
                f"in {format(years, '.1f')} years."
            )

    except ValueError:
        print("Invalid input. Please enter valid numbers.")