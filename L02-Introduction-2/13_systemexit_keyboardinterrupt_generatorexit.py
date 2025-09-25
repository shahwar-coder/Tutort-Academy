'''
Q. What is SystemExit and when does it occur?
Ans:
- Raised when sys.exit() is called.
- Used to terminate program gracefully.

Example:
'''
import sys

try:
    sys.exit("Goodbye")
except SystemExit as e:
    print("Caught:", e)

# Step-by-step:
# 1. sys.exit("Goodbye") raises SystemExit.
# 2. We catch it in try/except → prints "Caught: Goodbye".



'''
Q2. What is KeyboardInterrupt and how does it happen?
Ans:
- Raised when user presses Ctrl+C in terminal.
- Lets us handle user-initiated interruptions.

Example:
'''
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted by user")



'''
Q3. What is GeneratorExit and when is it raised?
Ans:
- Raised when a generator’s close() is called.
- Useful for cleanup inside generators.

Example:
'''
def gen():
    try:
        yield 1
    finally:
        print("Generator closed")

g = gen()
print(next(g))
g.close()

# Step-by-step:
# 1. Generator yields 1.
# 2. g.close() raises GeneratorExit inside.
# 3. finally block runs → "Generator closed".



'''
Q4. How do quit() and exit() work?
Ans:
- Convenience functions for interactive mode.
- Internally, they just raise SystemExit.

Example:
'''
try:
    exit("Bye!")
except SystemExit as e:
    print("Intercepted:", e)

# Step-by-step:
# exit() = wrapper for sys.exit().
# Raises SystemExit → we can catch if needed.



'''
Q5. How do these exceptions differ from normal errors?
Ans:
- They’re not bugs; they’re control signals.
- SystemExit/KeyboardInterrupt/GeneratorExit are subclasses of BaseException (not Exception).
- This ensures they can bypass normal except Exception handlers.
'''



'''
Q6. Quick shorthand
- SystemExit → program termination (sys.exit).
- KeyboardInterrupt → user pressed Ctrl+C.
- GeneratorExit → generator close() called.
- quit()/exit() → wrappers raising SystemExit.
'''
