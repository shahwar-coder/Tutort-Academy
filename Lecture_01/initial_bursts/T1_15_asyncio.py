'''
1. Asyncio?
- It is a way to run many tasks at same time
- Especially in case of "waiting"
- Like APIs or Downloading

2. Great For:
- Downloading 1000 web pages.
- Waiting for APIs
- Chat servers
- Sockets
- Files I/O with delays

3. Key concepts are 3:

a. `async def` : Declares an async function (can await)
b. `await` : Tells python "wait here and let others run"
c. `asyncio.run()` : Starts the async program (like main())
'''

# Example:
import asyncio

async def task():
    print("Start Task..")
    await asyncio.sleep(2) # the task
    print("End Task..")

async def main():
    await task() # run the task

asyncio.run(main())


# OUTPUT:
'''
Start task
(wait 2 seconds)
End task
'''

# Program Flow:
'''
1. `task()` is defined as an **async function** using `async def`.

2. Inside task(), `await asyncio.sleep(2)` means:
   - Pause here and let other things run (if any).
   - It's like a "non-blocking sleep".

3. The `main()` function also uses `async def`, and runs `await task()`.

4. `asyncio.run(main())` kicks off the whole async system.

✅ Even though it only runs one task, it does so **without blocking** the whole program.

🧠 If you had more tasks, they would all **share time** efficiently.
'''
