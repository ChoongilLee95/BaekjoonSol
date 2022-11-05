from typing import MutableSequence
import sys


a, b  = map(int, sys.stdin.readline().strip().split())
li = list(map(int,sys.stdin.readline().strip().split()))


def wood(woods, n):
    maxi = max(woods)
    old_mid =0
    li = list(range(1,maxi))
    def binary_search(left:int, right:int,target):
        nonlocal maxi
        nonlocal old_mid
        total = 0
        if left>right:
            return old_mid
        mid = li[(left+right)//2]
        for wood in woods:
            total += wood-maxi+mid if wood-maxi+mid>0 else 0
        if total ==target:
            return maxi-mid
        elif total>target:
            old_mid = maxi-mid
            return binary_search(left,(left+right)//2-1,target)
        else:
            return binary_search((left+right)//2+1,right,target)
    return binary_search(0,maxi-2,n)

print(wood(li,b))