import sys

def dfs(n,ans):
    is_infected[n] = True
    for i in vtx[n]:
        if not is_infected[i]:
            ans = dfs(i,ans+1)
    return ans

num_com  = int(sys.stdin.readline().strip())
num_edge = int(sys.stdin.readline().strip())

vtx = [[] for _ in range(num_com+1)]
is_infected = [False for _ in range(num_com+1)]
for _ in range(num_edge):
    a1, a2 = map(int, sys.stdin.readline().strip().split())
    vtx[a1].append(a2)
    vtx[a2].append(a1)

print(dfs(1,0))

