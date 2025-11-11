'''
*****
****
***
**
*
**
***
****
*****
'''

n=5
for i in range(n, 0, -1):
    stars='*'*i
    spaces=' '*(n-i)
    print(stars+spaces)
for i in range(2, n+1):
    stars='*'*i
    spaces=' '*(n-i)
    print(stars+spaces)


'''
Step-by-step explanation:

1️⃣ First loop prints inverted triangle:
    ***** → *
   (stars decrease each row)

2️⃣ Second loop prints normal triangle:
    ** → *****
   (stars increase each row)

3️⃣ Start second loop at 2 to avoid repeating the center '*'.

Result:
*****
****
***
**
*
**
***
****
*****
'''
