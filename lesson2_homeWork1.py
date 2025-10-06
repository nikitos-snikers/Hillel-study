number = int(input("Введите четырехзначное число: "))

number1 = number // 1000
number2 = (number // 100) % 10
number3 = (number // 10) % 10
number4 = number % 10

print(number1)
print(number2)
print(number3)
print(number4)