def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:] if text else ""
    if not text.endswith('.'):
        text += '.'
    return text
print(correct_sentence("привіт"))
print(correct_sentence("Привіт"))
print(correct_sentence("Привіт."))
print(correct_sentence("як справи"))

