import sys
from collections import deque

num_row,num_col,num_flour  = map(int,sys.stdin.readline().strip().split())
# flour, col, row
graph = []
que = deque()


for f in range(num_flour):
    flour = []
    for c in range(num_col):
        flour.append(list(map(int, sys.stdin.readline().strip().split())))
        for i in range(num_row):
            if flour[c][i] == 1:
                que.append((0,f,c,i))
    graph.append(flour)

f_m = [0,0,1,-1,0,0]
c_m = [1,-1,0,0,0,0]
r_m = [0,0,0,0,1,-1]

def bfs():
    max_dis = 0
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
            if graph[next_f][next_c][next_r]==0:
                graph[next_f][next_c][next_r] = 1
                que.append([dis+1,next_f,next_c,next_r])
                max_dis = dis+1 if dis+1 > max_dis else max_dis
    return max_dis
def start(max_dis):
    for f in range(num_flour):
        for c in range(num_col):
            for r in range(num_row):
                if graph[f][c][r]==0:
                    return -1
    return max_dis
a = bfs()
print(start(a))