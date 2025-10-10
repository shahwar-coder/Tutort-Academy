'''
Write a program to calculate the factorial of a given number. Like,
5! = 120
'''

def calculate_factorial(number: int)->int:
    """
    Calculate factorial of a number (recursion)
    """
    if number==1:
        return 1
    return number * calculate_factorial(number-1)

def take_valid_integer(prompt: str)->int:
    """
    Ensure valid integer input
    """
    while True:
        try:
            number=int(input(prompt))
            if number<=0:
                print("Please enter a positive valid integer.")
            else:
                return number
        except ValueError:
            print("Enter a valid integer.")
    
number=take_valid_integer("Enter a valid integer: ")
print(calculate_factorial(number))




'''
🧩 Factorial Program — Flow

1️⃣  🖊️ User Input → prompts for a positive integer  
2️⃣  🧠 Validation → rejects 0, negatives, or non-numeric entries  
3️⃣  🔁 Recursion → 
     • base case → 1 returns 1  
     • recursive case → n × factorial(n−1)  
4️⃣  🧮 Calculation unfolds → multiplies downward till 1  
5️⃣  📤 Output → prints final factorial result (e.g., 5! = 120)  
'''
