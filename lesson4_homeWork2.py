lst = [2, 3, 4, 5, 6, 7]
if len(lst) == 0:
    result = 0
else:
    double_sum = sum(lst[::2])
    result = double_sum * lst[-1]

print(result)
