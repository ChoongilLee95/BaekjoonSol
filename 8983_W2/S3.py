import sys
sys.setrecursionlimit(10**6)
def binary_search(li,left:int, right:int,target):
    if left+1==right:
        return [li[left],li[right]]
    mid = (left+right)//2
    if li[mid] ==target:
        return [li[mid]]
    elif li[mid]<target:
        return binary_search(li,mid,right,target)
    else:
        return binary_search(li,left,mid,target)
def binary_search2(li,left:int, right:int,target):
    while left+1 != right:
        mid = (left+right)//2
        if li[mid] ==target:
            return [li[mid]]
        elif li[mid]<target:
            left = mid
        else:
            right = mid
    return [li[left],li[right]]

M,N,L  = map(int,sys.stdin.readline().strip().split())

shooters  = list(map(int,sys.stdin.readline().strip().split()))
ans = 0
shooters.sort()

for i in range(N):
    x,y = map(int,sys.stdin.readline().strip().split())
    if y>L:
        continue
    else:
        j_list = binary_search(shooters,0,M-1,x)
        for j in j_list:
            if y+abs(x-j)-L<=0:
                ans+=1
                break
print(ans)