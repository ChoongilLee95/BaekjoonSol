import sys
from bisect import bisect_left
sys.setrecursionlimit(10**6)
def check(start_idx,end):
    checker = num_list[start_idx]
    if checker[1] == end:
        return 1
    else:
        next_idx = bisect_left(num_list,[checker[1],])
        if next_idx < n and num_list[next_idx][0] == checker[1]:
            return check(next_idx,end)
        else:
            return 0

n  = int(sys.stdin.readline().strip())
num_list = []
num_start = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    x1, x2 = a-b,a+b
    num_list.append([x1,x2])
    num_start.append(x1)
num_list.sort(key=lambda x: (x[0], -x[1]))
ans = 1+n
for i in range(n-1):
    if num_list[i][0] == num_list[i+1][0]:
        ans += check(i+1,num_list[i][1])
print(ans)