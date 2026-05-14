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
    print(f"You worked {overtime_hours:.2f} hours of overtime.")
    print(f"Regular pay: ${regular_pay:.2f}")
    print(f"Overtime pay: ${overtime_pay:.2f}")
    print(f"The total pay for the week is: ${total_pay:.2f} OT worked")
else:
    total_pay = hours_worked * pay_rate
    print(f"The total pay for the week is: ${total_pay:.2f} no OT worked")