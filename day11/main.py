from art import logo 
from replit import clear
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(l):
  if len(l) == 2 and sum(l) == 21:
    return 0
  elif 11 in l and sum(l) > 21:
    l.remove(11)
    l.append(1)
  return sum(l)

def result(user, computer):
  if user > 21 and computer > 21:
    return "You lose"
  elif user == computer:
    return "Draw"
  elif user == 0 :
    return "Win with blackjack"
  elif computer == 0:
    return "Lose they got blackjack"
  elif user > 21:
    return "You Lose"
  elif computer > 21:
    return "You win"
  elif user > computer:
    return "You win"
  else:
    return "You lose"
  

    
def game():
  print(logo)
  user_cards = []
  computer_cards = []
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  game_end = False 
  while not game_end:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
  
    print(f"Your cards:{user_cards}, current_score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
  
    if user_score == 0 or computer_score == 0 or sum(user_cards) > 21:
      game_end = True
    else:
      ch = input("Type 'y' to get another card, type 'n' to pass:")
      if ch == "y":
        user_cards.append(deal_card())
      else:
        game_end = True

  while computer_score != 0 and computer_score < 17 :
    computer_score = calculate_score(computer_cards)
    computer_cards.append(deal_card())
  print(f"Your final hand:{user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

  print(result(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
  clear()
  game()