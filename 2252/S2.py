import sys
from collections import deque
input = sys.stdin.readline

# bfs로 위상정렬 구현

num_vtx ,num_node = map(int, input().split())
vtx_connected = [[] for _ in range(num_vtx+1)]
vtx_left = [0]*(num_vtx+1)

for _ in range(num_node):
    a1,a2 = map(int,input().split())
    vtx_left[a2] +=1
    vtx_connected[a1].append(a2)

que = deque()
answer = []

# 시작점은 방문차수가 0인 애들이므로 미리 que에 넣어놓는다
for i in range(1,num_vtx+1):
    if vtx_left[i]:
        continue
    que.append(i)
    answer.append(i)

def bfs():
    while que:
        now = que.popleft()
        # now와 연결된 간선들에 작업시작
        for i in vtx_connected[now]:
            # vtx_left 횟수가 남은 애들한테 -1 아니면 이미 answer에 추가됐을것.
            if vtx_left[i]:
                vtx_left[i] -=1
                # vtx_left가 0이 된 애들은 answer과 que 에 append한다.
                if vtx_left[i] == 0:
                    answer.append(i)
                    que.append(i)
bfs()
print(*answer)
