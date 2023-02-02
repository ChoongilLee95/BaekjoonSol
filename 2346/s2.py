
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

num_b = list(map(int, input().strip().split()))

num_queue = deque()

for i in range(0,N):
    num_queue.append((i+1,num_b[i]))

ans = []

for i in range(N):
    bulloon, move = num_queue.popleft()
    if move >0:
        move-=1
    num_queue.rotate(-move)
    ans.append(bulloon)
print(*ans)