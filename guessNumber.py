import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

GuessNumber = random.randint(1,100)
tries=0
clear()
print ("\n🎲 Welcome to the Number Guessing Game!\n")
while (True):
    your_number = int(input("Guess a number between 1 and 100 : "))
    tries +=1
    if (GuessNumber > your_number):
        print(" Too low! Try again.")
    elif(GuessNumber < your_number):
        print(" Too hight ! Try again.")
    else:
        print(f"\n🎉🎉🎉 Correct! You guessed the number in {tries} tries.")
        break

