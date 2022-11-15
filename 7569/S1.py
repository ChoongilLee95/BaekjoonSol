import sys
from collections import deque

num_row,num_col,num_flour  = map(int,sys.stdin.readline().strip().split())
# flour, col, row
graph = []

for h in range(num_flour):
    flour = []
    for c in range(num_col):
        flour.append(list(map(int, sys.stdin.readline().strip().split())))
    graph.append(flour)
f_m = [0,0,1,-1,0,0]
c_m = [1,-1,0,0,0,0]
r_m = [0,0,0,0,1,-1]
def bfs(flour,col,row):
    visited = [[[0]*(num_row) for _ in range(num_col)] for i in range(num_flour)]
    que = deque()
    # level,f,c,r
    que.append([0,flour,col,row])
    while que:
        dis,flour,col,row = que.popleft()
        for i in range(6):
            next_f = flour + f_m[i]
            if next_f<0 or next_f > num_flour-1:
                continue
            next_c = col + c_m[i]
            if next_c<0 or next_c > num_col-1:
                continue
            next_r = row + r_m[i]
            if next_r <0 or next_r > num_row-1:
                continue
            if graph[next_f][next_c][next_r] == 1:
                return dis+1
            if not visited[next_f][next_c][next_r] and graph[next_f][next_c][next_r]==0:
                que.append([dis+1,next_f,next_c,next_r])
    return -1
def start():
    answer = 0
    for flour in range(num_flour):
        for col in range(num_col):
            for row in range(num_row):
                if graph[flour][col][row]!=0:
                    continue
                ans = bfs(flour,col,row)
                if ans == -1:
                    return -1
                else:
                    answer = ans if ans > answer else answer
    return answer
print(start())



