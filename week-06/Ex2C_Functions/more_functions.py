# Jordan Worrobah
# 5/19/2026
# This program defines a few functions that perform various tasks.

def display_mailing_label(name, address, city, state, zip):
    return f"{name}\n{address}\n{city}, {state} {zip}"

def add_numbers(*numbers):
    total = sum(numbers)

    equation = " + ".join(str(number) for number in numbers)

    print(f"{equation} = {total}")

def display_receipt(total_due, amount_paid):
    change_due = amount_paid - total_due

    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")

    if change_due < 0:
        remaining_balance = total_due - amount_paid
        print(f"Remaining Balance: ${remaining_balance:.2f}")
    else:
        print(f"Change Due: ${change_due:.2f}")

# Test Code
display_mailing_label("John Doe", "123 Main St", "Anytown", "CA", "12345")
print()

display_mailing_label("Jane Smith", "456 Oak Ave", "Philadelphia", "PA", "19104")
print()


# Test add_numbers() three times
add_numbers(5)
add_numbers(5, 10)
add_numbers(2, 4, 6, 8, 10)
print()


# Test display_receipt() three times
display_receipt(50.00, 60.00)
print()

display_receipt(50.00, 50.00)
print()

display_receipt(50.00, 40.00)


