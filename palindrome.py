s = input("enter your string to check is it palindrome or not")
if(s == s[::-1]):
    print("palindrome")
else:
    print("not palindrome")
