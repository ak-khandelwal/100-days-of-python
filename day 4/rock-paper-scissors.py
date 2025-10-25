import sys

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

import random
options = [rock,paper,scissors]
userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computerInput = random.randint(0,2)
print('user has selected: ')
if userInput==0:
    print('rock')
elif userInput==1:
    print("paper")
elif userInput==2:
    print('scissors')
else:
    print('wrong input')
    sys.exit(1)
print(options[userInput])
print("CPU has selected: ")
if computerInput==0:
    print('rock')
elif computerInput==1:
    print("paper")
elif computerInput==2:
    print('scissors')
print(options[computerInput])

if userInput==computerInput:
    print("tie!!!")
elif userInput==2 and computerInput==0:
    print('cpu win!')
elif userInput==0 and computerInput==2:
    print("you win!")
elif userInput>computerInput:
    print("you win!")
elif userInput<computerInput:
    print('cpu win!!')
