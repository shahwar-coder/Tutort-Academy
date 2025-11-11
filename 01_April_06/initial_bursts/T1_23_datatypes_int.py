'''
- Python’s `int` is an immutable, arbitrary-precision integer type: it grows as large as memory allows, with no fixed bit-width limit.
- Small integers (typically from –5 to 256) are cached and reused for performance, so identity (`is`) may hold for them.
- `bool` is a subclass of `int` (`True == 1`, `False == 0`), which means booleans can be used in arithmetic contexts.
- Supports all usual arithmetic operators: `+`, `-`, `*`, `//`, `%`, `**`, and bitwise operators: `&`, `|`, `^`, `~`, `<<`, `>>`.
- Offers built-in methods for introspection and conversion:
  - `.bit_length()` returns the number of bits necessary to represent the number in binary (excluding sign bit).
  - `.bit_count()` returns the number of set bits (1s) in the binary representation.
  - `.to_bytes(length, byteorder, *, signed=False)` and `int.from_bytes(bytes, byteorder, *, signed=False)` for byte conversions.
  - `.as_integer_ratio()` returns `(numerator, denominator)` such that the ratio equals the integer.
  - `.conjugate()` returns itself (for compatibility with complex numbers).
- Common formatting functions (though not methods): `bin()`, `hex()`, `oct()` convert to respective string representations with prefixes.
- Creating an `int` from a `float` truncates toward zero; from strings, you can specify any base (2–36) as `int(s, base)`.
- Division with `/` yields a `float`; use `//` for integer (floor) division. Beware negative-floor behavior.
- Hash of an `int` is itself, making it ideal as dictionary keys or set elements.
- Internally, Python uses a variable‐length array of “digits” in base 2³⁰ (or 2¹⁵ on some builds) and a sign flag.
- Performance: arithmetic on very large ints is slower (O(n × log n) for multiplication via Karatsuba beyond a threshold).
- Use `isinstance(x, numbers.Integral)` to test generic integer-ness across Python’s numeric tower.
'''


'''
🔢 Question: Binary Bit Length Counter

Write a function `count_bits(n)` that:

- Accepts an integer `n` as input
- Returns the number of bits needed to represent it in **binary**, excluding the sign bit

📌 You should use the built-in `.bit_length()` method.

Then test your function with the following inputs:

print(count_bits(0))        # → 0
print(count_bits(5))        # → 3     (binary: 101)
print(count_bits(1023))     # → 10    (binary: 1111111111)
print(count_bits(-7))       # → 3     (binary of abs(-7): 111)

Hint: Negative integers should be treated based on their magnitude (absolute value).
'''

def count_bits(n: int)->int:
    "Count bits"
    return abs(n).bit_length()

print(count_bits(0))        # → 0
print(count_bits(5))        # → 3     (binary: 101)
print(count_bits(1023))     # → 10    (binary: 1111111111)
print(count_bits(-7))       # → 3     (binary of abs(-7): 111)
