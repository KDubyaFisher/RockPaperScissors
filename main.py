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

#Write your code below this line 👇
# load game pics into list for accessing later
game_pics = [rock, paper, scissors]

# Get and display user choice
user_input = int(input("What do you choose? 0 for rock, 1 for paper, or 2 for scissors.\n"))
print(game_pics[user_input])


# Get and display computer's choice
computer_choice = random.randint(0,2)
print("Computer chose: ")
print(game_pics[computer_choice])

# Check user input for validity and win conditions
if user_input >= 3 or user_input < 0:
  print("You typed an invalid number, you lose!")
elif user_input == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_input == 2:
  print("You lose")
elif computer_choice > user_input:
  print("You lose")
elif user_input > computer_choice:
  print("You win!")
elif computer_choice == user_input:
  print("It's a draw")