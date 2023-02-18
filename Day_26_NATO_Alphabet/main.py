import pandas

# Create a list of phonetic words
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# print(phonetic_dict)

# create a list of phonetic code rows from a word that the user inputs.

def generate_phonetic():
    word = input("Enter the word: ").upper()
    try:
        letter_list = [letter for letter in word]
        phonetic_list = [phonetic_dict[letter] for letter in word]

        word_speling = {"Letter": letter_list, "": "as", "Phonetic": phonetic_list}
        print(word_speling)
        word_data_frame = pandas.DataFrame(word_speling)
    except KeyError:  # cath such type of error
        print("Sorry, only letters from alphabet is accepted.")
        generate_phonetic()
    else:
        print(word_data_frame)


generate_phonetic()
