import sys

input =sys.stdin.readline

target = int(input())

num_rel = int(input())

need = [[0]*(target+1) for _ in range(target+1)]

visited = [True]*(target+1)

for _ in range(num_rel):
    making,maker,num = map(int,input().split())
    need[making][maker]=num
    # 이렇게 하면 재료 즉 더 파고들어갈 일 없는 애들은만 True
    visited[making] = False

# visited 가 안된 n에 대하여 dfs
def f(n):
    for i in range(target-1,0,-1):
        if visited[i] or need[n][i]==0:
            continue
        for j in range(i-1,0,-1):
            need[n][j] += need[i][j]*need[n][i]
        need[n][i] = 0
f(target)
for i in range(1,target):
    if visited[i]:
        print(i,need[target][i])




