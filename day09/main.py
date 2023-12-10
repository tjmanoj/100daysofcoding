from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidding_dictionary = {}

choice = True 
while choice:
  name = input("What is your name?:")
  bid = int(input("What's your bid?: $"))
  user_choice = input("Are there any other bidders? Type 'yes' or 'no'.")
  bidding_dictionary[name] = bid
  if user_choice == "no":
    clear()
    choice = False 
    winner_name = ""
    final_bid = 0
    for bidder in bidding_dictionary:
      if bidding_dictionary[bidder] > final_bid:
        winner_name = bidder 
        final_bid = bidding_dictionary[bidder]
    print(f"The winner is {winner_name} with a bid of ${final_bid}")
  else:
    clear()
  