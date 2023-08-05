""" Tip Calculator """

print("Welcome to the Tip calculator.")
bill = float(input("Enter the total bill of the food: "))
persons = int(input("How many persons want to split the bill: "))
tip_percentage = float(input("How much percentage of tip do you want to give? (10%, 12%, 15%): "))

tip = (tip_percentage / 100) * bill
total_bill = bill + tip
amount_per_person = total_bill / persons
final_amount = round(amount_per_person)

print(f"Each person should pay: {final_amount}")
