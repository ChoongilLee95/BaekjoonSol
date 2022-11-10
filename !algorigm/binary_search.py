from typing import MutableSequence
## 기본형
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
## 해당 수가 없다면 해당수 앞뒤
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
## 해당 수가 없다면 해당 수 보다 큰 첫번째 애의 인덱스 그런애가 없다면 -1
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
        return -1
    else:
        return left
a = binary_search([1,2,3,4,5,6,7,8,9,10],0,11,9)
print(a)

