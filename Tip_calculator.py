print("Welcome to the tip calculator!")
try:
    # Get the total bill amount
    bill = float(input("What was the total bill? Rupees "))

    # Get the tip percentage
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

    # Get the number of people to split the bill
    people = int(input("What is the number of people to split the bill? "))

    # Calculate the tip as a percentage
    tip_as_percent = tip / 100

    # Calculate the total tip amount
    total_tip_amount = bill * tip_as_percent

    # Calculate the total bill
    total_bill = bill + total_tip_amount

    # Calculate the amount each person should pay
    bill_per_person = total_bill / people

    # Round the result to two decimal places
    final_amount = round(bill_per_person, 2)

    print(f"Each person should pay: Rupees {final_amount}")

except Exception as e:
    print(f"Exception occured: {e}")
