'''
1. 🧩 What is “duck typing” primarily concerned with?
A. The actual type of an object
B. The methods and properties an object supports  ← correct
C. Memory layout of objects
D. Compile-time type checking

# Note 1: Duck typing means “if it quacks like a duck…”, focusing on an object's capabilities.
# Note 2: B is correct; A, C, D relate to static or memory concerns, not behavior.

2. 🔗 Which concept prevents direct access to object internals in OOP?
A. Inheritance
B. Polymorphism
C. Encapsulation  ← correct
D. Abstraction

# Note 1: Encapsulation bundles data and methods, hiding internal state.
# Note 2: C matches hiding; A/B extend or overload behavior; D is simplifying interface.

3. 🔄 What does “idempotent” mean in the context of functions or operations?
A. Can be applied multiple times with no additional effect  ← correct
B. Changes with each call
C. Raises an error on second call
D. Only works once per program

# Note 1: Idempotence means repeated calls yield same result without side effects.
# Note 2: A matches definition; B–D are opposite or unrelated.

4. 🧮 Which algorithmic complexity describes binary search on a sorted array?
A. O(n)
B. O(n log n)
C. O(log n)  ← correct
D. O(1)

# Note 1: Binary search halves the search space each step → logarithmic.
# Note 2: C is correct; A is linear, B is sort-like, D is constant.

5. ⚠️ In exception handling, which block is guaranteed to execute whether an exception occurs or not?
A. try
B. except
C. finally  ← correct
D. else

# Note 1: finally always runs for cleanup.
# Note 2: C is correct; except only on errors; else runs only if no error.

6. 🎯 What does the “volatile” keyword in some languages signify?
A. A variable stored on the heap
B. A variable that can be changed by external factors  ← correct
C. A read-only constant
D. A compile-time macro

# Note 1: volatile prevents certain compiler optimizations.
# Note 2: B matches its role; A/C/D are incorrect qualifiers.

7. 🧵 Which model uses shared memory protected by locks?
A. Actor model
B. CSP (Communicating Sequential Processes)
C. Thread-based concurrency  ← correct
D. Event-driven callbacks

# Note 1: Thread concurrency uses shared memory and locks.
# Note 2: C matches; A uses message passing, B uses channels, D is single-threaded.

8. 🔒 What does “SQL injection” exploit?
A. Overflow bugs
B. Improper input sanitization  ← correct
C. Race conditions
D. Garbage collection

# Note 1: SQL injection uses unsanitized inputs in queries.
# Note 2: B is correct; A/C/D are unrelated security issues.

9. 🧠 Which sorting algorithm is in-place and stable?
A. Quick sort
B. Merge sort
C. Insertion sort  ← correct
D. Heap sort

# Note 1: Insertion sort shifts elements and keeps order of equals.
# Note 2: C matches; quick and heap are unstable, merge isn’t in-place by default.

10. 🎨 Which language paradigm treats computation as evaluation of mathematical functions?
A. Procedural
B. Functional  ← correct
C. Object‑Oriented
D. Event‑Driven

# Note 1: Functional paradigm avoids side effects, uses pure functions.
# Note 2: B matches definition; others focus on statements, objects, or events.

11. ⚙️ In dependency injection, what is “inversion of control”?
A. Components control their dependencies
B. Dependencies are created inside components
C. Framework provides dependencies to components  ← correct
D. Components cannot use external libraries

# Note 1: IoC means the framework injects dependencies.
# Note 2: C matches; A/B are normal control flow, D is false.

12. 🔢 Which numeric type offers arbitrary precision in Python?
A. float
B. int  ← correct
C. complex
D. decimal

# Note 1: Python’s int grows to any size limited by memory.
# Note 2: B is correct; float and complex are fixed precision; decimal is fixed context.

13. 🔍 What is “memoization”?
A. Storing log messages
B. Caching function results for reuse  ← correct
C. Encrypting data
D. Writing documentation

# Note 1: Memoization speeds up repeated calls by caching.
# Note 2: B matches; others are unrelated tasks.

14. 🔄 Which HTTP method is considered “idempotent”?
A. POST
B. GET  ← correct
C. PATCH
D. CONNECT

# Note 1: GET returns the same resource without side effects.
# Note 2: B is idempotent; POST/PATCH modify, CONNECT negotiates.

15. ⏳ What does “thundering herd” refer to in concurrency?
A. Too many locks
B. Many threads awaken simultaneously on an event  ← correct
C. Lack of threads
D. Infinite recursion

# Note 1: The thundering herd causes performance bottlenecks.
# Note 2: B matches; A/C/D are different issues.

16. 🛡️ Which is a principle of secure design: “Fail‑secure” means?
A. System continues in unsafe mode on error
B. System denies access if safe completion isn’t possible  ← correct
C. System logs but proceeds
D. System retries indefinitely

# Note 1: Fail‑secure denies operations to avoid vulnerabilities.
# Note 2: B matches; A/C/D risk unsafe behavior.

17. 🔧 What is a “broken arrow” in software testing?
A. A failed unit test  ← correct
B. A deprecated API
C. A memory leak
D. A continuous integration pipeline

# Note 1: “Broken Arrow” is slang for test suite failure detection.
# Note 2: A matches; others are different software issues.

18. 🧪 Which metric does code coverage measure?
A. Lines of code executed by tests  ← correct
B. Complexity of algorithms
C. Execution speed
D. Memory usage

# Note 1: Coverage tools report which code lines run under tests.
# Note 2: A matches; B/C/D are unrelated metrics.

19. 📦 In package management, what does “semver” stand for?
A. Secure versioning
B. Semantic Versioning  ← correct
C. Simple Versioning
D. Sequential Versioning

# Note 1: SemVer uses MAJOR.MINOR.PATCH rules.
# Note 2: B is correct; others aren’t standard terms.

20. ⚡ Which language feature allows code to run asynchronously without threads?
A. Callbacks
B. Coroutines  ← correct
C. Inheritance
D. Lambda expressions

# Note 1: Coroutines yield control and resume cooperatively.
# Note 2: B matches async features; A uses callbacks, C/D are unrelated.
'''
