lst = [0,0,0,1,1,1]
print(lst)

non_zero = [i for i in lst if i != 0]
zero = [i for i in lst if i == 0]

lst = non_zero + zero

print(lst)
