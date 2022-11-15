import sys
from collections import deque
input = sys.stdin.readline

num_col,num_row = map(int,input().strip().split())

graph = [list(input().strip()) for _ in range(num_col)]

water_que = deque()

for col in range(num_col):
    for row in range(num_row):
        if graph[col][row] == '*':
            water_que.append((0,col,row))
            graph[col][row] = 0
            continue
        if graph[col][row] == 'D':
            end = (col,row)
            continue
        if graph[col][row] == 'S':
            start = (col,row)
            graph[col][row] = '.'
            continue
col_move = [0,0,-1,1]
row_move = [1,-1,0,0]
def bfs_water():
    while water_que:
        left,col,row = water_que.popleft()
        for i in range(4):
            n_c = col + col_move[i]
            if n_c<0 or n_c > num_col-1:
                continue
            n_r = row + row_move[i]
            if n_r <0 or n_r > num_row-1:
                continue
            if graph[n_c][n_r] == 'D':
                max_run = left
            if graph[n_c][n_r]=='.':
                water_que.append((left+1,n_c,n_r))
                graph[n_c][n_r] = left+1
    return max_run
def bfs_run(max_run):
    run_que = deque()
    run_que.append((0,start[0],start[1]))
    while run_que:
        run, col,row = run_que.popleft()
        for i in range(4):
            n_c = col + col_move[i]
            if n_c<0 or n_c > num_col-1:
                continue
            n_r = row + row_move[i]
            if n_r <0 or n_r > num_row-1:
                continue
            if graph[n_c][n_r] == 'D':
                return run +1
            if graph[n_c][n_r] !='X' and graph[n_c][n_r] > run+1:
                run_que.append((run+1,n_c,n_r))
                graph[col][row] = 'X'
    return 'KAKTUS'
max_run = bfs_water()
print(bfs_run(max_run))