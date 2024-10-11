# Sorting

my_list = [1,3,4,2,5,9]

# sort --> inplace sorting. Will modify original list. Will not return a new sorted list.
# It cannot be used with other iterables like tuples/ strings.

# sorted ---> sortes iterable tuples/ string sort return new list does not modify original. Can be used woith everything. Will return a new list, does not modify original one.

my_list.sort()
print(my_list)
# [1, 2, 3, 4, 5, 9]

sorted_list = sorted(my_list)
print(sorted_list)
# [1, 2, 3, 4, 5, 9]

my_list = "hello"
print(sorted(my_list))
# ['e', 'h', 'l', 'l', 'o']
# print(my_list.sort()) --> 
# AttributeError: 'str' object has no attribute 'sort'
# Will not work with tuples, set, strings, maps, dictionary

