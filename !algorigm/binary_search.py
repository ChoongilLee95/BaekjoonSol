from typing import MutableSequence

def binary_search(li:MutableSequence,left:int, right:int,target):
    if left>right:
        return -1
    mid = (left+right)//2
    if li[mid] ==target:
        return mid
    elif li[mid]<target:
        return binary_search(li,mid+1,right,target)
    else:
        return binary_search(li,left,mid-1,target)

a = binary_search([1,2,3,4,5,6,7,8,9,10],0,11,9)
print(a)