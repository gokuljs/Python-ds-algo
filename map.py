from functools import reduce


list1=range(0,10)
times_2=lambda x:x*2
# print(list(map(times_2,list1)))
# print(list(filter(lambda x:x%2==0,range(0,20))))

## reduce 
# receive a list and return a single values
print(reduce(lambda x,y:x+y,range(0,4)))