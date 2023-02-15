from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")
bids_dictionary={}
#HINT: You can call clear() to clear the output in the console.
end_auction=False
def winer_bid(biders):
  highest_bid=0
  name_winner=""
  for key in biders:
    bid_value = biders[key]
    if bid_value>highest_bid:
      highest_bid=bid_value
      name_winner=key

  print(f"The winner is {name_winner} with a bid of ${highest_bid}.")

while not end_auction:
  name = input("What is your name?: ")
  bid= int(input("What's is your bid($)?: "))
  bids_dictionary[name]=bid
  new_biders=input("Are there any other biders? Type 'yes' or 'no'.\n")
  if new_biders=="yes":
    clear()
  else:
    winer_bid(biders=bids_dictionary)
    end_auction=True
  