
seconds = int(input("Введіть кількість секунд (0 ≤ n < 8640000): "))

days, rem = divmod(seconds, 24 * 60 * 60)
hours, rem = divmod(rem, 60 * 60)
minutes, seconds = divmod(rem, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in (2, 3, 4) and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {hours:02d}:{minutes:02d}:{seconds:02d}")
