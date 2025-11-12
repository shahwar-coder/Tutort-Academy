'''
📘 Important String Concepts in Python — One Concept per Point

• Strings are sequences of characters enclosed in quotes (' ' or " ").
• Strings are immutable — once created, they cannot be changed.
• You can access characters using indexing (e.g., s[0]).
• Negative indexing starts from the end (e.g., s[-1] → last char).
• Slicing extracts substrings (e.g., s[1:4]).
• Step in slicing skips characters (e.g., s[::2]).
• len(s) gives the number of characters in the string.
• String concatenation uses + operator.
• String repetition uses * operator (e.g., 'a'*3 → 'aaa').
• Strings support membership test with `in` (e.g., 'a' in s).
• Strings can be iterated using for-loops.
• Strings support comparison using ==, <, > (lexicographic order).
• You can convert other types to string using str().
• split() breaks a string into a list by a delimiter.
• join() merges a list of strings into one string.
• strip(), lstrip(), rstrip() remove whitespace.
• lower() and upper() change case.
• capitalize(), title(), swapcase() modify word capitalization.
• find() and index() locate substrings (index() raises error if not found).
• count() counts occurrences of a substring.
• replace(old, new) replaces all occurrences.
• startswith() and endswith() check prefixes/suffixes.
• isalpha(), isdigit(), isalnum(), isspace() check character types.
• format() and f-strings support variable interpolation.
• ord() converts a character to its ASCII/Unicode value.
• chr() converts ASCII/Unicode code back to character.
• Strings are iterable but not mutable (cannot assign s[0] = 'x').
• You can reverse a string with slicing: s[::-1].
• String comparison is case-sensitive by default.
• Triple quotes (''' ''' or """ """) allow multiline strings.
• Raw strings (r"…") ignore escape sequences like \n or \t.
• Escape characters (e.g., \n, \t, \") represent special symbols.
• Strings can be encoded to bytes using encode().
• Bytes can be decoded back to strings using decode().
• format(), f-strings, and % formatting are common for string interpolation.
• String concatenation inside loops is inefficient — use join() instead.
• Strings are stored in Unicode, supporting multiple languages.
'''

