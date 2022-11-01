from typing import MutableSequence

## 단순 삽입정렬 

def insertion_sort(a:MutableSequence):
    n = len(a)
    for i in range(1,n):
        j = i
        tmp = a[i]
        while j>0 and a[j-i]>tmp:
            a[j] = a[j-1]
            j-=1
        a[j] = tmp