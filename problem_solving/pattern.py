import math
pattern=input("enter your pattern")
pattern=pattern+" "
loop=int(input("enter number of loops you want to print this"))
for i in range(loop+1):
    print(pattern*i,end=" ")
    print(" ")

for i in range(loop+1):
    print(" "*(loop-i),end="")
    print(pattern*i)
for i in range(2):
    print(" "*(loop-1),end="")
    print(pattern)

print(" ")

for i in range(loop):
    print(" "*(loop-i),end="")
    print(pattern*i)

print(" ")

for i in range(loop+1):
    print(" "*abs(loop-i),end="")
    print("*"*i)


for i in range(loop):
    print(" "*(loop-i),end="")
    print(pattern*i)
for i in range(loop,-1,-1):
    print(" "*(loop-i),end="")
    print(pattern*i)
