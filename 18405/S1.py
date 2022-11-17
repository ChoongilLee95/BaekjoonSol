import sys
from collections import deque
input = sys.stdin.readline

num_col, max_vi = map(int, input().split())

n_status =[]

for _ in range(num_col):
    n_status.append(list(map(int, input().split())))

time, t_col, t_row = map(int, input().split())
t_row-=1
t_col-=1
que = []

m_c = [0,0,1,-1]
m_r = [1,-1,0,0]
for col in range(num_col):
    for row in range(num_col):
        vi = n_status[col][row]
        if vi==0:
            continue
        que.append((vi,col,row))
que.sort()
que = deque(que)
def bfs():
    stopper = len(que)
    done = 0
    while done < stopper:
        vi, n_c,n_r = que.popleft()
        for i in range(4):
            new_c = n_c + m_c[i]
            if new_c<0 or new_c>num_col-1:
                continue
            new_r = n_r + m_r[i]
            if new_r<0 or new_r>num_col-1:
                continue
            if new_r == t_row and new_c == t_col:
                return vi
            if n_status[new_c][new_r]!=0:
                continue
            n_status[new_c][new_r] = vi
            que.append((vi,new_c,new_r))
        done+=1
    return 0
a = 0
for i in range(time):
    if not que:
        break
    a = bfs()
    if a:
        print(a)
        break
if not a:
    print(0)

