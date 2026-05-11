# Jordan R. Worrobah
# Celsius to Fahrenheit Converter
# 5/9/2026

if __name__ == "__main__":
    try:
        celsius = float(input("Enter the temperature in Celsius: "))

        fahrenheit = (celsius * 9 / 5) + 32

        print(
            f"{format(celsius, '.1f')}°C is equal to "
            f"{format(fahrenheit, '.1f')}°F"
        )

    except ValueError:
        print("Invalid input. Please enter a valid number.")