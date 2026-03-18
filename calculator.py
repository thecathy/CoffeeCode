# Start program
from decimal import Decimal, ROUND_HALF_UP  # import once

# Repeat:
while True:
    # Take inputs
    # Ask user for first number
    first_number = Decimal(input("Enter First Number: "))
    
    # Ask user for operation (+, −, ×, ÷)
    Operation = input("Enter the operation (+, -, *, /): ")
    
    # Ask user for second number
    second_number = Decimal(input("Enter Second Number: "))
    
    # If operation is addition → compute sum
    if Operation == "+":
        result = first_number + second_number

    # Else if subtraction → compute difference
    elif Operation == "-":
        result = first_number - second_number

    # Else if multiplication → compute product
    elif Operation == "*":
        result = first_number * second_number

    # Else if division:
    elif Operation == "/":
        if second_number == 0:
            print("Error: Division by zero")
            continue
        result = first_number / second_number

    # Else → show “invalid operation”
    else:
        print("Invalid operation")
        continue

    # Display result
    print("Result:", result)

    # Ask user if they want to continue
    choice = input("Do you want to continue? (yes/no): ").lower()

    # If user says no → stop program
    if choice != "yes":
        break