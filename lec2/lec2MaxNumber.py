

def maximum_number(a,b,c):
    if(a>=b and a>=c):
        largest = a
    elif(b>=a and b>=c):
        largest = b
    else :
        largest = c
    return largest   # every time largest will create locally

a = int(input('Enter first no.'))  
b = int(input('Enter second no.')) 
c = int(input('Enter third no.'))

ans = maximum_number(a,b,c)
print(ans)