import sys
sys.setrecursionlimit(10**6)
input  = sys.stdin.readline

N , M = map(int,input().strip().split())
target = N//2

rel_small = [[] for _ in range(N+1)]
rel_big = [[] for _ in range(N+1)]
for _ in range(M):
    new = list(map(int, input().strip().split()))
    rel_big[new[1]].append(new[0])
    rel_small[new[0]].append(new[1])

def dfs(n,arr):
    global len_n
    for i in arr[n]:
        if not visited[i]:
            visited[i] = True
            len_n+=1
            dfs(i,arr)
ans = 0
for i in range(1,N+1):
    visited = [False]*(N+1)
    len_n = 0
    dfs(i,rel_big)
    if len_n > target:
        ans +=1
    else:
        len_n = 0
        dfs(i,rel_small)
        if len_n > target:
            ans +=1
print(ans)

