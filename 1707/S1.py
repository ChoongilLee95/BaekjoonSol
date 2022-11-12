import sys
sys.setrecursionlimit(10**6)
def dfs(n,side):
    if visited[n]:
        if which_side[n]==side:
            return False
        else:
            return True
    else:
        side = 1 if side == 2 else 2
        which_side[n] = side
        visited[n] = True
        for i in vtx[n]:
            if dfs(i,side):
                continue
            else:
                return False
        return True


num_tc  = int(sys.stdin.readline().strip())
for tc in range(num_tc):
    which_side = dict()
    num_vtx, num_edge = map(int,sys.stdin.readline().strip().split())
    vtx = [[] for _ in range(num_vtx+1)]
    visited = [False for _ in range(num_vtx+1)]
    for _ in range(num_edge):
        a1, a2 = map(int,sys.stdin.readline().strip().split())
        vtx[a1].append(a2)
        vtx[a2].append(a1)
    ans = 'YES'
    for i in range(1,num_vtx+1):
        if not visited[i]:
            if not dfs(i,1):
                ans = 'NO'
                break
    print(ans)

