from itertools import combinations

import sys

num_num,target  = map(int, sys.stdin.readline().strip().split())


num_list = list(map(int, sys.stdin.readline().strip().split()))

sum_1 = sum(num_list)

# i 빼는 수의 개수
# j 뺴는 조합
ans = 0
target = sum_1-target
for i in range(0,len(num_list)):
    for j in list(combinations(num_list,i)):
        if sum(j)==target:
            ans +=1

print(ans)
