number1=float(input("введите первое число:"))

act=input("Введите символ действия(+,-,*,/):")

number2=float(input("введите второе число:"))

print('Ваш результат:')

if act=="+":
    print(number1+number2)
elif act=="-":
    print(number1-number2)
elif act=="*":
    print(number1*number2)
elif act=="/":
    if number2==0:
        print("На 0 делить нельзя!!!")
        exit()
    else:
        print(number1/number2)
else:
    print("введите корректный символ")
    exit()
print('Хорошего времени суток!!!')


