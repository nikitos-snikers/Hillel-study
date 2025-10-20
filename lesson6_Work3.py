
n = int(input("Введіть число: "))


while n > 9:
    dob = 1
    for digit in str(n):
        dob *= int(digit)
    n = dob

print("Результат:", n)
