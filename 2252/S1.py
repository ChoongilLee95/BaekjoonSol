import sys
from collections import deque
input = sys.stdin.readline

# dfs로 위상정렬 구현

num_vtx ,num_node = map(int, input().split())
vtx = [[]for _ in range(num_vtx+1)]
for _ in range(num_node):
    a1,a2 = map(int,input().split())
    vtx[a1].append(a2)
visited = [False]*(num_vtx+1)
answer = deque()
# n은 vtx의 이름
def dfs(n):
    if not visited[n]:
        visited[n] = True
        for i in vtx[n]:
            dfs(i)
        answer.appendleft(n)

for i in range(1,num_vtx+1):
    dfs(i)
print(*answer)
