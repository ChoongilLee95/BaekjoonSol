import sys
sys.setrecursionlimit(10**6)
def dfs(n):
    visited[n] = True
    for i in edge[n]:
        if not visited[i]:
            dfs(i)

N,M = map(int, sys.stdin.readline().strip().split())

visited = [False for _ in range(N+1)]
edge = [[] for _ in range(N+1)]

for _ in range(M):
    a1,a2 = map(int, sys.stdin.readline().strip().split())
    edge[a1].append(a2)
    edge[a2].append(a1)

ans = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        ans +=1
print(ans)
