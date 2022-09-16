a=9
b=3
# finding the greatest common divisor among this two


for i in range(min(a,b),1,-1):
    if a%i==0 and b%i==0:
        print(i)
        break

