import string
beg=str("Введите слово для преобразования в хештег:")
print(beg)

user_input = input("")

hashtag = "#" + "".join(word.capitalize() for word in user_input.translate(str.maketrans('', '', string.punctuation)).split())[:140]

print(hashtag)
exit()
