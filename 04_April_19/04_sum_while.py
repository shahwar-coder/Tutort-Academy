'''
Sum of digits (using while loop)
Eg.
i/p: 286
o/p: 16
'''

def add_digits(number: int)->int:
  """
  Calculate sum of digits
  """
  number=abs(number)
  sum=0
  while number!=0:
    digit=number%10
    sum+=digit
    number//=10
  return sum
  

def take_integer_input(prompt: str)->int:
  """
  Ensure valid integer input
  """
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter a valid integer.")

number=take_integer_input("Enter an integer: ")
print(add_digits(number))


'''
🧩 Sum of Digits — Execution Flow

• 🧮 Input: User enters an integer (validated via while + try/except).  
• 🔄 Processing:  
   → Convert to positive with abs()  
   → Loop: extract each digit using %10  
   → Add digits cumulatively, then //=10 to move left  
• 📤 Output: Print total sum of digits.  
'''
