def sequence_generator(func, first, n):
    """
    Генератор числової послідовності.
    :param func: функція, яка описує закон послідовності (наприклад, lambda x: x + 2)
    :param first: перший член послідовності
    :param n: кількість членів, які потрібно згенерувати
    """
    value = first
    for _ in range(n):
        yield value
        value = func(value)


gen = sequence_generator(lambda x: x + 3, 2, 5)
print(list(gen))  # [2, 5, 8, 11, 14]


gen = sequence_generator(lambda x: x * 2, 1, 6)
print(list(gen))
