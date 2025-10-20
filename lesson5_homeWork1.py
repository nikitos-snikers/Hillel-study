import keyword
import string
name = input("введите строку: ")
if name in keyword.kwlist:
    print(False)
    exit()
if name[0].isdigit():
    print(False)
    exit()
if any(ch.isupper() for ch in name):
    print(False)
    exit()
for ch in name:
    if ch in string.punctuation.replace("_", "") or ch == " ":
        print(False)
        exit()
print(True)








