
# reverse() --->  in place
                  # where it won't work --->
                  #  immutable ---> string etc
                  # can be use in list
                  # it works on mutuable sequence like lists.
                  # work in place, modify original one

my_list = [1,2,3,4,5]

print(my_list.reverse()) 
# None

my_list.reverse()
print(my_list)
# [1, 2, 3, 4, 5]

# where reverse() cannot be used,
# immutable ---> tuple, string

My_string = "Hello"
# My_string.reverse() ---> Will give Attribute Error, Property not define with it.

n = 123
#n.reverse() ---> will give attribute error




# reversed --->   Work with mutuable
                  # reversed(string) ---> will give error

# Will return a sequence in reversed order

# reverse_n = reversed(n)
# print(reverse_n) 
# TypeError: 'int' object is not reversible, same with reversed({1,2,3})

org_str = "hello"
rev_str = reversed(org_str)
# print(rev_str)
# <reversed object at 0x00000296737B13C0>


for char in rev_str:
    print(char)
# o
# l
# l
# e
# h

print(org_str)
# hello   ---> original string will remain unchanged



my_list = [1,2,3,4,5]
reverse_list = reversed(my_list)
print(reverse_list)
# <list_reverseiterator object at 0x000001D98D071630>

reverse_list = list(reversed(my_list))  # Typecast
print(reverse_list)
# [5, 4, 3, 2, 1]


my_tuple = {1,2,3,4,5}
# reverse_tuple = reversed(my_tuple)
# print(reverse_tuple)
# TypeError: 'set' object is not reversible  

