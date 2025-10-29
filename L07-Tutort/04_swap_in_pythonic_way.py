# arr[i], arr[i+1] = arr[i+1], arr[i]

'''
Idiomatic swap in Python:

1. Traditional way:
   temp = arr[i]
   arr[i] = arr[i+1]
   arr[i+1] = temp

2. Pythonic way:
   arr[i], arr[i+1] = arr[i+1], arr[i]

3. How it works:
   - Right side forms a tuple (arr[i+1], arr[i])
   - Left side unpacks the tuple back into arr[i], arr[i+1]
   - Both assignments happen simultaneously

4. Example:
   a, b = 10, 20
   a, b = b, a
   print(a, b)  # 20 10

5. Benefits:
   - Concise, safe, and idiomatic
   - Works for variables, list elements, etc.
'''
