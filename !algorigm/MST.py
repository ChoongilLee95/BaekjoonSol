import sys
import heapq
input = sys.stdin.readline

## union_find를 이용한 Kruskal 풀이

V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))

Elist.sort(key=lambda x: x[2])

## root를 찾는 과정에서 최신화가 된다.
def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
print(answer)

## Prim풀이

V, E = map(int, input().split())
chk = [False]*(V+1)
edge = [[] for _ in range(V+1)]
heap = [[0,1]]
for _ in range(E):
    a1, a2, cost = map(int,input().split())
    edge[a1].append([cost,a2])
    edge[a2].append([cost,a1])
total_cost = 0
while heap:
    cost,new_edge = heapq.heappop(heap)
    if chk[new_edge] == False:
        chk[new_edge] = True
        total_cost +=cost
        for next_edge in edge[new_edge]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap,next_edge)
print(total_cost)
