import sys
sys.setrecursionlimit(10**6)

num_vtx  = int(sys.stdin.readline().strip())
vtx = [[] for _ in range(num_vtx+1)]
for _ in range(num_vtx-1):
    a1, a2 = map(int, sys.stdin.readline().strip().split())
    vtx[a1].append(a2)
    vtx[a2].append(a1)
ans_dict = dict()
visited = [False for _ in range(num_vtx+1)]
def dfs(n,parent):
    ans_dict[n] = parent
    visited[n] = True
    for i in vtx[n]:
        if not visited[i]:
            dfs(i,n)
dfs(1,0)
for i in range(2,num_vtx+1):
    print(ans_dict[i])
