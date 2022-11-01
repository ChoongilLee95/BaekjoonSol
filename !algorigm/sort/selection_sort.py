from typing import MutableSequence

## 단순 선택 정렬

def selection_sort(a:MutableSequence):
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1,n-1):
            if a[j]<a[min]:
                min = j
        a[i], a[min] = a[min],a[i]