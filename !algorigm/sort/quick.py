from typing import MutableSequence

a = [16, 33, 41, 22, 5, 3, 6, 3, 7, 7, 9, 11, 23]

## pivat 이해

def partition(a : MutableSequence) ->None:
    n = len(a)
    pl = 0
    pr = n-1
    pivot = a[n//2]
    while pl<=pr:
        while a[pl] < pivot:
            pl+=1
        while a[pr] > pivot:
            pr -=1
        if pl<=pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl +=1
            pr -=1
    print(f'피벗 : {pivot}')

    print('피벗 이하 그룹')
    print(a[0:pl]) ## 피벗 이하 그룹 0 ~ pl-1
    print('피벗과 같은 그룹')
    if pl > pr+1: ## 이하 그룹과 이상 그룹의 교집합
        print(a[pr+1:pl])
    print('피벗 이상 그룹')
    print(a[pr+1:n]) ## 피벗 이상 그룹 pr+1 ~ n-1
## 테스트
# partition(a) # 단순 피벗기준 파티션
# print(a)

def q_sort(a:MutableSequence, left:int,right:int) ->None:
    pl = left
    pr = right
    pivot = a[(left+right)//2]
    while pl <=pr:
        while a[pl] < pivot:
            pl+=1
        while a[pr] > pivot:
            pr -= 1
        if pl<=pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl+=1
            pr-=1
    if left<pr:
        q_sort(a,left,pr)
    if pl<right:
        q_sort(a,pl,right)

def quick_sort(a:MutableSequence) ->None:
    q_sort(a,0,len(a)-1)
## 테스트
# quick_sort(a) # pivot 중심으로 고정한 퀵소트
# print(a)

## 비 재귀적인 퀵 정렬

from stack import Stack

def q_sort_noRe(a:MutableSequence, left:int, right:int) -> None:
    call_stack = Stack() # 스택 생성 log n 보다 작게
    call_stack.push((left, right))

    while not call_stack.isEmpty(): # 스택의 성분이 0일떄 멈춤
        pl, pr = left, right = call_stack.pop()
        pivot = a[(left + right) // 2]

        while pl <= pr:  # 퀵 정렬
            while a[pl] < pivot:
                pl+=1
            while a[pr] < pivot:
                pr-=1
            if pl <=pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl+=1
                pr-=1
        if left < pr:
            call_stack.push((left,pr)) # 재귀함수를 호출하는 부분, 스택에 추가
        if pl < right:
            call_stack.push((pl,right))
def quick_sort_noRe(a):
    left = 0
    right = len(a)-1
    q_sort_noRe(a,left,right)
## 테스트
# quick_sort_noRe(a) # pivot 중심으로 고정한 재귀없는 퀵소트(스택)
# print(a)

## 피벗을 다르게 설정하기

def q_sort_pivot(a:MutableSequence, left:int,right:int) ->None:
    for i in [left,(left+right)//2,right]: # 세개 뽑아서 정렬
        j = i
        tmp = a[i]
        while j>0 and a[j-1]>tmp:
            a[j] = a[j-1]
            j-=1
        a[j] = tmp
    pl = left+1
    pr = right-2
    pivot = a[(left+right)//2]
    a[(left+right)//2] , a[right-1] =a[right-1], a[(left+right)//2]
    while pl <=pr:
        while a[pl] < pivot:
            pl+=1
        while a[pr] > pivot:
            pr -= 1
        if pl<=pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl+=1
            pr-=1
    if left<pr:
        q_sort_pivot(a,left,pr)
    if pl<right:
        q_sort_pivot(a,pl,right)
def quick_sort_pivot(a:MutableSequence) ->None:
    q_sort_pivot(a,0,len(a)-1)
## 테스트
# quick_sort_pivot(a) # pivit을 계속 바꾸는 퀵소트
# print(a)

## 피벗 다르게 설정, 길이가 9보다 작다면 삽입정렬
def q_sort_final(a:MutableSequence,left:int, right:int) -> None:
    if right-left <8:
        insertion_sort(a,left, right)
    else:
        for i in [left,(left+right)//2,right]: # 세개 뽑아서 정렬
            j = i
            tmp = a[i]
            while j>0 and a[j-1]>tmp:
                a[j] = a[j-1]
                j-=1
            a[j] = tmp
        pl = left+1
        pr = right-2
        pivot = a[(left+right)//2]
        a[(left+right)//2] , a[right-1] =a[right-1], a[(left+right)//2]
        while pl <=pr:
            while a[pl] < pivot:
                pl+=1
            while a[pr] > pivot:
                pr -= 1
            if pl<=pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl+=1
                pr-=1
        if left<pr:
            q_sort_final(a,left,pr)
        if pl<right:
            q_sort_final(a,pl,right)
def quick_sort_final(a:MutableSequence):
    q_sort_final(a,0,len(a)-1)
## 길이가 9 미만인  경우를 위한 단순삽입 정렬
def insertion_sort(a:MutableSequence,left:int,right:int):
    for i in range(left+1,right+1):
        j = i
        tmp = a[i]
        while j>left and a[j-1]>tmp:
            a[j] = a[j-1]
            j-=1
        a[j] = tmp

## 테스트
# quick_sort_final(a)
# print(a)

## 정글 테스트용 (재귀과정 확인)

# def q_sort_test(a:MutableSequence, left:int,right:int,node:int) ->None:
#     pl = left
#     pr = right
#     pivot = a[(left+right)//2]
#     while pl <=pr:
#         while a[pl] < pivot:
#             pl+=1
#         while a[pr] > pivot:
#             pr -= 1
#         if pl<=pr:
#             a[pl], a[pr] = a[pr], a[pl]
#             pl+=1
#             pr-=1
#     print(f'left: {left} right : {right} 정렬후 : {a} {node}')
#     if left<pr:
#         new_node=node+'->왼쪽'
#         q_sort_test(a,left,pr,new_node)
#     if pl<right:
#         new_node=node+'->오른쪽'
#         q_sort_test(a,pl,right,new_node)
# def quick_sort_test(a:MutableSequence) ->None:
#     q_sort_test(a,0,len(a)-1,'시작!')

# b = [3, 1, 2,5,3,1]
# print(b)
# quick_sort_test(b)
