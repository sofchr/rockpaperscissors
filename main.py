import random

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

raw_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

user_choice = int(raw_input)

computer_choice = random.randint(0,2)

print(f"Your choice is {user_choice} and the computer's choice is {computer_choice}")

if user_choice == 0 and computer_choice == 2:
	print("You won!")
elif user_choice == 2 and computer_choice == 1:
	print("You won!")
elif user_choice == 1 and computer_choice == 0:
	print("You won!")
elif user_choice == computer_choice:
	print("You tied!")
else:
	print("You lost!")