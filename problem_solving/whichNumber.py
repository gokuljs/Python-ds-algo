import math
num=int(input("enter your number"))
num_string=str(num)
finalSum=0
for i in num_string:
    finalSum+=math.pow(int(i),len(num_string))
if int(finalSum)==num:
    print(finalSum)
    print(num)
    print("it is armstrong number")
else:
    print("not armstrong number")

finalSum=0
for i in num_string:
    finalSum+=int(i)

if num%finalSum==0:
    print("this is Niven number")
else:
    print("this is not Niven number")


def fact(i):
    val=1
    for i in range(1,i+1):
        val=val*i
    return val

finalSum=0
for i in num_string:
    finalSum+=fact(int(i))

if finalSum==num:
    print("it is special number")
else:
    print("it is not special number")

finalSum=0
while finalSum!=1:
    for i in num_string:
        finalSum+=math.pow(int(i),2)
    if finalSum==1:
        break
    else:
        num_string=str(finalSum)
        finalSum=0