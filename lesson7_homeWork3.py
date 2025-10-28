def second_index(text: str, symbol: str) -> int | None:
    first = text.find(symbol)
    if first == -1:
        return None
    second = text.find(symbol, first + 1)
    return second if second != -1 else None
print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", "h"))
print(second_index("Hello hello", "lo"))
