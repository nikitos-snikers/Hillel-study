number = int(input("Введи число из 5 цифр: "))

n1 = number // 10000
n2 = (number // 1000) % 10
n3= (number // 100) % 10
n4 = (number // 10) % 10
n5 = number % 10

reverse_number = n5 * 10000 +n4 * 1000 +n3 * 100 + n2* 10 + n1

print(reverse_number)