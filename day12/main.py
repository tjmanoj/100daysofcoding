from art import logo 
import random

answer = random.randint(1,100)

def game(chance):
  chances = chance
  while chances != 0:
    print(f"You have {chances} attempts to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
      print(f"You got it. The answer was {answer}")
      chances = 0
    elif guess > answer:
      print("Too high.")
      if chances != 1:
        print("Guess again.")
      chances -= 1
    else:
      print("Too low.")
      if chances != 1:
        print("Guess again.")
      chances -= 1
  
  if chances == 0:
    print("You've run out of guesses, you lose🥺")

print(logo)
print("Welcome to guessing game!!")
print("Guess a number between 1 and 100.")
level = input("Choose hard or easy level?: ")

if level == "easy":
  game(5)
else:
  game(10)
