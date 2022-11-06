import sys
import heapq


def binary_search(li,left:int, right:int,target):
    if left>right:
        return 0
    mid = (left+right)//2
    if li[mid] ==target:
        return 1
    elif li[mid]<target:
        return binary_search(li,mid+1,right,target)
    else:
        return binary_search(li,left,mid-1,target)

num_num  = int(sys.stdin.readline().strip())
nums = map(int, sys.stdin.readline().strip().split())
pos_heap = []
neg_heap = []
long = []
for i in nums:
    if i <0:
        heapq.heappush(neg_heap,-i)
    else:
        heapq.heappush(pos_heap,i)

len_p = len(pos_heap)
len_n = len(neg_heap)
breaker = 0
list_target = []
list_ans = []
if len_p>1:
    list_target.append(pos_heap[1]+pos_heap[0])
    list_ans.append([pos_heap[0],pos_heap[1]])
if len_n>1:
    list_target.append(neg_heap[1]+neg_heap[0])
    list_ans.append([-neg_heap[1],-neg_heap[0]])
if len_p>0 and len_n>0:
    list_ans.append([-neg_heap[0],pos_heap[0]])
    list_target.append(abs(pos_heap[0]-neg_heap[0]))
ans = list_ans.pop()
target = list_target.pop()
for i in range(len(list_ans)):
    if target > list_target[i]:
        ans = list_ans[i]
        target = list_target[i]

if target ==0:
    print(ans[0],ans[1])
else:
    if len_p<len_n:
        short = pos_heap
        for i in range(len_n):
            long.append(heapq.heappop(neg_heap))
        pointer = 1
    else:
        pointer =-1
        short = neg_heap
        for i in range(len_p):
            long.append(heapq.heappop(pos_heap))

    for num in short:
        for j in range(target):
            if binary_search(long,0,len(long)-1,num-j):
                ans = [(-num+j)*pointer,num*pointer]
                if j !=0:
                    target=j
                    break
                else:
                    breaker = 1
                    break
            if binary_search(long,0,len(long)-1,num+j):
                ans = [(-num-j)*pointer,num*pointer]
                if j !=0:
                    target=j
                    break
                else:
                    breaker = 1
                    break
        if breaker==1:
            break
    if ans[0]<ans[1]:
        print(ans[0],ans[1])
    else:
        print(ans[1],ans[0])

