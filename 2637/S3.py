import sys
from collections import deque
input =sys.stdin.readline
target = int(input())
num_rel = int(input())


# bfs풀이, dp, 타뷸레이션

# 타뷸레이션 dp
dp = [[0]*(target+1) for _ in range(target+1)]


# 하위노드 정보 안에 상위노드 저장
# 여기서 일반적인 bottom-up과 다른점
# 일반적인 점화식은 상위 노드에서 하위노드를 호출한다
# 하지만 위상정렬 bottom-up은 끝단의 하위노드가 상위노드를 호출하며 수정한다.
# 즉 순서를 모르기 때문에 이렇게 한다.
vtx_connected = [[] for _ in range(target+1)]

# in_degree : done여부를 알 수 있고 done 즉 본인의 작업이 끝나면 상위에 작업을 시작한다.
# 원래 dp라면 dq를 조회함으로써 작업의 유무를 판단 가능하지만, 이문제는 그게 안된다.
# indegree 를 순회하며 시작점들을 작업 que에 추가하고 해당 시작점을 jeryo에 추가한다.
in_degree = [0]*(target+1)

# 제료인지 판단하는 리스트, 제료라면 상위노드를 호출할때 in_degree만 조작한다.
# 아니라면 상위노드에 자신의 dp요소를 더해준다.
jeryo = [True]*(target+1)


for _ in range(num_rel):
    making,maker,num = map(int,input().split())
    vtx_connected[maker].append(making)
    # 이렇게 하면 재료 즉 끝단만 True
    dp[making][maker] = num
    in_degree[making] +=1
    jeryo[making] = False

que = deque()
def bfs(n):
    que.append(n)
    while que:
        now = que.popleft()
        for next in vtx_connected[now]:
            if in_degree[next]==0:
                continue
            in_degree[next]-=1
            if not jeryo[now]:
                for now_dp in range(1,target+1):
                    dp[next][now_dp] += dp[next][now]*dp[now][now_dp]
                dp[next][now] = 0
            if in_degree[next]:
                continue
            que.append(next)
for i in range(1,target+1):
    if jeryo[i]:
        bfs(i)
for i in range(1,target+1):
    if dp[target][i]:
        print(i,dp[target][i])

