import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

num_coin, target = map(int,input().strip().split())

coin = set()

for _ in range(num_coin):
    coin.add(int(input()))

coin = list(coin)
coin.sort()
que = deque()
visited = defaultdict(int)
que.append((0,target))

def bfs():
    while que:
        num,target = que.popleft()
        for n_c in coin:
            new_target = target-n_c
            if new_target == 0:
                return num+1
            if new_target >0 and not visited[new_target]:
                que.append((num+1,new_target))
                visited[new_target]=1
    return -1
print(bfs())




