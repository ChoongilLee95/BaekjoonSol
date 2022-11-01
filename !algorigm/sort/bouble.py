
from typing import MutableSequence

## 기본 버블 정렬 프로그램

def bouble_basic(a:MutableSequence) -> None:
    n = len(a)
    for i in range(n-1): # n-1번 시행
        for j in range(n-1,i,-1): # n-1부터 i까지(정렬끝난부분 전까지)
            if a[j]<a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]


## 버블 개선 1 : 한 패스 안에 교환 여부 확인

def bouble_fixed_1(a:MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        exchange = 0  # 한 패스 안에 교환 여부
        for j in range(n-1,i,-1):
            if a[j]<a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                exchange +=1
        if exchange==0: # 전 패스에서 교환이 없었다면 더 할 필요 없다
            break

## 버블 개선 2 : pass중 교환이 마지막으로 일어나는 영역 확인


def bouble_fixed_2(a:MutableSequence) -> None:
    n = len(a)
    last = n-1  # 한 패스 안에 교환 여부
    for i in range(n-1):
        for j in range(last,i,-1):
            if a[j]<a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                last = j
        