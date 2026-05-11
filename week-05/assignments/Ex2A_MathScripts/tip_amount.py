#Jordan R. Worrobah
#Tip Amount Calculator  
#5/8/2026

if __name__ == "__main__":

    try:
        billAmount = float(input("Enter the bill amount: "))
        tipPercentage = float(input("Enter the tip percentage: "))

        tipAmount = billAmount * (tipPercentage / 100)

        print(f"The tip on a ${billAmount:.2f} restaurant bill is ${tipAmount:.2f}")
    except:
        print("Invalid input. Please enter a valid number.")