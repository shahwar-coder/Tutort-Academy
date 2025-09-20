'''
Q1. What is a programming language?
Ans:
- It’s a formal system to express instructions so a computer can execute them.
- Think of it as a “bridge” between human ideas and machine operations.

Example:
'''
Human idea → “Add two numbers and show result.”
Python code → print(2 + 3)
# Step-by-step:
# 1. Human expresses idea in Python syntax.
# 2. Python interpreter converts it into CPU operations.
# 3. Computer shows output → 5



'''
Q2. What’s the difference between low-level and high-level languages?
Ans:
- Low-level → closer to machine, harder for humans (e.g., Assembly, C).
- High-level → closer to human logic, hides hardware details (e.g., Python, Java).

Example:
'''
# Assembly (low-level):
MOV AX, 2
ADD AX, 3
PRINT AX

# Python (high-level):
print(2 + 3)

# Step-by-step:
# Both do the same task → add 2 + 3.
# Assembly is verbose and hardware-oriented.
# Python is shorter, human-readable.



'''
Q3. What are syntax and semantics?
Ans:
- Syntax = the structure/rules of writing code.
- Semantics = the meaning of that code.

Example:
'''
# Syntax error:
print("Hello"   # ❌ missing parenthesis

# Semantic error:
print(2 / 0)    # Syntax is fine, but meaning invalid (ZeroDivisionError).

# Step-by-step:
# Syntax → “is this written correctly?”
# Semantics → “does this make sense when executed?”



'''
Q4. Why do we need compilers or interpreters?
Ans:
- Computers understand only machine code (binary).
- A compiler/interpreter translates human-readable code into machine code.

Example:
'''
# Python (interpreted):
print("Hi")

# Step-by-step:
# 1. Python interpreter parses code.
# 2. Translates to bytecode/machine code.
# 3. CPU executes → prints "Hi".



'''
Q5. Why do we need different programming languages?
Ans:
- Different tradeoffs:
   - C → speed, control.
   - Python → readability, rapid development.
   - JavaScript → web development.
- No single “best” language — choice depends on use-case.
'''



'''
Q6. Quick shorthand
- Language = bridge (human ↔ machine).
- Syntax = form. Semantics = meaning.
- Compiler/Interpreter = translator.
- Low-level = detailed, harder. High-level = abstracted, easier.
'''
