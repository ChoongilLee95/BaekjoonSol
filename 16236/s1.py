import sys

from collections import deque


queue = deque()

N = int(input())


pool = []

m_c = [-1,0,0,1]
m_r = [0,-1,1,0]


for i in range(N):
    pool.append(list(map(int, input().strip().split())))
    for j in range(N):
        if pool[i][j] == 9:
            pos = (i,j)


def baby_shark(pos,shark_size):
    visited = [[0]*N for i in range(N)]
    pool[pos[0]][pos[1]] = 0
    moves = deque()
    time = 0
    moves.append((pos[0],pos[1],time))
    ans_pos = (N,N)
    stop_time= N*N
    is_found = False
    while moves:
        col, row, time= moves.popleft()
        if time >stop_time-1:
            break
        for i in range(4):
            new_c = col + m_c[i]
            new_r = row + m_r[i]
            if new_c<0 or new_c>=N or new_r<0 or new_r>=N or visited[new_c][new_r] or pool[new_c][new_r]>shark_size:
                continue
            if 0<pool[new_c][new_r] < shark_size:
                visited[new_c][new_r] = 1
                stop_time = time+1
                is_found = True
                if new_c < ans_pos[0] or (ans_pos[0]==new_c and new_r <ans_pos[1]):
                    ans_pos = (new_c,new_r)
                    continue
            # print(new_c,new_r, time+1)
            visited[new_c][new_r] = 1
            moves.append((new_c,new_r,time+1))
    if is_found:
        return ans_pos, stop_time
    return (0,0),0


def solve(pos):
    shark_size = 2
    food_to_up = 2
    sum_time = 0
    while 1:
        pos, time = baby_shark(pos,shark_size)
        # print(pos, time)
        if time == 0:
            break
        food_to_up-=1
        if food_to_up == 0:
            shark_size+=1
            food_to_up = shark_size
        sum_time += time
    return sum_time
print(solve(pos))

