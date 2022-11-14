import sys
from collections import deque
import heapq

num_city,num_road,dis,start  = map(int,sys.stdin.readline().strip().split())
link = [[] for _ in range(num_city+1)]
que = deque()

for _ in range(num_road):
    a1,a2 = map(int,sys.stdin.readline().strip().split())
    link[a1].append(a2)
visited = [False for _ in range(num_city+1)]
def bfs(x):
    answer = []
    level = 0
    que.append([x,level])
    visited[x] = True
    while que:
        new = que.popleft()
        level = new[1]
        if level < dis:
            for i in link[new[0]]:
                if not visited[i]:
                    visited[i] = True
                    que.append([i,level+1])
        else:
            heapq.heappush(answer, new[0])
    return answer
ans = bfs(start)
if ans:
    while ans:
        print(heapq.heappop(ans),end='\n')
else:
    print(-1)
