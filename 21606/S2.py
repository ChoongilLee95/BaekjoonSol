import sys
num_vtx  = int(sys.stdin.readline().strip())

inOut = '0'+sys.stdin.readline().strip()
def dfs(a1):
    global answer
    if inOut[a1] == '1':
        answer +=1
    else:
        for i in vtx[a1]:
            if not visited[i]:
                visited[i] = True
                dfs(i)
                visited[i] = False


vtx = [[] for _ in range(num_vtx+1)]
visited = [False for _ in range(num_vtx+1)]
answer = 0
for _ in range(0,num_vtx-1):
    a1, a2 = map(int,sys.stdin.readline().strip().split())
    vtx[a1].append(a2)
    vtx[a2].append(a1)
for i in range(1,num_vtx+1):
    if inOut[i] =='1' and not visited[i]:
        visited[i] = True
        for j in vtx[i]:
            if not visited[j]:
                dfs(j)
print(answer*2)
