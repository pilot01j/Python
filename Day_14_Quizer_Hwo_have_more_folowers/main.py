from art import logo, vs
from game_data import data
import random
from replit import clear
import time

account_a = random.choice(data)

def random_b (account_a):
  account_b = random.choice(data)
  if account_b == account_a :
    account_b = random.choice(data)
  return account_b
  
account_b = random_b (account_a) 

def print_account(ac_data):
  name = ac_data['name']
  follower = ac_data['follower_count']
  description =ac_data ['description']
  country = ac_data['country']
  print_ac =(f"{name}, a {description}, from {country}.")
  return print_ac 

def compare (account_a, account_b):
  end_game = False
  score = 0
  while not end_game:
    print(logo)    
    print(f"Curent score is  {score} points.")
    print("A:", print_account(account_a))
    print(vs)
    print("B:", print_account(account_b))
    
    follower_a = account_a['follower_count']
    #print(follower_a)
    
    follower_b = account_b['follower_count']
    #print(follower_b)
    print("----------------------------------------------------")
    user_choose = input("Who has more follower on instagaram? Type 'A' or 'B'.\n").lower()
    if user_choose == 'a' and follower_a > follower_b:
      score+=1
      account_b = random_b (account_a)
      print("You are right!")
      time.sleep(1)
      clear()
    elif user_choose == 'b'and follower_a < follower_b :
      score+=1
      account_a = account_b
      account_b = random_b (account_a)
      print("You are right!")
      time.sleep(1)
      clear()
    else:
      print(f"You Fail!\nA: have : {follower_a} follower.\nB: have : {follower_b} follower.\nYour final score is {score} points.")
      end_game = True

compare (account_a,account_b)