import sys
sys.setrecursionlimit(10**6)
num_vtx  = int(sys.stdin.readline().strip())

inOut = [0] + list(map(int, input().rstrip()))
def dfs(n):
    num = 0
    visited[n] = 1
    for i in vtx[n]:
        if inOut[i] == 1:
            num+=1
        else:
            if not visited[i]:
                num += dfs(i)
    return num

vtx = [[] for _ in range(num_vtx+1)]
visited = [0] * (num_vtx + 1)
answer = 0
for _ in range(num_vtx-1):
    a1, a2 = map(int,sys.stdin.readline().strip().split())
    vtx[a1].append(a2)
    vtx[a2].append(a1)

for i in range(1,num_vtx+1):
    if inOut[i] ==1:
        for j in vtx[i]:
            if inOut[j] == 1:
                answer += 1
    else:
        if not visited[i]:
            a = dfs(i)
            answer += a*(a-1)
print(answer)

# posibles = defaultdict(int)
# def start(a1, a2):
#     a = posibles[f'{a2},{a1}']
#     if a==2:
#         return 2
#     elif a==1:
#         return 1
#     else:
        

