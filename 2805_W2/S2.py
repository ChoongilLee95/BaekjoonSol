import sys


a, b  = map(int, sys.stdin.readline().strip().split())
li = list(map(int,sys.stdin.readline().strip().split()))


maxi = max(li)-b//a
old_mid =0
num_li = list(range(0,maxi+1))
def binary_search(left:int, right:int,target):
    global maxi
    global old_mid
    total = 0
    if left>right:
        return old_mid
    mid = num_li[(left+right)//2]
    for wood in li:
        total += wood-mid if wood-mid>0 else 0
    if total ==target:
        return mid
    elif total>target:
        old_mid = mid
        return binary_search((left+right)//2+1,right,target)
    else:
        return binary_search(left,(left+right)//2-1,target)
print(binary_search(0,maxi+1-b//a-1,b))

