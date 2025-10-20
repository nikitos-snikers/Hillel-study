import string

letters = string.ascii_letters
start, end = input("Введіть дві літери через дефіс: ").split('-')

print(letters[letters.index(start): letters.index(end) + 1])
