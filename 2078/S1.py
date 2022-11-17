import sys
input = sys.stdin.readline

a,b = map(int,input().split())
left = 0
right = 0

while a>1 and b>1:
    if a >b:
        left += (a//b)
        a %=b
    else:
        right +=(b//a)
        b %=a
if a==1 and b==1:
    print(left,right)
else:
    if a > 1:
        left += a-1
    else:
        right +=b-1
    print(left,right)
