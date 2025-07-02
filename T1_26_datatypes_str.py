# 🔹 Python `str` (string) Type

# - `str` is an immutable sequence of Unicode characters in Python.
# - Used to store text data like names, sentences, paragraphs, etc.
# - Defined using single ('...'), double ("..."), or triple quotes ('''...''' or """...""").

# 🔸 Key Properties:
# - **Immutable**: Once created, strings cannot be changed in place.
# - **Indexable**: Supports indexing and slicing (0-based).
# - **Iterable**: Can be used in loops (for char in string).
# - **Supports concatenation**: Using `+` and `*` for repetition.

# 🔸 String Creation:
#     s1 = 'hello'
#     s2 = "world"
#     s3 = '''multi-line'''
#     s4 = str(123)  # converts number to string

# 🔸 String Methods (commonly used):
# - .upper(), .lower(), .capitalize(), .title()
# - .find(), .index(), .count(), .replace()
# - .strip(), .rstrip(), .lstrip()
# - .split(), .join()
# - .startswith(), .endswith()
# - .isalpha(), .isdigit(), .isalnum(), .isspace()

# 🔸 String Formatting:
# - f-strings: f"Hello {name}"
# - .format(): "Hello {}".format(name)
# - % operator: "Hello %s" % name

# 🔸 Escape Sequences:
# - \n (newline), \t (tab), \\ (backslash), \', \"

# 🔸 Raw Strings:
# - Prefix with r to ignore escape sequences → r"C:\new\text"

# 🔸 Membership:
# - 'a' in 'apple' → True
# - 'z' not in 'banana' → True

# 🔸 Comparison:
# - Lexicographical comparison using <, ==, etc.

# 🔸 String Encoding:
# - encode() and decode() used to handle byte conversions.

# 🔸 Memory Efficiency:
# - Python optimizes memory by interning small strings (e.g., 'hello' is 'hello' is True).


# Examples:

name = "Alice"
print(name.upper())        # 'ALICE'
print(name[0])             # 'A'
print("ice" in name)       # True
print(name.replace("A", "M"))  # 'Mlice'
print(f"Hello, {name}!")   # 'Hello, Alice!'
