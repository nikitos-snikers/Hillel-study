import keyword
import string

name = input("введите строку: ")
if name == "_":
    print(True)
    exit()
if "__" in name:
    print(False)
    exit()
if name in keyword.kwlist:
    print(False)
    exit()
if name[0].isdigit():
    print(False)
    exit()
if any(ch in string.punctuation.replace("_", "") or ch == " " for ch in name):
    print(False)
    exit()
if any(ch.isupper() for ch in name):
    print(False)
    exit()
print(True)









