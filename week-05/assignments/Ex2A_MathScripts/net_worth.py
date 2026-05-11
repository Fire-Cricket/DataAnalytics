#Jordan R. Worrobah
#Net Worth Calculator   
#5/8/2026

if __name__ == "__main__":
    try:

        print("Welcome to the Net Worth Calculator!")
        print("Please enter the following information:")
        carValue =float(input("What is the value of your cars? "))
        houseValue =float(input("What is the value of your house? "))
        checkingAccountValue =float(input("What is the value of your checking account? "))
        savingsAccountValue =float(input("What is the value of your savings account? "))
        RetirementAccountValue =float(input("What is the value of your retirement account? "))
        otherAssetsValue =float(input("What is the value of your other assets? "))
        print("Now, please enter your debts:")
        houseLoanValue =float(input("What is the value of your house loan? "))
        carLoanValue =float(input("What is the value of your car loan? "))
        creditCardDebtValue =float(input("What is the value of your credit card debt? "))
        studentLoanValue =float(input("What is the value of your student loan? "))
        otherDebtsValue =float(input("What is the value of your other debts? "))
        assets = carValue + houseValue + checkingAccountValue + savingsAccountValue + RetirementAccountValue + otherAssetsValue
        debts = houseLoanValue + carLoanValue + creditCardDebtValue + studentLoanValue + otherDebtsValue
        netWorth = assets - debts
        print("\nCalculating your net worth...")
        print("Done!")
        print(f"Your total assets are: ${assets:.2f}")
        print(f"Your total debts are: ${debts:.2f}")
        print(f"Your net worth is: ${netWorth:.2f}")
    except:
        print("Invalid input. Please enter a valid number.")