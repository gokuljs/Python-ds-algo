def addSum(num1:int=1,num2:int=1):
    return num1+num2

print(addSum(10,14))

#now when you dont know how many values your going to get 

def getSum2(*args):
    sum=0
    for arg in args:
        sum+=arg
    return sum

print(getSum2(1,2,3,4,5,6))


#returning the multiple values

def new(num):
    return num+1,num+2,

i1,i2=new(5)
print(i1)
print(i2)