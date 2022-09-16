n = int(input("enter your number"))
print(n)
answer = 1
for i in range(1, n+1):
    print(i, "i")
    answer = answer*i
    print(answer, "answer")
print(answer)
