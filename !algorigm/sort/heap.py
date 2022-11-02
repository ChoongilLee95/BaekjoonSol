from typing import MutableSequence

a = [16, 33, 41, 22, 5, 3, 6, 3, 7, 7, 9, 11, 23]

## heap을 이용한 '오름차순 정렬' 아래 부분 지우면 최대 힙
def heap_sort(a:MutableSequence) ->None:
    ## 내부는 모르겠고 아무튼 맨 위에있는 애는 규칙에 맞는 힙
    ## 그래서 이걸 자식이 있는 모든 노드에 대해 아래쪽 노드부터 해야함
    def down_heap(a:MutableSequence,left:int,right:int) ->None:
        temp = a[left]
        parent = left
        while parent < (right+1)//2:
            cl = parent*2+1
            cr = parent*2+2
            # cl이 없으면 실행되지 않는다, 따라서 마지막 원소의 부모부터 실행한다.
            child = cr if cr<=right and a[cr] > a[cl] else cl
            if temp>=a[child]:
                break
            a[parent] =a[child]
            parent = child
        a[parent] = temp
    n = len(a)
    for i in range((n-1)//2,-1,-1): # 마지막 자식의 부모노드부터 쭉~ 힙화
        down_heap(a,i,n-1) # 해당 노드부터 자식 끝까지 데리고함

    ## 여기서부턴 힙구조인 a를 크기순으로 정렬 후 그거빼고 힙구조 다시 맞춤
    # 여기부터 없으면 그냥 최대 힙
    for i in range(n-1,0,-1):
        a[0],a[i] = a[i], a[0]
        down_heap(a,0,i-1)

## 힙을 이용한 정렬 테스트

# heap_sort(a)
# print(a)

## heapq 모듈을 사용하는 힙 정렬
import heapq
def heapq_sort(a:MutableSequence):
    heap = []
    for i in a:
        heapq.heappush(heap,i) # 해당 리스트에 힙으로 i원소 넣는다
    for i in range(len(a)):
        a[i] = heapq.heappop(heap) # 해당 리스트의 root를 빼고 heap화

# heapq_sort(a)
# print(a)