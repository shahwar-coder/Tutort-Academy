'''
🔹 Python `list` Type

- A `list` in Python is an **ordered**, **mutable** collection of elements.
- Lists can hold items of **any data type**, and even a mix of types.
- Lists are **indexed (0-based)**, **iterable**, and **dynamic** (size can change).

🔸 Creation:
    my_list = [1, 2, 3]
    mixed = [1, "hello", 3.14, True]
    nested = [[1, 2], [3, 4]]
    empty = []

🔸 Accessing Elements:
    my_list[0]       → First element
    my_list[-1]      → Last element
    my_list[1:3]     → Slicing (elements at index 1 and 2)

🔸 Mutability:
    my_list[1] = 10  → Lists are mutable; elements can be changed

🔸 Common Methods:
- `.append(x)`          → Add item at end
- `.extend([a, b])`     → Add multiple items
- `.insert(i, x)`       → Insert at position `i`
- `.remove(x)`          → Remove first occurrence of `x`
- `.pop([i])`           → Remove & return item at `i` (default: last)
- `.clear()`            → Remove all items
- `.index(x)`           → First index of `x`
- `.count(x)`           → Count occurrences of `x`
- `.sort()`             → In-place ascending sort
- `.reverse()`          → Reverse list in-place
- `sorted(list)`        → Returns sorted copy
- `len(list)`           → Number of items

🔸 Iteration:
    for item in my_list:
        print(item)

🔸 List Comprehension:
    squares = [x**2 for x in range(5)]
    evens = [x for x in range(10) if x % 2 == 0]

🔸 Nesting:
    matrix = [[1,2,3],[4,5,6]]
    matrix[1][2] → 6

🔸 Memory & Identity:
- Lists are **mutable**, so assignment copies the reference:
    a = [1, 2]
    b = a
    b[0] = 99  → Now `a[0]` is also 99

- Use `copy()` or `list()` for a shallow copy:
    b = a.copy() or b = list(a)

🔸 Checking Membership:
    x in my_list       → True if `x` exists in list

🔸 Heterogeneous:
    A list can store elements of different types:
    [1, "hi", None, [3, 4]]

🔸 Dynamic Sizing:
    List size can grow or shrink with `append`, `pop`, etc.

🔸 Caution:
- Avoid modifying a list while iterating over it (use `.copy()` if needed)
'''

