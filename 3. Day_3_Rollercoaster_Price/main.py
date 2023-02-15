print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))
bill=0
if height>=120:
  print("You can ride the rollercoaster!")
  age = int(input("How old are you? "))
  if age<12:
    bill=5
    print("Pay please $5.")
  elif age>=12 and age<18:
    bill=7
    print("Pay please $7.")
  else:
    bill=10
    print("Pay please $10.")
  wants_photo=input("Do you wants a photo (Y/N)?")
  if wants_photo=="Y":
    bill+=3
    print(f"Pay please ${bill}.")
else:
  print("Sorry but you can't ride on the rollercoaster .")