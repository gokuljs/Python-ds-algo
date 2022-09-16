prime=[]
flag=False
for i in range(2,408):
    for j in range(2,i):
        if i%j!=0:
            flag=True
        else:
            flag=False
            break
    if flag==True:
        prime.append(i)
    flag=False
print(prime)
print(prime[0:-1:2])


