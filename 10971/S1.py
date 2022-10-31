import sys
import itertools


num_city  = int(sys.stdin.readline().strip())


## 0출발 0도착 고정 -> 1부터
nPr = itertools.permutations(range(1,num_city),num_city-1)

list_city_move = list(nPr)


default_start = 0
expence = []
for i in range(num_city):
    new_ex = list(map(int, sys.stdin.readline().strip().split()))
    expence.append(new_ex)
list_total_ex = []
start = 0
for i in list_city_move:
    total_ex = 0
    start = 0
    unbreaked =1
    for j in i:
        if expence[start][j]==0:
            unbreaked = 0
            break
        total_ex += expence[start][j]
        start = j
    if unbreaked and expence[start][0]:
        list_total_ex.append(total_ex+expence[start][0])
print(min(list_total_ex))


