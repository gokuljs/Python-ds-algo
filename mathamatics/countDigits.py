val=121
tem=val
rev=0
while val>0:
    rev=rev*10+val%10
    val=val//10
if rev==tem:
    print("palindrome number")
else:
    print("not palindrome number")
