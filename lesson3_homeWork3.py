lst = [1,2,3,4,5]
print(lst)

n = len(lst)
middle = (n + 1) // 2
first = lst[:middle]
second = lst[middle:]

result = [first, second]

print(result)
