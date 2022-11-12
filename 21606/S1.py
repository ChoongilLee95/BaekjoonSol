import sys
num_vtx  = int(sys.stdin.readline().strip())

inOut = '0'+sys.stdin.readline().strip()
def dfs(n,ans):
    if inOut[n] == '1':
        return 1
    else:
        for i in vtx[n]:
            if not visited[i]:
                visited[i] = True
                ans += dfs(i,ans)
                visited[i] = False
        return ans

vtx = [[] for _ in range(num_vtx+1)]
# 2 불가 1 가능 0 모름
visited = [False for _ in range(num_vtx+1)]
answer = 0
for _ in range(num_vtx-1):
    a1, a2 = map(int,sys.stdin.readline().strip().split())
    vtx[a1].append(a2)
    vtx[a2].append(a1)
for i in range(num_vtx+1):
    if inOut[i] =='1':
        visited[i] =True
        for j in vtx[i]:
            answer += dfs(j,0)
        visited[i] = False
print(answer)

# posibles = defaultdict(int)
# def start(a1, a2):
#     a = posibles[f'{a2},{a1}']
#     if a==2:
#         return 2
#     elif a==1:
#         return 1
#     else:
        

