from math import gcd

num = int(input())
flag = True
for i in range(2, num):
    if gcd(i, num) != 1:
        flag = False
        break
if flag and num > 1:
    print('This number is prime')
else:
    print('This number is not prime')
