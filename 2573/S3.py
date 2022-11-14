import sys

# 안녹은애 기준으로 bfs
sys.setrecursionlimit(10**4)
input  = sys.stdin.readline

num_col, num_row = map(int, input().strip().split())
ice = []

for _ in range(num_col):
    ice.append(list(map(int,input().strip().split())))

# 이전 작업을 진행한 횟수(이전 빙산)-이전 빠진 빙산의 수 = 다음 빙산의 수, 다음 작업이 된 횟수 
visited = [[False]*(num_row-1) for _ in range(num_col-1)]

way_x = [0, 1, 0, -1]
way_y = [1, 0, -1, 0]

def dfs(col,row):
    global to_zero
    global num_ices
    # 방문 처리
    num_ices +=1
    visited[col-1][row-1] = True
    for i in range(4):
        # 방문 안한 다음 애들 중에
        # 다음 애가 0이 아니라면 dfs 0이라면 -1
        if not visited[col+way_x[i]-1][row+way_y[i]-1]:
            if ice[col+way_x[i]][row+way_y[i]]>0:
                dfs(col+way_x[i],row+way_y[i])
            else:
                ice[col][row] -= 1
    if ice[col][row] < 1:
        to_zero +=1

to_zero = 0
num_ices = 0
breaker = 0
for col in range(1,num_col-1):
    for row in range(1,num_row-1):
        if not visited[col-1][row-1] and ice[col][row] >0:
            dfs(col,row)
            breaker = 1
            break
    if breaker:
        break
ex_ices = num_ices - to_zero
ans = 1
while breaker:
    visited = [[False]*(num_row-1) for _ in range(num_col-1)]
    checker = 0
    ans +=1
    to_zero = 0
    num_ices =0
    for col in range(1,num_col-1):
        for row in range(1,num_row-1):
            if not visited[col-1][row-1] and ice[col][row] >0:
                dfs(col,row)
                if ex_ices !=num_ices:
                    checker = 1
                    break
                else:
                    checker = 2
                    break
        if checker:
            break
    if checker==1:
        ans -=1
        break
    elif checker==0:
        ans = 0
        break
    else:
        ex_ices = num_ices - to_zero
print(ans)




