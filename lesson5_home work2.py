while True:
    number1 = float(input("Введите первое число: "))
    act = input("Введите символ действия (+, -, *, /): ")
    number2 = float(input("Введите второе число: "))

    print("Ваш результат:")

    if act == "+":
        print(number1 + number2)
    elif act == "-":
        print(number1 - number2)
    elif act == "*":
        print(number1 * number2)
    elif act == "/":
        if number2 == 0:
            print("На 0 делить нельзя!!!")
        else:
            print(number1 / number2)
    else:
        print("Введите корректный символ")


    con = input("Хотите сделать ещё одно вычисление? (y/yes для продолжения): ").lower()
    if con not in ("y", "yes"):
        print("Работа калькулятора завершена.")
        break
