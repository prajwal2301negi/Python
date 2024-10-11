restaurants = ["mcdonald", "burger king", " kfc", "subway", "kfc"]
unique_res = set(restaurants)
print(unique_res)
# {'kfc', 'burger king', 'mcdonald', ' kfc', 'subway'}

# set is not the same order as the original list. Sets-> unordered.
# Where unorder is present, write sets.

l1 = list(unique_res)
print(l1)
# ['kfc', 'subway', 'burger king', 'mcdonald', ' kfc']

# list is the same order.

my_set = {3,1,4,1,5,9}
print(my_set)
# {1, 3, 4, 5, 9}. set has uniqueness -> 1 is appearing 1 time only.

my_list = list(my_set)
print(my_list)
# [1, 3, 4, 5, 9]


# Set --->
# 1. Unordered  --> do not maintain order of insertion
#               --> hash to store the table.
#   Hashing -->
#               A ---> 1
#               B ---> 2
#               C ---> 3


for num in my_list:
    print(num)
# 1
# 3
# 4
# 5
# 9

# Input-> input() ---> return string

name = input("Enter your name")
age = int(input('Enter age'))
height = int(input("Enter height"))
response = input("Enter response -> Yes/No")

is_answer = response.lower() == "yes"
print(is_answer)  #yEs
# True

