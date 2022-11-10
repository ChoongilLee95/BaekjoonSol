import sys
## 93퍼까진 간 풀이
def binary_search(li,left:int, right:int,target):
    while left <= right:
        mid = (left+right)//2
        if li[mid] ==target:
            return [li[mid]]
        elif li[mid]<target:
            left = mid+1
        else:
            right = mid-1
    if left > len(li)-1:
        return [li[right]]
    elif right <0:
        return [li[left]]
    else:
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
            if y+abs(x-j)-L<1:
                ans+=1
                break
print(ans)