import os
#HINT: You can call "os.system("cls")" to clear the output in the console.
import art

print(art.logo)

bids = {}
bidding_finished = False

def find_a_highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a BID {highest_bid}")

while not bidding_finished:
  name = input("What is your name : ")
  price = int(input("What is the bid price : "))
  bids[name] = price
  other_bider = input("if anyone want's to bid type 'yes' or 'no' : ").lower()
  if other_bider == "no":
    bidding_finished = True
    find_a_highest_bidder(bids)
  elif other_bider == "yes":
    os.system("cls")

print("\n")
print("All Bidder's")
print(bids)