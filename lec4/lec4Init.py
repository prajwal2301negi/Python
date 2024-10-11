# __init__()

# built in function
# function to assign values

class P:
    def __init__(self, name, age):   # if function is use in class ---> init() is use. It helps to initialise the instance.
        self.name = name
        self.age = age

p1 = P("ABC", 12)
print(p1.age)
print(p1.name)
# 12
# ABC


class c2:
    def __init__(self, x):
        self.x = x
    def display(self):
        print(self.x)

obj = c2(4) 
obj.display()
# 4      

class Person:
    def __init__(self,n,a):
        self.n = n
        self.a = a
    def myfunc(self):
        print("Hiii", self.n)

p1 = Person("ABC", 12)
p1.age = 10   # modify
del p1.age    # delete
#del p1        # whole delete
p1.myfunc()
# Objects can contain functions, methods in objects are functions that belong to the object            


class Per:
    pass
# pass is a placeholder when we don't want to do anything in a function or class. It 
# is a null operation -- when it is executed, nothing happens.

# creation of Parent class
class SPerson:
    def __init__(self, f, l):
        self.f = f
        self.l = l
    def printName(self):
        print(self.f, self.l)

x = SPerson("A","B")
x.printName()


# creation of child class
class Student(SPerson):
    pass
x = Student("C","D")
x.printName()

class Person:
    def __init__(self, f, l):
        self.f = f
        self.l = l
    def printName(self):
        print(self.f, self.l)

class Student(Person):
    def __init__(self, f, l, age):
        super().__init__(f, l)   # Adding new Property
        self.age = age           # We can add properties

x = Student("a","b", 20)
x.printName()