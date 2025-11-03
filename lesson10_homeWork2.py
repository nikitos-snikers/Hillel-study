def first_word(text):

    for ch in '.,':
        text = text.replace(ch, ' ')

    text = text.strip()

    words = text.split()

    return words[0] if words else ''

print(first_word("Hello world"))
print(first_word("...and so on"))
print(first_word(" , , ,word"))
print(first_word("don't touch it"))
print(first_word("   single"))
print(first_word(""))

