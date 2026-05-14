# Jordan R. Worrobah
# 5/11/2026
# Pay Rules

pay_rate = float(input("Enter the hourly pay rate: "))
hours_worked = float(input("Enter the number of hours worked: "))


if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = 40 * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    total_pay = regular_pay + overtime_pay
    filingJointly = input("Are you filing jointly? (Yes/No): ").strip().lower()
    if filingJointly == "yes":
        match total_pay:
            case _ if total_pay <= 12000:
                tax = 0.0
                print("You are in the 0% tax bracket. Lucky you!")
            case _ if 12000 <= total_pay <= 24999.99:
                tax = 0.06
            case _ if 25000 <= total_pay <= 74999.99:
                tax = 0.11
            case _ if 75000 <= total_pay:
                tax = 0.20
        federalTax = total_pay * tax
    
    else:
         match total_pay:
            case _ if total_pay <= 12000:
                tax = 0.05
            case _ if 12000 < total_pay <= 24999.99:
                tax = 0.20
            case _ if 25000 < total_pay <= 74999.99:
                tax = 0.15
            case _ if 75000 < total_pay:
                tax = 0.20
    federalTax = total_pay * tax
    print(f"You worked {overtime_hours:.2f} hours of overtime.")
    print(f"Regular pay: ${regular_pay:.2f}")
    print(f"Overtime pay: ${overtime_pay:.2f}")
    print(f"Federal tax: ${federalTax:.2f}")
    print(f"The total pay for the week is: ${total_pay:.2f} OT worked")

else:
    total_pay = hours_worked * pay_rate

    filingJointly = input("Are you filing jointly? (Yes/No): ").strip().lower()
    if filingJointly == "yes":
        match total_pay:
            case _ if total_pay <= 12000:
                tax = 0.0
                print("You are in the 0% tax bracket. Lucky you!")
            case _ if 12000 <= total_pay <= 24999.99:
                tax = 0.06
            case _ if 25000 <= total_pay <= 74999.99:
                tax = 0.11
            case _ if 75000 <= total_pay:
                tax = 0.20
        federalTax = total_pay * tax
    
    else:
         match total_pay:
            case _ if total_pay <= 12000:
                tax = 0.05
            case _ if 12000 < total_pay <= 24999.99:
                tax = 0.20
            case _ if 25000 < total_pay <= 74999.99:
                tax = 0.15
            case _ if 75000 < total_pay:
                tax = 0.20
    federalTax = total_pay * tax

print(f"You worked {hours_worked:.2f} hours this period.")
print(f"Because you earn${pay_rate:.2f} per hour, your gross weekly pay is ${total_pay:.2f}.")
print(f"Your filing status is {'joint' if filingJointly == 'yes' else 'single'}.")
print (f"Your tax withholding for the week is ${federalTax:.2f}.")
print(f"Your net pay per week is ${total_pay - federalTax:.2f}.")
print(f"The tax rate applied to your income is {tax * 100:.2f}%.")
print(f"Your yearly gross pay is ${total_pay * 52:.2f}.")

