import sys
from collections import defaultdict,deque
def bfs(n):
    que_list.append(n)
    while que_list:
        k = que_list.popleft()
        if visited[k]==0:
            visited[k]=1
            answer.append(k)
            edge[k].sort()
            for next_edge in edge[k]:
                que_list.append(next_edge)
def dfs(n):
    if visited[n]==0:
        visited[n]=1
        answer.append(n)
        edge[n].sort()
        for next_edge in edge[n]:
            dfs(next_edge)
N,M,V  = map(int,sys.stdin.readline().strip().split())

visited = defaultdict(int)
edge = [[] for _ in range(N+1)]
answer = []


for _ in range(M):
    a1,a2  = map(int,sys.stdin.readline().strip().split())
    edge[a1].append(a2)
    edge[a2].append(a1)
dfs(V)
print(*answer)
answer = []
que_list =deque()
visited = defaultdict(int)

bfs(V)
print(*answer)
