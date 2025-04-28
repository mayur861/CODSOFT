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
game_images = [rock , paper, scissors]

user_choose = int(input("what do you choose? Type 0 for Rock , 1 for Paper, 2 for Scissor."))

if user_choose >= 0 and user_choose <=2:
 print(game_images[user_choose])

computer_choose = random.randint(0,2)
print(f"computer choose:")

print(game_images[computer_choose])


if user_choose == 0 and computer_choose== 2:
    print("You Win!")

elif computer_choose > user_choose:
    print("You loose")

elif user_choose == computer_choose:
    print("Its a draw!")

elif user_choose ==2 and computer_choose == 1:
    print("You win!")

elif user_choose ==2 and computer_choose == 0:
    print("You Loose")

elif user_choose == 1 and computer_choose== 0:
    print("You Win!")


else:
    print("You print a invalid number")


