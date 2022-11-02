from typing import MutableSequence

## 단순 삽입정렬
## 정렬되지 않은 원소를 정렬된 영역에 삽입

def insertion_sort(a:MutableSequence):
    n = len(a)
    for i in range(1,n):
        j = i
        tmp = a[i]
        while j>0 and a[j-1]>tmp:
            a[j] = a[j-1]
            j-=1
        a[j] = tmp
    return a
a = [16, 33, 41, 22, 5, 3, 6, 3, 7, 7, 9, 11, 23]
insertion_sort(a)
print(a)