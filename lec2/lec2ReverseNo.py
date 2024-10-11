# 123 ---> 321


x_new = 0
x_temp = x

while(x_temp>0):
    x_new = x_new*10 + x_temp%10
    x_temp = x_temp/10

if(x_new == x):
    print("true")
else:
    print("false")        

print(10/3)
# 3.3333333333
print(10//3)
# 3    