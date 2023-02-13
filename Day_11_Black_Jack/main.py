import random
from art import logo
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Prima metoda dins lista cu carti selecteaza random o carte si returneaza valoarea ei
def deal_card():
  card = random.choice(cards)
  return card

#A doua metoda calculeaza valoare cartilor primite 
def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#A treia metoda compara rez obtinut de jucator si calculator
#atrage atengia la ordinea in care sunt puse if / elif
def compare_score(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
     return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score ==0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game ():
  print(logo)
  user_cards=[]#memoreaza cartile hucatorului
  computer_cards=[]#memoreaza cartile computerului
  end_game=False#p.u opreirea jocului in while

  for _ in range(2):
    #adauga primele 2 carti ale jucatorului si a calculatorului
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not end_game:
    #calculeaza valoarea cartilor ale jucatorului sia calculatorului
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your cards : {user_cards} , your score is {user_score} .")
    print(f"    Computer firs card is {computer_cards[0]}")
    if user_score == 0 or computer_score ==0 or user_score > 21 :
      end_game = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: \n")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        end_game = True
  while computer_score !=0 and computer_score < 17 :
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print("----------------------------------------------------------------------------")
  print(f"    Your final hand: {user_cards}, final  score {user_score}")
  print(f"    Computer's final hand: {computer_cards}, final score {computer_score} ")
  print (compare_score(user_score, computer_score))
  
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': \n") == "y":
  clear()
  play_game()