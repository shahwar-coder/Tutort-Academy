'''
Write a program that prompts the user to input a posiive integer. It should then print the multiplication table of that number.
'''

def write_multiplication_table(number: int)->None:
    """
    Print multiplication table till 10 for the number
    """
    for i in range(1, 11):
        print(f"{number} x {i} = {number*i}")

def take_integer_input(prompt: str)->int:
    """
    Ensure valid positive integer input
    """
    while True:
        try:
            number = int(input(prompt))
            if number<=0:
                print("Please enter valid positive integer.")
            else:
                return number
        except ValueError:
            print("Please enter a valid integer")

number=take_integer_input("Enter a positive integer: ")
write_multiplication_table(number)


'''
🧩 Multiplication Table — Flow

1️⃣  User Input → asks for a positive integer  
2️⃣  🔁 Validation → repeats until > 0 integer given  
3️⃣  ⚙️ Process → loop i = 1 → 10  
4️⃣  ✖️ Compute → number × i  
5️⃣  📤 Output → prints formatted table lines  
'''
