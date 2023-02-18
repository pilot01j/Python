# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


#w - delet all and writw a new text
#a - append a new text
#r - read text from a file
# with open("my_file.txt", mode="a") as file:
#     file.write("New texggggt.")


PLACEHOLDER = "[name]"
with open("./venv/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./venv/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./venv/Input/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

