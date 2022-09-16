import sys
import math
import random
import threading
import time
from functools import reduce


# print("hello world")
# name=input("enter your name")
# print(name,"name")
# #comments
''' multi line comments '''
# Integers,floats,complex numbers strings booleans
# print(type(10))
# print(sys.maxsize)
# print(sys.float_info.max)

# # complex numbers
# # first is real numbers and then is complex numbers
# cn1=5+6j
# b1=False
# str="Escape sequences \' \" \t \\"
# print(int(5.4))
# print(ord('a')) # converts a character into a string
# print(chr(97)) # converts integer into string based on ascii value
# print(11,19,1999,sep="/")
# print("no new line",end="")
# print(11,19,1999,sep="/")


# ## math functions
# print("5+2",5+2)
# print("5-2",5-2)
# print("5*2",5*2)
# print("5/2",5/2)
# print("5/2",5%2)
# print("5**2",5**2)
# print("5//2",5//2),

# print("rand",random.randint(1,100))


# #  Now coming to NAn and infinity
# print(math.inf<0)

# age= True if 19>20 else False
# print(age,"age")


# strings

print("hello"+"world")
print(r"i' will be ignored")
str1 = "hellow orld smaskj"
print("lenght", len(str1))
print(str1[0])
print(str1[-1])
print(str1[0:3])
print(str1[::-1])
print(str1[0:-1:2])
str1 = str1.replace("hellow", "hello")
print(str1)
str1 = str1[:6] + "w" + str1[6:]
print(str1)
print("world" not in str1)
print("hello" in str1)
print("you index", str1.find("world"))
print("  hello   ".lstrip())

# converting a list into a string
list = ["hello", "world", "come herer"]
print(" ".join(list))
# converting string to list
hello = "welcome to the new world"
print(hello.split(" "))
print("loweTUGSDGS".lower())
print("loweTUGSDGS".upper())

# checking out if a string is a character or number
print("Astring123".isalnum())  # to check alphabets and number
print("Astring".isalpha())  # to check alphabets
print("1212".isdigit())  # checking everything is number


# list
l = [i for i in range(0, 11)]
print(len(l))
print(l[1])
print(l[-1])
# print(l[2:2])
l[0] = "newton is dead"
print(l)
l[2:4] = ["relativity is dead", "newton is no more"]
print(l)
l[2:2] = [[i for i in range(10, 20)]]
print(l)
l1 = [i for i in range(10, 15)]+l
print(l1)
l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l2[1][1])
l = [i for i in range(11)]
print(1 in l)
print(min(l))
print(max(l))
print(l[0:-1:5])
print(l[::-1])


# loops
l = [i for i in range(11)]
w = 1

while w < 5:
    w = w+1
print(w)

w2 = 0
while w2 <= 20:
    if(w2 % 2 == 0):
        print(w2)
    elif(w2 == 9):
        break
    else:
        w2 += 1
        continue
    w2 += 1

print("=====")
l = [i for i in range(11)]
while len(l):
    print(l.pop(0))


# for loops
for x in range(0, 10):
    print(x, end=" ")

l = [1, "Sdsdsd", "Sdsdsd", "Sdsdsd"]
for x in l:
    print(l)


# iterators

s = "aaaaaaandsjkd"
print(s.replace("a", "", 4))
