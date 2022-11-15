import sys
from collections import deque

# 메모리 초과 가능성 : que, 
num_city  = int(sys.stdin.readline().strip())
num_bus = int(sys.stdin.readline().strip())

rute = [[] for _ in range(num_city+1)]
for _ in range(num_bus):
    a1,a2,cost = map(int,sys.stdin.readline().strip().split())
    rute[a1].append([a2,cost])
start,end = map(int,sys.stdin.readline().strip().split())
que = deque()
short = [0]*(num_city+1)
def bfs(start, end):
    answer = 0
    for i in rute[start]:
        short[i[0]] = i[1]
        que.append(i)
    while que:
        now = que.popleft()
        total_cost = now[1]
        if now[0] == end:
            if answer > total_cost or answer==0:
                answer = total_cost
        elif total_cost<=short[now[0]]:
            for i in rute[now[0]]:
                if short[i[0]]==0 or short[i[0]] > i[1]+total_cost:
                    short[i[0]] =i[1]+total_cost
                    que.append([i[0],i[1]+total_cost])
    return answer
print(bfs(start,end))