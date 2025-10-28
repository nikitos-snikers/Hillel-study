from collections import Counter
from typing import List, Optional

def find_unique_value(numbers: List[int]) -> Optional[int]:

    if not numbers:
        return None

    counts = Counter(numbers)
    for num in numbers:
        if counts[num] == 1:
            return num
    return None
print(find_unique_value([1, 1, 2, 1, 1]))
print(find_unique_value([4, 5, 4, 4, 4]))
print(find_unique_value([7, 7, 7]))
print(find_unique_value([]))

