'''
1. COROUTINE:
- A special function
- It can pause at certain point (eg. allow `yield` to finish), then resume at the same point.
- This can allow asynchronous, non-blocking execution
- It can be called a sfunction with memory

2. Regular Functions vs Coroutines:
| Regular Function             | Coroutine                   |
| ---------------------------- | --------------------------- |
| Runs start to end            | Can pause and resume        |
| Uses `return`                | Uses `yield` or `await`     |
| One-way communication        | Two-way (send & receive)    |
| No state saved between calls | Remembers state after pause |

'''

# Example:

def simple_coroutine():
    print("Coroutine started..")
    x=yield
    print("Received : ", x)

# Create Coroutine
coro = simple_coroutine()

# Start Coroutine
next(coro)

# Send Value
coro.send(42)


'''
1. `next(coro)` starts the function, pauses at `yield`.
2. `coro.send(42)` sends value into coroutine and resumes execution.
'''

'''
3. What is yield doing here ?
- `yield` : pauses the function and waits for the value to be sent
- when we send a vlaue using `.send()` , the value is received at the yield line
- Hence Two-Way communication is allowed by coroutines
'''

# An Example to observe:
def greeter():
    print("Ready to greet someone...")
    while True:
        name = yield
        print(f"Hello, {name}!")

g = greeter()
next(g)         # Prime the coroutine
g.send("Alice") # Prints: Hello, Alice!
g.send("Bob")   # Prints: Hello, Bob!


'''
1. Coroutine starts and waits at yield.
2. You send names, and it greets them.
3. Loop continues — doesn't restart from top!
'''

# Let's revise steps in Coroutine:
'''
| Operation      | What it does                                  |
| -------------- | --------------------------------------------- |
| `next(coro)`   | Starts coroutine and runs until first `yield` |
| `coro.send(x)` | Resumes and sends data into coroutine         |
| `coro.close()` | Stops coroutine                               |
'''
