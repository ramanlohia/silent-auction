from replit import clear

bids={}
bid_over = True

import art
print(art.logo)

def highest_bidder():
  clear()
  highest_bid = 0
  winner = ""
  for bidder in bids:
    if highest_bid < bids[bidder]:
      highest_bid = bids[bidder]
      winner = bidder
  print(f"Winner is {winner} with the highest bid of Rs.{highest_bid}")

while bid_over == True:
  name = input("Enter your name:\n")
  bid = int(input("Enter your bid amount: \n"))
  bids[name] = bid
  another_bidder = input("If there is any other bidder type 'yes' else 'no' ")
  if another_bidder == 'yes':
    clear()
  else:
    bid_over = False
    highest_bidder()

print("GoodBye")