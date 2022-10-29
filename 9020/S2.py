import sys

num_tc  = int(sys.stdin.readline().strip())

def sosu(n:int):
    root_n = int(n**(1/2))
    if n ==2:
        ans = True
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


for tc in range(num_tc):
    ans =''
    n = int(sys.stdin.readline().strip())
    if n ==4:
        ans = f'{2} {2}'
    else:
        if n%4==0:
            start = int(n/2+1)
        else:
            start = int(n/2)
        for i in range(start,n,2):
            if sosu(i):
                if sosu(n-i):
                    ans = f'{n-i} {i}'
                    break
                else:
                    continue
            else:
                continue
    print(ans)



