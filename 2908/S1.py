import sys

num1 = ''
num2 = ''

a, b = sys.stdin.readline().strip().split()

for i in range(2,-1,-1):
    num1 += a[i]
    num2 += b[i]

if int(num1)>int(num2):
    print(num1)
else:
    print(num2)



