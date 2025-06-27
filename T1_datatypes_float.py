'''
- Python's `float` implements IEEE 754 double-precision (64-bit) floating-point numbers.
- It provides approximately 15–17 significant decimal digits of precision.
- Internally stored as 1 sign bit, 11 exponent bits, and 52 fraction (mantissa) bits.
- Common operations supported: `+`, `-`, `*`, `/`, `//` (floor division returns `float`), `%`, `**` (exponentiation), and comparisons.
- Special values:
  - `inf` and `-inf` represent positive and negative infinity (e.g., `1.0/0.0`).
  - `nan` (not-a-number) indicates undefined or unrepresentable results (e.g., `0.0/0.0`).
- Methods and functions for conversion and inspection:
  - `float.as_integer_ratio()` returns `(numerator, denominator)` exactly representing the float.
  - `float.hex()` returns a hexadecimal string representation; `float.fromhex()` parses it back.
  - `math.isnan(x)` and `math.isinf(x)` to test for `nan` or infinite values; `math.isfinite(x)` checks for neither.
- Formatting floats:
  - `format(x, '.2f')`, `f"{x:.2f}"`, or `round(x, 2)` for controlling decimal places.
- Caveats:
  - Floating-point arithmetic can introduce rounding errors; use `decimal.Decimal` for exact decimal arithmetic.
  - Comparisons should allow a tolerance: `abs(a - b) < epsilon` rather than `a == b`.
- `float` inherits from `numbers.Real`; `isinstance(x, numbers.Real)` checks for real numbers.
'''

'''
🌊 Question: Floating Point Formatter

Write a function `format_float(x)` that:

- Takes a float `x` as input
- Returns a string with the value formatted to exactly **2 decimal places**

Use string formatting to achieve this.

🔹 Example Calls:
print(format_float(3.14159))     # → '3.14'
print(format_float(2.0))         # → '2.00'
print(format_float(9.876543))    # → '9.88'
'''

def format_float(x: float)->str:
    "Format float and return the string"
    formatted_x = format(x, '.2f')
    return formatted_x
    # return str(formatted_x) # converting to str is not required a s format() itslef gives string.
    
print(format_float(x=9.885678))
