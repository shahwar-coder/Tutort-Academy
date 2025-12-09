'''
Printing jobs
'''

from collections import deque

printer_queue = deque(["Job1", "Job2", "Job3"])

while printer_queue:
    job = printer_queue.popleft()
    print("Printing:", job)

# Printing: Job1
# Printing: Job2
# Printing: Job3
