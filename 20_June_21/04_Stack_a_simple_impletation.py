'''
❓ Problem: Remove All Stars ⭐
Given a string s, remove a character before every '*' character.
Return the final string after all operations.

📌 Rule:
When you see '*', remove the previous character (using stack behavior)
Remove the '*' too

INPUT:
s = "ab*c*d"

PROCESS:
push 'a' → ['a']
push 'b' → ['a','b']
'*' removes 'b' → ['a']
push 'c' → ['a','c']
'*' removes 'c' → ['a']
push 'd' → ['a','d']

OUTPUT:
"ad"
'''

def removeStars(s):
    stack = []
    
    for ch in s:
        if ch == '*':
            if stack:
                stack.pop()  # remove previous char
        else:
            stack.append(ch)
    
    return "".join(stack)


# Test cases
print(removeStars("ab*c*d"))  # Output → "ad"
print(removeStars("abc**"))   # Output → "a"
print(removeStars("****"))    # Output → ""



