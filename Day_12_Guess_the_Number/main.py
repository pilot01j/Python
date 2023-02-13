#Number Guessing Game
import random
from art import logo

def dificulty ():
  choose_dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ")
  if choose_dificulty == "easy":
    return 10
  else:
    return 5 
 
def guess_number(attempts,random_number):
    while attempts !=0:
      print(f"You have {attempts} attempts to guess the number .")
      attempts-=1
      guess = int(input("Make a guess: "))
      if guess == random_number :
        print (f"You guess! The number was {random_number}.")
        attempts = 0
      elif attempts == 0:
        print(f"You lose. The number was {random_number}.")
      elif guess > random_number:
        print("Too high.")
      else:
        print("Too low.")    
def game ():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  random_number = random.randint(0,100)
  print(random_number)
  attempts = dificulty()
  guess_number(attempts,random_number)
  
game()