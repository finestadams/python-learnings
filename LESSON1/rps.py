import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3



print("")
playerChoice = input('Enter... \n1 for Rock \n2 for Paper, or\n3 for Scissors: \n')

player = int(playerChoice)


if player < 1 | player > 3:
    sys.exit('You must enter 1, 2 or 3')

comoputerChoice = random.choice('123')

computer = int(comoputerChoice)

print("")

print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Computer chose " + str(RPS(computer)).replace('RPS.', '') + ".")

print("")

if player == 1 and computer == 3:
    print("😊 You win!")
elif player == 2 and computer == 1:
    print("😊 You win!")
elif player == 3 and computer == 2:
    print("😊 You win!")
elif player == computer: 
    print("😳 Tie game")
else:
    print("🐍 Python win!")