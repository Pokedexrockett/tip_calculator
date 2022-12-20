print("Welcome to the tip calculator.")
bill = float(input("What is the total bill? $"))
tip = int(input("What percentage would you like to give? 18, 20, or 22?"))
people = int(input("How many peiple to split the bill?"))

bill_with_tip = tip / 100 * bill + bill

bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: $ {final_amount}")