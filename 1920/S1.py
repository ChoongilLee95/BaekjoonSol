from typing import MutableSequence
from collections import defaultdict

### 딕셔너리?
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

import sys

input_num  = int(sys.stdin.readline().strip())
input_num_list = list(map(int, sys.stdin.readline().strip().split()))

num_dict = defaultdict(int)

for i in input_num_list:
    num_dict[i] = 1

new_num = int(sys.stdin.readline().strip())
new_num_list =list(map(int, sys.stdin.readline().strip().split()))

for i in new_num_list:
    if num_dict[i]:
        print(1)
    else:
        print(0)

