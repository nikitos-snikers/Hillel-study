def popular_words(text, words):
    text = text.lower().split()

    result = {word: text.count(word) for word in words}

    return result


text = '''When I was One
 I had just begun
 When I was Two
 I was nearly new'''

print(popular_words(text, ['i', 'was', 'three', 'near']))
