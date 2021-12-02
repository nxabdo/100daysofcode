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
gameImages = [rock, paper, scissors]
#Store user input
userInput= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

#Computer random selection
computerSelection = random.randint(0,2)
computerMotion=''
usermotion =''


if (userInput == computerSelection):
    print("It is a draw!")

elif (userInput == 0 and computerSelection == 1):
    usermotion = gameImages[0]
    computerMotion = gameImages[1]
    print(f"User chose: {usermotion}")
    print(f"Computer chose: {computerMotion}")
    print("Computer wins! Paper defeats rock.")

elif (userInput == 1 and computerSelection == 0):
    usermotion = gameImages[1]
    computerMotion = gameImages[0]
    print(f"User chose: {usermotion}")
    print(f"Computer chose: {computerMotion}")
    print("You win! Paper defeats rock.")

elif (userInput == 1 and computerSelection == 2):
    usermotion = gameImages[1]
    computerMotion = gameImages[2]
    print(f"User chose: {usermotion}")
    print(f"Computer chose: {computerMotion}")
    print("Computer wins! Scissor defeats paper.")

elif (userInput == 2 and computerSelection == 1):
    usermotion = gameImages[2]
    computerMotion = gameImages[1]
    print(f"User chose: {usermotion}")
    print(f"Computer chose: {computerMotion}")
    print("You win! Scissor defeats paper.")

elif (userInput == 2 and computerSelection == 0):
    usermotion = gameImages[2]
    computerMotion = gameImages[0]
    print(f"User chose: {usermotion}")
    print(f"Computer chose: {computerMotion}")
    print("Computer wins! Rock defeats scissors.")

elif (userInput == 0 and computerSelection == 2):
    usermotion = gameImages[0]
    computerMotion = gameImages[2]
    print(f"User chose: {usermotion}")
    print(f"Computer chose: {computerMotion}")
    print("You win! Rock defeats scissors.")

else:
    print("Invalid input.")