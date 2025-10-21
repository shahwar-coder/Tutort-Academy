
'''
n=5
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''

n=5
for i in range(1, n+1):
    left_spaces=" "*(n-i)
    middle_spaces=" "*(2*(i-1))
    if i==1:
        print(left_spaces + "*")
    else:
        print(left_spaces + "*" + middle_spaces + "*")
        
for i in range(n-1, 0, -1):
    left_spaces=" "*(n-i)
    middle_spaces=" "*(2*(i-1))
    if i==1:
        print(left_spaces + "*")
    else:
        print(left_spaces + "*" + middle_spaces + "*")
