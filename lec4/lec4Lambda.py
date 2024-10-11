# python has lambda function ---> takes n no of arguments, ---> single expression

# lambda argument:expression
x = lambda a:a+10

y = x(5)
print(y)  # or print(x(5))
#15

x = lambda a,b:a+b
print(x(5,6))
#11

z = lambda a,b,c: a+b+c
print(z(1,2,3))
#6

# Mostly usage ---> where some function is inside another function

def func(n):
    return lambda a:a*n

x = func(2)  # n=2
print(x(2))  # a=2
#4
print(x(3))  # a=3
#6

