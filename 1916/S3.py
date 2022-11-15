import sys
import heapq
from sys import maxsize

num_city  = int(sys.stdin.readline().strip())
num_bus = int(sys.stdin.readline().strip())

rute = [[] for _ in range(num_city+1)]
for _ in range(num_bus):
    a1,a2,cost = map(int,sys.stdin.readline().strip().split())
    rute[a1].append((cost,a2))
start,end = map(int,sys.stdin.readline().strip().split())
# todo 리스트에 cost가 낮고 cost가 같다면 방문위치의 수가 작은 순서대로 넣는다.(heap)
# 고려사항
# 중간에 더 효율적인 경우의 수가 생긴다 -> 비효율적인 요소가 계속해서 자신의 자식을 수행한다
# heap으로 더 효율적인 거 부터 시행 -> 비효율 적인 애들은 나중에 시행된다.
# pop한게 효율적인 것인지(방문판단 & to_cost가 더 낮은지 판단) 판단 후 시행, 다음에 넣을 애들이 효율적인 요소일때 넣는다.
to_cost = [maxsize]*(num_city+1)
def dijkstra(start,end):
    todo = []
    todo.append((0,start))
    to_cost[start] = 0
    while todo:
        total_cost,now = heapq.heappop(todo)
        if now == end:
            continue
        elif to_cost[now] < total_cost:
            continue
        for cost,next in rute[now]:
            if to_cost[next] > cost+total_cost:
                to_cost[next] = cost+total_cost
                heapq.heappush(todo,(cost+total_cost,next))
dijkstra(start,end)
print(to_cost[end])
