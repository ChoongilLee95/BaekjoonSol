import sys
from collections import deque

def bfs(col,row):
    level = 1
    que.append([col,row,level])
    done = 0
    while que:
        now = que.popleft()
        level = now[2]
        level+=1
        for i in range(4):
            if now[0]+y[i]==N-1 and now[1]+x[i]==M-1:
                done = 1
                break
            elif -1<now[0]+y[i]<N and -1<now[1]+x[i]<M and Matrix[now[0]+y[i]][now[1]+x[i]] == '1':
                Matrix[now[0]+y[i]][now[1]+x[i]] =0
                que.append([now[0]+y[i],now[1]+x[i],level])
        if done:
            break
    return level

N,M  = map(int,sys.stdin.readline().strip().split())

Matrix = []

for _ in range(N):
    Matrix.append(list(sys.stdin.readline().strip()))

que = deque()
x = [0,1,0,-1]
y = [1,0,-1,0]

print(bfs(0,0))
