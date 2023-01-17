
import sys

input = sys.stdin.readline
tc = int(input())
ans = 0
building_left = []
building_left.append(int(input()))
num_building_left = 1
for i in range(tc-1):
    new = int(input())
    while num_building_left !=0 and building_left[-1] <=new:
        building_left.pop()
        num_building_left-=1
    ans += num_building_left
    building_left.append(new)
    num_building_left+=1
print(ans)

