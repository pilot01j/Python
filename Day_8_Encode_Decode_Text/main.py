from lowercase_alphabet import alphabet
from art import logo

print(logo)

# caesar - primeste 3 argumente ,textul, shift_amount- codul de criptare/decrimptare si cipher_rirection-secectam ce dorim sa facem cu textul sa-l crimptam sau sa-l decrimptam
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""#cream un nou String care sa salveze textul criptat/decriptat
  if cipher_direction == "decode":#decriptarea reprezinta opusul la criptare de aceea shift_amount*-1
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)#stabilim pozitia char din alphabet care este == cu char din text
      new_position = position + shift_amount#setam noua pozitie conform shift_amount stabilit
      end_text += alphabet[new_position]
    else:#daca alphabet nu se gaseste caracterul din textul introdus atunci el automat se adauga la end_text, aceasta este facut p,u ca simbolurile si spatiile libere sa ramina la fel .
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#totul punem intr-un while ca sa putem noi sa setam cind dorim sa oprim programul
should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # operatiune de mai jos exclude eroarea cind introducem un shift_amount mai mare deict litere in alphabet
  shift = shift % 26
  #chemam functia deja definita caesar
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  #selectam daca dorim sa oprim sau nu progeamul
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")