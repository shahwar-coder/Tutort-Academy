'''
- Concurrency : When multiple tasks are in progress at the same time.
- Python has 3 concurrency models:
1. Threading
2. Multiprocessing
3. AsyncIO
'''

'''
1. THREADING 🧵📗

- THREADING : Threading let's your program do two or more things at same time,
especially while waiting for something.  eg. downloading a file.

2. Why do we use threading ?
- To make programs faster and responsive when doing I/O tasks:
- "Waithing for website response"
- "Reading or Writing a file"
- "Downloading a file"
- "Delaying using sleep"
'''

# Simple Example:
'''
- We will use one of the threading things which is WAITING/DELAY
'''

import threading
import time

# 1. Define the Thread
def say_hello():
    # Indication of thread starting...
    print("'say_hello' function is the threading part, Threading is saying hello from there.")
    # Thread activity eg. wait/delay
    time.sleep(2)
    # Finish Thread task
    print("The Thread has stopped now..!")

# 2. Create the Thread
t = threading.Thread(target=say_hello)

# 3. Start the Thread
t.start()

# Main program will continue irresoective
print("Main programme continues..")

# 4. Wait for thread (to finish)
t.join()

# Now the main program finishes
print("Main program is done...")

'''
```
Hello from thread!
Main program continues...
Thread is done!
Main program done.
```
'''

# Revising points understood:
'''
- A function `say_hello()` is defined, which simulates a delay using `time.sleep(2)`.
- A Thread is created to run the `say_hello()` function independently.
- `t.start()` starts the thread. It begins execution in parallel with the main program.
- While the thread is sleeping (for 2 seconds), the main program continues to run and prints "Main programme continues..".
- The thread wakes up after 2 seconds and prints "The Thread has stopped now..!".
- `t.join()` tells the main program to wait for the thread to finish before proceeding.
- After the thread finishes, the main program prints "Main program is done...".
'''

