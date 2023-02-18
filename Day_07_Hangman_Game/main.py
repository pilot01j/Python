import random
import hangman_logo
import hangman_words
import replit

display=[]
lives=6
end_of_game = False
stages=hangman_logo.stages
word_list=hangman_words.word_list
chosen_word=random.choice(word_list)

print(hangman_logo.logo)
print(chosen_word)
for x in range (len(chosen_word)):
  display.append('_')
print(display)
while not end_of_game:
  guess=input("Gues a letter: ").lower()
  replit.clear()
  if guess in display:
    print(f"You've already guessed {guess}")
  for x in range (len(chosen_word)-1):
    if chosen_word[x] == guess:
      display[x]=guess
  print(display)
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")
  if "_" not in display:
    end_of_game = True
    print("You win")
    
  print(stages[lives])
