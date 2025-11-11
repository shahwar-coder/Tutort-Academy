'''
n=5, print following pattern
    *
   * *
  *   *
 *     *
*********
'''

n=5
for i in range(1, n):
    spaces = ' '*(n-i)
    stars_spaces_stars=''
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            stars_spaces_stars+='*'
        else:
            stars_spaces_stars+=' '
    print(spaces + stars_spaces_stars)
print('*'*(2*n-1)) # cool thing i did to have this last line separately printed.
    
            


