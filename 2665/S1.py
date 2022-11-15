from sys import maxsize
import sys,heapq
N = int(sys.stdin.readline().strip())
# 효율성은 index로 판단
visited = [[maxsize]*(N) for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))

move_col = [0,1,0,-1]
move_row = [1,0,-1,0]

def dijkstra(col,row):
    que = []
    que.append((0,col,row))
    visited[col][row] = 0
    while que:
        cost,col,row = heapq.heappop(que)
        if visited[col][row] <cost:
            continue
        for i in range(4):
            n_cost = cost
            n_col = col+move_col[i]
            if n_col<0 or n_col>N-1:
                continue
            n_row = row+move_row[i]
            if n_row<0 or n_row>N-1:
                continue
            if graph[n_col][n_row] == '0':
                n_cost += 1
            if visited[n_col][n_row] >n_cost:
                visited[n_col][n_row] = n_cost
                heapq.heappush(que,(n_cost,n_col,n_row))
dijkstra(0,0)
print(visited[N-1][N-1])
