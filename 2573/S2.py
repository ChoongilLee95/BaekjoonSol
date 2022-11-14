# 녹은애 기준으로 bfs
import sys

# 안녹은애 기준으로 bfs
sys.setrecursionlimit(10**6)
input  = sys.stdin.readline

num_col, num_row = map(int, input().strip().split())

way_x = [0, 1, 0, -1]
way_y = [1, 0, -1, 0]

ice = []

for _ in range(num_col):
    ice.append(list(map(int,input().strip().split())))

visited = [[False]*(num_row) for _ in range(num_col)]

def dfs(col,row):
    ## 방문 했으면 멈춤
    if visited[col][row]:
        return
    else:
        # 방문 처리
        visited[col][row] = True
        for i in range(4):
            ## 물이라면 dfs 빙산이라면 -1
            if 0<=col+way_x[i]<num_col and 0<=row+way_y[i]<num_row:
                if ice[col+way_x[i]][row+way_y[i]]<1:
                    dfs(col+way_x[i],row+way_y[i])
                else:
                    ice[col+way_x[i]][row+way_y[i]] -= 1
def check_dfs(col,row):
    # 방문 처리
    visited[col][row] = True
    for i in range(4):
        ## 안가본 빙산이면 가서 방문체크
        if ice[col+way_x[i]][row+way_y[i]]>0 and not visited[col+way_x[i]][row+way_y[i]]:
            check_dfs(col+way_x[i],row+way_y[i])
ans = 0
while True:
    ans +=1
    checker = 0
    for col in range(num_col):
        for row in range(num_row):
            if ice[col][row]>0 and not visited[col][row]:
                checker +=1
                if checker == 2:
                    break
                else:
                    check_dfs(col,row)
        if checker ==2:
            break
    if checker==2:
        ans-=1
        break
    elif checker == 0:
        ans = 0
        break
    for col in range(num_col):
        for row in range(num_row):
            if not visited[col][row] and ice[col][row] <1:
                dfs(col,row)
    visited = [[False]*(num_row) for _ in range(num_col)]
print(ans)
