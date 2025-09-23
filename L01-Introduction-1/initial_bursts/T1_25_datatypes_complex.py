'''
- `complex` is a built-in Python data type used to represent **complex numbers**, which have:
  - A real part
  - An imaginary part (multiplied by `j`, not `i` as in mathematics)

- Syntax:
    complex_number = real + imaginary * j

- You can define complex numbers in two ways:
    1. Using literals → `z = 2 + 3j`
    2. Using `complex()` constructor → `z = complex(2, 3)`

- Access parts:
    - `z.real` → gives the real part (float)
    - `z.imag` → gives the imaginary part (float)

- Python supports arithmetic operations on complex numbers:
    - Addition: `(2 + 3j) + (1 + 4j)` → `(3 + 7j)`
    - Subtraction: `(5 + 2j) - (1 + 1j)` → `(4 + 1j)`
    - Multiplication, division, power, etc.

- Built-in functions for complex:
    - `abs(z)` → magnitude (modulus) → √(real² + imag²)
    - `z.conjugate()` → returns the complex conjugate (real - imag*j)

- Cannot be ordered: `>` or `<` will raise `TypeError`
- Useful in scientific, engineering, signal processing, and electrical circuit applications

- Complex numbers are immutable.
'''

# Example

z1 = 2 + 3j
z2 = complex(4, -2)

print(z1 + z2)            # (6+1j)
print(z1 * z2)            # (14+8j)
print(z1.real)            # 2.0
print(z1.imag)            # 3.0
print(z1.conjugate())     # (2-3j)
print(abs(z1))            # 3.605551275463989 (√(2² + 3²))
