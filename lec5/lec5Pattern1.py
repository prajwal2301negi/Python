n = int(input("Enter Number "))

for i in range(0,n):
    if i == 0:
        print(' '*(n-1), end = '')  # end must be empty, else next line me print ho jayega
        print('*'*n)
    elif i == n-1:
        print('*'*n)
    else:
        for j in range(0, n-i-1):
            print(" ", end = '')
        print('*', end = '')
        print(' '*(n-2), end = '')    
        print('*')  
    
