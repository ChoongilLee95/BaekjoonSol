import sys


num_city  = int(sys.stdin.readline().strip())
num_bus = int(sys.stdin.readline().strip())

rute = [[] for _ in range(num_city+1)]
for _ in range(num_bus):
    a1,a2,cost = map(int,sys.stdin.readline().strip().split())
    rute[a1].append([a2,cost])
start,end = map(int,sys.stdin.readline().strip().split())
visited = [False for _ in range(num_city+1)]
def dfs(start,end):
    if start == end:
        return 0
    cost_li = []
    for i in rute[start]:
        if not visited[i[0]]:
            visited[i[0]] = True
            a = dfs(i[0],end)
            if a != 'n':
                cost_li.append(i[1]+a)
            visited[i[0]] = False
    if cost_li:
        return min(cost_li)
    else:
        return 'n'

print(dfs(start,end))