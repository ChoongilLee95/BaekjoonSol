import sys
from collections import deque
input = sys.stdin.readline

num_col,num_row = map(int,input().strip().split())

graph = [list(input().strip()) for _ in range(num_col)]

water_que = []

for col in range(num_col):
    for row in range(num_row):
        if graph[col][row] == '*':
            water_que.append((col,row))
            graph[col][row] = 'X'
            continue
        if graph[col][row] == 'D':
            end = (col,row)
            continue
        if graph[col][row] == 'S':
            start = (col,row)
            graph[col][row] = 'X'
            continue
col_move = [0,0,-1,1]
row_move = [1,-1,0,0]
run_que =[]
run_que.append((0,start[0],start[1]))
def dochi_move():
    global run_que
    new = []
    while run_que:
        run, col,row = run_que.pop()
        for i in range(4):
            n_c = col + col_move[i]
            if n_c<0 or n_c > num_col-1:
                continue
            n_r = row + row_move[i]
            if n_r <0 or n_r > num_row-1:
                continue
            if graph[n_c][n_r] == 'D':
                return run +1
            if graph[n_c][n_r] =='.':
                new.append((run+1,n_c,n_r))
                graph[n_c][n_r] = 'X'
    run_que = new
    return 0
def water_move():
    global water_que
    new = []
    for col,row in water_que:
        for i in range(4):
            n_c = col + col_move[i]
            if n_c<0 or n_c > num_col-1:
                continue
            n_r = row + row_move[i]
            if n_r <0 or n_r > num_row-1:
                continue
            if graph[n_c][n_r]=='.':
                new.append((n_c,n_r))
                graph[n_c][n_r] = 'X'
    water_que = new
def bfs():
    while True:
        # for i in range(num_col):
        #     print(graph[i])
        # print(0)
        water_move()
        a = dochi_move()
        if a:
            return a
        if not run_que:
            return 'KAKTUS'
print(bfs())