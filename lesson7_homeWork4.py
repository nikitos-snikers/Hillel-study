def common_elements():
    list1 = [x for x in range(100) if x % 3 == 0]
    list2 = [x for x in range(100) if x % 5 == 0]
    return set(list1) & set(list2)

print(common_elements())

