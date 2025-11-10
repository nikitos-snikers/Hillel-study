def generate_cube_numbers(limit):
    n = 2
    while True:
        cube = n ** 3
        if cube >= limit:
            return
        yield cube
        n += 1

print(list(generate_cube_numbers(30)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(8)))
