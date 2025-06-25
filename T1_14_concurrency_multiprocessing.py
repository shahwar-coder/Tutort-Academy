'''
1.MULTIPROCESSING:
- Multiprocessing means , running multiple parts of your program, using multiple CPU cores.
- Unlike threads, which runs on single core, mutiprocessing actually involves multiple cores of the CPU. 

2. When to use?
- Use multiprocessing for CPU heavy tasks:
    - Image Processing
    - Data Analysis

3. Not to use for?
- Simple I/O tasks (use threads or asyncio instead)
'''

# Example
# Let's run multiple processes:

import multiprocessing
def do_the_square(num: int)->int:
    "Function that squares the input number"
    print(f"{num}² : {num**2}")

if __name__=="__main__":
    numbers=[1,2,3,4]
    processes=[]

    for num in numbers:
        p=multiprocessing.Process(target=do_the_square(num))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()



# OUTPUT:
'''
Main program continues...
Process started
Process finished
Main program done.
'''

# FLOW:
'''
1. The function `task()` is defined to simulate some work:
   - It prints "Process started"
   - Waits for 2 seconds
   - Prints "Process finished"

2. A new **process** is created using:
   → multiprocessing.Process(target=task)

3. `.start()` launches the task in a **separate process**, 
   meaning it runs **parallel** to the main program.

4. While the process is running `task()`, 
   the main program **immediately prints**:
   → "Main program continues..."

5. `.join()` makes the main program **wait** until the process finishes.

6. After the process finishes (after 2 seconds), 
   → it prints "Process finished"
   → and then main program prints "Main program done."

✅ Conclusion:
- This is **true parallelism**.
- Perfect for **CPU-heavy** or blocking work.
- Both parts run **at the same time** on separate CPU cores.
'''
