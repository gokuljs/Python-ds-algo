# prime factorization of a number containing  2 and 5 will give you trailing zeros
# always remember no of prime factors of 5 is always less than 2 so just see number of 5 prime factors occurs

from re import I


n=100
i=5
count=0
while(n/i>=1):
    count=count+n//i
    i*=5
print(count)
