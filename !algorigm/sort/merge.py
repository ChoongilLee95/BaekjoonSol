from tkinter import N, SE
from typing import MutableSequence, Sequence

## 정렬된 두 배열을 병합 하는 함수
def merge_sorted_list(a:Sequence, b:Sequence,c:MutableSequence):
    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a),len(b),len(c)
    while pa<na and pb<nb:
        if a[pa] <b[pb]:
            c[pc]=a[pa]
            pa+=1
        else:
            c[pc]=b[pb]
            pb+=1
        pc +=1
    while pa < na:
        c[pc] = a[pa]
        pc+=1
        pa+=1
    while pb < nb:
        c[pc] = a[pb]
        pc+=1
        pb+=1

# 병합 함수 테스트

# a = [1, 2, 6, 10,15,25]
# b = [4,5,11,13,17,18]
# c = [0,0,0,0,0,0,0,0,0,0,0,0]
# merge_sorted_list(a,b,c)
# print(c)

## 병합 정렬 
def merge_sort(a:MutableSequence):
    def _merge_sort(a:MutableSequence, left:int, right:int):
        if left < right:
            center = (left+right)//2
            _merge_sort(a,left,center)
            _merge_sort(a,center+1,right)
            buff_putting=buff_pulling=0
            front_pointer = a_pointer =left
            while front_pointer<center:
                buff[buff_putting]  = a[front_pointer]
                front_pointer +=1
                buff_putting +=1
            while front_pointer < right and buff_pulling<buff_putting:
                if buff[buff_pulling] <= a[front_pointer]:
                    a[a_pointer] = buff[buff_pulling]
                    buff_pulling +=1
                else:
                    a[a_pointer] = a[front_pointer]
                    front_pointer+=1
                a_pointer+=1
            while buff_pulling<buff_putting:
                a[a_pointer]=buff[buff_pulling]
                a_pointer+=1
                buff_pulling +=1
    n = len(a)
    buff = [None]*n
    _merge_sort(a,0,n-1)
    del buff
## 병합정렬 테스트

# a = [1, 2, 6, 10,15,25,4,5,11,13,17,18]
# merge_sort(a)
# print(a)
