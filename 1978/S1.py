import sys


def sosu(n:int):
    root_n = int(n**(1/2))
    if n ==2:
        ans = True
    elif n %2 ==0:
        ans = False
    elif root_n == n**(1/2):
        ans =False
    elif root_n>2:
        ans = True
        for i in range(3,root_n+1,2):
            if n%i==0:
                ans = False
                break
            else:
                continue
    else:
        ans=True
    return ans

num_tc  = int(sys.stdin.readline().strip())
nums= map(int,sys.stdin.readline().strip().split())

ans = 0
for i in nums:
    if sosu(i):
        ans +=1
    else:
        continue
print(ans)
