rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
list1 = ['Rock','Paper','Scissors']
list2 = [rock,paper,scissors]
user_choice = int(input())
computer_choice = random.randint(0,2)
print(f"Your choice: {list1[user_choice]}")
print(list2[user_choice])
print(f"Computer choice: {list1[computer_choice]}")
print(list2[computer_choice])

if user_choice == computer_choice:
    print("It\'s a draw!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("invalid choice")
    
