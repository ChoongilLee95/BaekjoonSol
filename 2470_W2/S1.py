import sys
import heapq
num_num  = int(sys.stdin.readline().strip())

nums = map(int, sys.stdin.readline().strip().split())

pos_heap = []
neg_heap = []
for i in nums:
    if i <0:
        heapq.heappush(neg_heap,-i)
    else:
        heapq.heappush(pos_heap,i)
len_p = len(pos_heap)
len_n = len(neg_heap)
breaker = 0
if len_p>2:
    ans1 = [pos_heap[0],pos_heap[1]] if pos_heap[1] < pos_heap[2] else [pos_heap[0],pos_heap[2]]
    a1 = pos_heap[1]+pos_heap[0] if pos_heap[1] < pos_heap[2] else pos_heap[2]+pos_heap[0]
    if len_n >2:
        ans2  = [-neg_heap[1],-neg_heap[0]] if neg_heap[1] < neg_heap[2] else [-neg_heap[2],-neg_heap[0]]
        a2 = neg_heap[1]+neg_heap[0] if neg_heap[1] < neg_heap[2] else neg_heap[2]+neg_heap[0]
        ans =ans1 if a1< a2 else ans2
        target = a1 if a1< a2 else a2
    elif len_n ==2:
        ans2 = [-neg_heap[1],-neg_heap[0]]
        a2 = neg_heap[1]+neg_heap[0]
        ans =ans1 if a1< a2 else ans2
        target = a1 if a1< a2 else a2
    else:
        ans = ans1
        target = a1
elif len_p==2:
    ans1 = [pos_heap[0],pos_heap[1]]
    a1 = pos_heap[1]-pos_heap[0]
    if len_n >2:
        ans2 = [-neg_heap[1],-neg_heap[0]] if neg_heap[1] < neg_heap[2] else [-neg_heap[2],-neg_heap[0]]
        a2 = neg_heap[1]+neg_heap[0] if neg_heap[1] < neg_heap[2] else neg_heap[2]+neg_heap[0]
        ans =ans1 if a1< a2 else ans2
        target = a1 if a1< a2 else a2
    elif len_n ==2:
        ans2 = [-neg_heap[1],-neg_heap[0]]
        a2 = neg_heap[1]+neg_heap[0]
        ans =ans1 if a1< a2 else ans2
        target = a1 if a1< a2 else a2
    else:
        ans = ans1
        target = a1
else:
    if len_n >2:
        ans = [-neg_heap[1],-neg_heap[0]] if neg_heap[1] < neg_heap[2] else [-neg_heap[2],-neg_heap[0]]
        target = neg_heap[1]+neg_heap[0] if neg_heap[1] < neg_heap[2] else neg_heap[2]+neg_heap[0]
    elif len_n ==2:
        ans = [-neg_heap[1],-neg_heap[0]]
        target = neg_heap[1]+neg_heap[0]
    else:
        ans =[-neg_heap[0],pos_heap[0]]
        target = pos_heap[0]-neg_heap[0]
if target ==0:
    print(ans[0],ans[1])
else:
    if len_p>len_n:
        for neg in neg_heap:
            for j in range(target):
                if neg-j in pos_heap:
                    ans = [-neg,neg-j]
                    if j !=0:
                        target=j
                        break
                    else:
                        breaker = 1
                        break
                if neg+j in pos_heap:
                    ans = [-neg,neg+j]
                    if j !=0:
                        target=j
                        break
                    else:
                        breaker = 1
                        break
            if breaker==1:
                break
    else:
        for pos in pos_heap:
            for j in range(target):
                if pos-j in neg_heap:
                    ans = [-pos+j,pos]
                    if j !=0:
                        target=j
                        break
                    else:
                        breaker = 1
                        break
                if pos+j in neg_heap:
                    ans = [-pos-j,pos]
                    if j !=0:
                        target=j
                        break
                    else:
                        breaker = 1
                        break
            if breaker==1:
                break
print(ans[0],ans[1])
