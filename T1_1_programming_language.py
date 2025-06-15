'''
1. 💻 What is the primary purpose of a programming language?
A. To draw graphics on a screen
B. To translate human thoughts into music
C. To instruct a computer to perform tasks  ← correct
D. To store large amounts of data

# Note 1: “Programming language” means a formal syntax and semantics for writing instructions.
# Note 2: Only C describes giving instructions; A, B, D are specialized tasks or storage.

2. 🚫 Which of the following is NOT a key feature of a programming language?
A. Syntax
B. Semantics
C. Flavor  ← correct
D. Control Flow

# Note 1: Syntax and semantics define structure and meaning; control flow manages execution paths.
# Note 2: “Flavor” isn’t a technical term; the others are fundamental properties.

3. 🔢 Computers natively understand which form of code?
A. Python
B. Java
C. Binary (0s and 1s)  ← correct
D. HTML

# Note 1: “Binary” refers to machine code bits that the CPU executes directly.
# Note 2: High-level languages (A,B,D) must be translated into binary first.

4. 🎭 In programming, “abstraction” refers to:
A. Obscuring all code details permanently
B. Using simple interfaces to manage complexity  ← correct
C. Turning code into abstract art
D. Writing code in uppercase letters

# Note 1: Abstraction hides complexity behind understandable APIs or data structures.
# Note 2: B captures intent; A, C, D are incorrect or nonsensical.

5. 🗄️ Which of these is a valid “data structure” concept?
A. Typography
B. Arrays  ← correct
C. Syntax
D. Semantics

# Note 1: Arrays are a standard indexed collection; data structures organize data.
# Note 2: Syntax and semantics are language features; typography is unrelated.

6. ⚙️ Which paradigm emphasizes functions without side effects and immutable data?
A. Object‑Oriented Programming
B. Procedural Programming
C. Functional Programming  ← correct
D. Logic Programming

# Note 1: Functional programming avoids mutable state and side effects.
# Note 2: Other paradigms focus on objects, sequences of commands, or logical rules.

7. 🔧 A “compiled” language differs from an “interpreted” one in that:
A. Compiled code runs in a web browser only
B. Interpreted code is pre‑translated to machine code once
C. Compiled code is translated to machine code ahead of execution  ← correct
D. Interpreted languages cannot use variables

# Note 1: Compilers produce machine code before running; interpreters read source on the fly.
# Note 2: C correctly contrasts ahead-of-time vs. run-time translation; A, B, D are false.

8. 📋 In static typing, type checking occurs:
A. At runtime only
B. Before the program runs  ← correct
C. Only when a compiler flag is set
D. When the user types input

# Note 1: Static typing enforces type rules at compile time.
# Note 2: B describes compile-time checking; A is dynamic typing, C/D are incorrect contexts.

9. 🔄 Which of these is an example of a control flow construct?
A. `for` loop  ← correct
B. HTTPS
C. SQL
D. CSS

# Note 1: Control flow constructs (loops, conditionals) dictate execution order.
# Note 2: B–D are protocols or languages, not flow constructs.

10. 🟰 In many languages, the `==` operator checks for:
A. Memory address equality
B. Semantic meaning of words
C. Value equality  ← correct
D. File system permissions

# Note 1: `==` compares values/content, not identity or external permissions.
# Note 2: Only C matches how equality operators work generally.

11. 🔒 Which mechanism allows a function to access variables defined in its outer lexical scope?
A. Polymorphism
B. Encapsulation
C. Closure  ← correct
D. Inheritance

# Note 1: Closures capture surrounding scope so nested functions can use outer variables.
# Note 2: Other terms relate to OOP, not lexical scoping.

```
def outer_function(message):
    def inner_function():
        print("Message is:", message)
    return inner_function

my_func = outer_function("Hello, World!")
my_func()
```
- Even though outer_function is done running, the variable message is still accessible by inner_function because of closure.
- And the message is printed.

12. 🔁 Tail-call optimization primarily benefits which style of programming?
A. Imperative
B. Concurrent
C. Functional  ← correct
D. Object‑Oriented

# Note 1: Tail-call optimization avoids stack growth in recursive, functional code.
# Note 2: It isn’t central to imperative or OO styles.

TAIL - CALL:
```
def tail_example(x):
    return another_function(x)  # ← Tail call

Example:
def tail_factorial(n, acc=1):
    if n == 0:
        return acc
    return tail_factorial(n - 1, acc * n)  # ← tail call!  
```

NOT TAIL - CALL:
```
def not_tail_example(x):
    return 1 + another_function(x)  # ← Still needs to add 1 after call

Example:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # ← not a tail call
```

13. 🗑️ Which garbage collection strategy reclaims memory of objects that are no longer reachable from “roots”?
A. Reference Counting
B. Mark‑and‑Sweep  ← correct
C. Buddy Allocation
D. Memory Paging

# Note 1: Mark‑and‑Sweep traverses live objects from roots, then reclaims others.
# Note 2: Reference counting is a different strategy; C/D are unrelated memory schemes.

14. 🥇 In a language with first‑class functions, you can:
A. Only call functions defined at the top of the file
B. Pass functions as arguments to other functions  ← correct
C. Use functions only for arithmetic
D. Define functions without parentheses

- A language has first-class functions if functions are treated like any other variable.
That means you can:
  - Assign functions to variables
  - Pass them as arguments
  - Return them from other functions.
  - Store them in data structures
- This is very common in Python, JavaScript, etc.
- Example:

```
def greet(name):
    return f"Hello, {name}!"

def shout(text):
    return text.upper()

def call_func(func, value):
    return func(value)

result = call_func(greet, "Shahwar")
print(result)  # Output: Hello, Shahwar!

print(call_func(shout, "good morning"))  # Output: GOOD MORNING
```

# Note 1: First-class functions can be passed, returned, and assigned like variables.
# Note 2: B shows that flexibility; A, C, D are false constraints.

15. 🤖 Which of the following is an example of a logic programming language?
A. C++
B. Prolog  ← correct
C. Ruby
D. JavaScript

# Note 1: Prolog uses facts and rules for logical inference.
# Note 2: Other languages are imperative or object-oriented, not logic-based.

16. ↔️ In an object‑oriented language, the Liskov Substitution Principle concerns:
A. Replacing all methods with static functions
B. Ensuring subclasses can stand in for their base classes  ← correct
C. Hiding data inside classes
D. Using `switch` statements rather than `if`

# Note 1: LSP ensures subtype objects behave like their supertypes.
# Note 2: B is the formal definition; others are unrelated.

17. 🦆 Duck typing is most closely associated with which typing discipline?
A. Static strong typing
B. Static weak typing
C. Dynamic typing  ← correct
D. Manual memory management

# Note 1: Duck typing relies on runtime checks of behavior, not static types.
# Note 2: It is a form of dynamic typing; others don’t capture this.

18. 🎭 Which concurrency model uses “actors” that communicate by message passing?
A. Shared memory threads
B. Event‑driven callbacks
C. Actor model  ← correct
D. Fork/join

# Note 1: The actor model encapsulates state and interacts via asynchronous messages.
# Note 2: C is the standard model; others use different threading or event patterns.

19. 🚀 What is a primary advantage of Just‑In‑Time (JIT) compilation?
A. Code is never optimized
B. It avoids any translation step
C. It can optimize hotspots at runtime  ← correct
D. It produces pure source code

# Note 1: JIT compiles frequently executed code paths (“hotspots”) to optimized machine code.
# Note 2: C reflects that dynamic optimization; A/B/D are incorrect.

20. 📐 In a dependently typed language, types can depend on:
A. Environmental variables
B. Other types only
C. Values (terms)  ← correct
D. Compilation flags

# Note 1: Dependent types allow types to be parameterized by values (e.g., vector length).
# Note 2: C describes this power; A/B/D are not the core concept.
'''
