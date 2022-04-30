from art import logo

print(logo)

bid_dict = {}
more_bidders = True

def add_bid(bid_name, bid_value):
  bid_dict[bid_name] = bid_value

def max_bid():
  max_value = max(bid_dict.values())
  max_bidder = max(bid_dict, key = bid_dict.get)
  print(f"The winner of the auction is {max_bidder} with a bid of ${max_value}.")

while more_bidders:
  name = input("What is your name?\n")
  bid_price = int(input('What is your bid price?\n$'))
  
  add_bid(bid_name = name, bid_value = bid_price)

  bidder_check = input("Are there any more bidders? Yes or No.\n").lower()

  if bidder_check == "no":
    more_bidders = False
    max_bid()


