#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
nr= nr_letters+nr_symbols+nr_numbers
for x in range (0,nr_letters):
  password+=letters[random.randint(0,len(letters)-1)]
for x in range (0, nr_symbols):
  password+=symbols[random.randint(0,len(symbols)-1)]
for x in range (0, nr_numbers):
  password+=numbers[random.randint(0,len(numbers)-1)]
print(password)
new_password=""
while len(password)>0:
  nr=random.randint(0,len(password)-1)
  new_password+=password[nr]
  password=password.replace(password[nr],'')
  #print(x_pasword)
print(new_password)
