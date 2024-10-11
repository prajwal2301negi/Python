fruits = ["apple","banana","cherry"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry


num = 1
while num<=5:
    print(num)
    num+=1
# 1
# 2
# 3
# 4
# 5

# range --->  (start, stop, step)
print("start")
for i in range(5):
    print(i)
# start
# 0
# 1
# 2
# 3
# 4

print("stop")
for i in range(2,5):
    print(i)
# stop
# 2
# 3
# 4


print("step")
for i in range(1, 10, 2):
    print (i)    
# step
# 1
# 3
# 5
# 7
# 9


# for ---> use whne no of iterations are known. It is entry control, known to us when it will end

# while ---> use when no of iterations are not known. It is exit control, when function exit, we get to know

