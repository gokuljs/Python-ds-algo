l1=["gokul",True,"hello world",1,2,3,4,5,6,7,8,9]
k="*"
n=5
l1[0]="pops"
print(l1)
l1[1:4]=[False,"Gokul JS",10]
print(l1)
l1[2:2]=["neman" ,"nikachu" ,"jalapeno"]
print(l1)
l1.insert(1,"goat")
print(l1)
l2=[1,2,3,4]
print(l2+[3,4,5,6,7,8,9])
l2.remove(3)
print(l2)
# l2.remove(3)
l2=l2+[3,4,5,6,7,8,9]
print(l2)
l2.pop()
print(l2)
l3=[[1,2,3],[4,5,6],[6,7,8],[6,7,8]]
print(len(l3[0]))
print(min(min(l3)))
print(l2[0:-1])
print("=======")
l2=[i for i in range(0,20)]
print(l2[-5:]) #to select only last five letters
print(l2[:-5]) # to select all except last five letters 
print(l2)
print(l2[0:-1:4])
print(list(range(0,100)))

