import sys

sys.setrecursionlimit(10**6)
input  = sys.stdin.readline

num_col, num_row = map(int, input().strip().split())

before = []

for _ in range(num_col):
    before.append(list(map(int,input().strip().split())))

visited = [[False]*(num_row-1) for _ in range(num_col-1)]

way_x = [0, 1, 0, -1]
way_y = [1, 0, -1, 0]

def dfs(col,row):
    ## 방문 했으면 멈춤
    if visited[col-1][row-1]:
        return 0
    else:
        # 방문 처리
        visited[col-1][row-1] = True
        ans = 0
        for i in range(4):
            ## 0이 아니라면 dfs 0이라면 -1
            if before[col+way_x[i]][row+way_y[i]]>0:
                ans += dfs(col+way_x[i],row+way_y[i])
            else:
                ice[col][row] -= 1
        return 1 +ans
###  두가지 지표, 다 녹아 없어졌거나 답이 나왔거나
ans = 0
ice = [item[:] for item in before]
while True:
    left = 0
    ans +=1
    t_b = 0
    for col in range(1,num_col-1):
        for row in range(1,num_row-1):
            if (not visited[col-1][row-1]) and ice[col][row] >0:
                t_b +=1
                if t_b == 2:
                    break
                else:
                    left += dfs(col,row)
        if t_b ==2:
            break
    print(left,ice)
    if t_b == 0:
        ans =0
        break
    elif t_b == 2:
        ans -=1
        break
    elif left < 3:
        ans = 0
        break
    else:
        before = [item[:] for item in ice]
        visited = [[False]*(num_row-1) for _ in range(num_col-1)]
print(ans)




