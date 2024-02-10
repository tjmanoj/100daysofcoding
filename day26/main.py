import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = {row.letter: row.code for(index, row) in data.iterrows()}

user_input = input("Enter a word: ")
result = [df[word.upper()] for word in user_input]
print(result)