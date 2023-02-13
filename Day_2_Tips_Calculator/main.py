print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
number_people=int(input("How many people to split the bill? "))
tip_total=total_bill*(tip/100)
final_bill=total_bill+tip_total
per_person=round(final_bill/number_people,2)
print(f"Each person should pay : ${per_person}")