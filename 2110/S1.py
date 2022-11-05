import heapq
import sys
sys.setrecursionlimit(10**6)
num_num, target_c  = map(int, sys.stdin.readline().strip().split())
num_list = []
for _ in range(num_num):
    num =int(sys.stdin.readline().strip())
    heapq.heappush(num_list,num)
first = heapq.heappop(num_list)
sorted_list = []
for i in range(num_num-1):
    sorted_list.append(heapq.heappop(num_list))
old_mid = 1
def binary_search(left:int, right:int):
    global target_c
    global first
    global old_mid
    if left>right:
        return old_mid
    mid = (left+right)//2
    which_is = 0
    num_old = first
    c_num =1
    for j in sorted_list:
        if j >=mid+num_old:
            # print(f'mid, j: {mid},{j},{target_c}')
            c_num+=1
            num_old = j
            if c_num == target_c:
                # print(mid, j,right)
                which_is = 1
                break
    if which_is ==1:
        old_mid = mid
        return binary_search((left+right)//2+1,right)
    else:
        return binary_search(left,(left+right)//2-1)
print(binary_search(2,(sorted_list[-1]-first)//(target_c-1)))
