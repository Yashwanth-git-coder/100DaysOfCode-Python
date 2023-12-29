import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonectic_data = {row.letter : row.code for (index, row) in data.iterrows()}

word = input("Enter the Letter : ").upper()
output = [phonectic_data[letter] for letter in word]
print(output)