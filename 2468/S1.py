from copy import deepcopy
import sys

sys.setrecursionlimit(10**6)

def find_touched(r, c):
    new_buildings[r][c] *=0
    if -1<r-1:
        if new_buildings[r-1][c]>0:
            find_touched(r-1,c)
    if r+1<num:
        if new_buildings[r+1][c]>0:
            find_touched(r+1,c)
    if c-1>-1:
        if new_buildings[r][c-1]>0:
            find_touched(r,c-1)
    if c+1<num:
        if new_buildings[r][c+1]>0:
            find_touched(r,c+1)


num  = int(sys.stdin.readline().strip())
nums = range(num)

buildings = []
height = set()
for i in range(num):
    new_row = list(map(int,sys.stdin.readline().strip().split()))
    height.update(new_row)
    buildings.append(new_row)
ans = 1
for i in list(height):
    new_buildings = deepcopy(buildings)
    new_ans = 0
    left = num**2
    for r in nums:
        for c in nums:
            if new_buildings[r][c] -i <1:
                new_buildings[r][c] =0
                left-=1
    if left > ans:
        for r in nums:
            for c in nums:
                if new_buildings[r][c]<1:
                    continue
                else:
                    new_ans +=1
                    find_touched(r,c)
        if new_ans>ans:
            ans = new_ans


print(ans)
