from art import logo
from art import vs
from replit import clear
from game_data import data 
import random
score = 0

print(logo)

a = random.choice(data)
b = random.choice(data)
def compare(a, b):
  print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
  print(vs)
  print(f"Against B: {b['name']}, {b['description']}, {b['country']}")

  answer = "A" if a['follower_count'] > b['follower_count'] else "B"
  choice = input("Who has more followers? Type 'A' or 'B':")
  
  if choice == answer:
    global score
    score += 1
    clear()
    print(logo)
    print(f"You're right! Current score: {score}")
    compare(b, random.choice(data))
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

compare(a,b)