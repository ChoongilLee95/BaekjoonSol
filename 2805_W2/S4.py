import sys
import heapq

num_li = []
a, b  = map(int, sys.stdin.readline().strip().split())
li = list(map(int,sys.stdin.readline().strip().split()))
for i in li:
    heapq.heappush(num_li, -1)
max_high = abs(num_li[0])



old_mid =0
num_li = list(range(0,31))
def binary_search(left:int, right:int,target):
    global old_mid
    total = 0
    if left>right:
        return old_mid
    mid = num_li[(left+right)//2]
    for wood in li:
        total += wood-2**mid if wood-2**mid>0 else 0
    if total ==target:
        return mid
    elif total>target:
        old_mid = mid
        return binary_search((left+right)//2+1,right,target)
    else:
        return binary_search(left,(left+right)//2-1,target)

a = binary_search(0,31,b)

start = 2**a
end = 2**(a+1)-1

def binary_search_2(left:int, right:int,target):
    global old_mid
    total = 0
    if left>right:
        return old_mid
    mid = (left+right)//2
    for wood in li:
        total += wood-mid if wood-mid>0 else 0
    if total ==target:
        return mid
    elif total>target:
        old_mid =mid
        return binary_search_2(mid+1,right,target)
    else:
        return binary_search_2(left,mid-1,target)
print(binary_search_2(start,end,b))
print(2**30)