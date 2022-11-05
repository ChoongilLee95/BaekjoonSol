import sys
import heapq
from collections import defaultdict
num_num  = int(sys.stdin.readline().strip())
nums = map(int, sys.stdin.readline().strip().split())
dict_nums = defaultdict(int)
pos_heap = []
neg_heap = []
for i in nums:
    if i <0:
        heapq.heappush(neg_heap,-i)
        dict_nums[i] = 1
    else:
        heapq.heappush(pos_heap,i)
        dict_nums[i] = 1
len_p = len(pos_heap)
len_n = len(neg_heap)
breaker = 0
list_target = []
list_ans = []
if len_p>1:
    if len_p>2:
        if pos_heap[1]>pos_heap[2]:
            pos_heap[1],pos_heap[2] =pos_heap[2],pos_heap[1]
    list_target.append(pos_heap[1]+pos_heap[0])
    list_ans.append([pos_heap[0],pos_heap[1]])
if len_n>1:
    if len_n>2:
        if neg_heap[1]>neg_heap[2]:
            neg_heap[1],neg_heap[2] =neg_heap[2],neg_heap[1]
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
    pointer =-1
    short = neg_heap
    long = pos_heap
    if len_p<len_n:
        short = pos_heap
        long = neg_heap
        pointer = 1
    for num in short:
        for j in range(target):
            if dict_nums[-(num-j)*pointer]==1:
                ans = [(-num+j)*pointer,num*pointer]
                if j !=0:
                    target=j
                    break
                else:
                    breaker = 1
                    break
            if dict_nums[-(num+j)*pointer]==1:
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

