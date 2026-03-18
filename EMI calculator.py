from decimal import Decimal, ROUND_HALF_UP  # import once

while True:
    # Take inputs
    loan_amount = Decimal(input("Enter loan amount: "))
    annual_rate = Decimal(input("Enter annual interest rate (%): "))
    months = int(input("Enter loan duration (in months): "))

    # Convert annual rate to monthly rate
    monthly_rate = annual_rate / Decimal("12") / Decimal("100")

    # Calculate EMI
    if monthly_rate == 0:
        emi = loan_amount / months
    else:
        one_plus_r = (Decimal("1") + monthly_rate) ** months
        emi = (loan_amount * monthly_rate * one_plus_r) / (one_plus_r - Decimal("1"))

    # Round EMI to 2 decimal places
    emi = emi.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # Display result
    print("Monthly EMI:", emi)

    # Ask user to continue
    choice = input("Do you want to calculate again? (yes/no): ").lower()

    if choice == "no":
        print("Exiting calculator. Goodbye!")
        break