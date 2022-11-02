from typing import MutableSequence

## 단순 선택 정렬
## 정렬되지 않은 영역의 첫번째 원소를 정렬되지 않은 영역의 원소와 비교하며 결정
def selection_sort(a:MutableSequence):
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1,n-1):
            if a[j]<a[min]:
                min = j
        a[i], a[min] = a[min],a[i]
    return a