print("Welcome to the Tip Calculator!!")
currency = "$"
bill = float(input(f"What was the total bill?{currency}"))
tip_percentage = int(input("how much % of tip would you like to give? 10, 15 OR 20 "))
people = int(input("how many person to split the bill?"))

tip = bill * (tip_percentage / 100)
bill_with_tip = bill + tip
# OR simply we can write
# total_bill = bill + (bill * (per_person_bill / 100))

per_person_bill = round(bill_with_tip / people, 2)
print(f"Each person should pay {currency}{per_person_bill}")
