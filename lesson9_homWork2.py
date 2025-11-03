def difference(*args):
    if not args:
        return 0
    return round(max(args) - min(args), 2)

print(difference(1, 2, 3))
print(difference(5.5, 1.1, 10.2))
print(difference())
print(difference(2.333, 2.339))
